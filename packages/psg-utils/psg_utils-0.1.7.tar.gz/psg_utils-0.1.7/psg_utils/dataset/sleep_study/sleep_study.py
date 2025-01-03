"""
Implements the SleepStudy class which represents a sleep study (PSG)
"""

import logging
import numpy as np
from typing import Union, Tuple
from psg_utils import errors
from psg_utils.io.channels import RandomChannelSelector
from psg_utils.io.high_level_file_loaders import load_psg, load_hypnogram
from psg_utils.preprocessing import (apply_scaling, strip_funcs, apply_strip_func,
                                     assert_scaler, set_psg_sample_rate,
                                     quality_control_funcs, assert_equal_length,
                                     apply_quality_control_func,
                                     apply_filtering,
                                     apply_notch_filtering)
from psg_utils.hypnogram.utils import create_class_int_to_period_idx_dict
from psg_utils.dataset.sleep_study.subject_dir_sleep_study_base import SubjectDirSleepStudyBase
from psg_utils.time_utils import TimeUnit

logger = logging.getLogger(__name__)


def assert_header_fields(header):
    """ Check for minimally required fields of a header dict """
    check = (('sample_rate', False), ('channel_names', False), ('date', True))
    for c, replace_with_none in check:
        if c not in header:
            if replace_with_none:
                header[c] = None
            else:
                raise ValueError("Invalid header file loaded, did not find "
                                 "attribute {} in header {}".format(c, header))


class SleepStudy(SubjectDirSleepStudyBase):
    """
    Represents a PSG sleep study and (optionally) a manually scored hypnogram
    """
    def __init__(self,
                 subject_dir,
                 psg_regex=None,
                 hyp_regex=None,
                 header_regex=None,
                 no_hypnogram=None,
                 annotation_dict=None,
                 period_length: [int, float] = 30,
                 time_unit: Union[TimeUnit, str] = TimeUnit.SECOND,
                 internal_time_unit: Union[TimeUnit, str] = TimeUnit.MILLISECOND,
                 on_overlapping: str = "RAISE",
                 load=False):
        """
        Initialize a SleepStudy object from PSG/HYP data

        PSG: A file that stores polysomnography (PSG) data
        HYP: A file that stores the sleep stages / annotations for the PSG

        Takes a path pointing to a directory in which two or more files are
        located. One of those files should be a PSG (data) file and unless
        no_hypnogram == True another should be a hypnogram/sleep stages/labels
        file. The PSG(/HYP) files are automatically automatically inferred
        using a set of simple rules when psg_regex or hyp_regex are None
        (refer to the 'psg_utils.dataset.utils.find_psg_and_hyp' function).
        Otherwise, the psg_regex and/or hyp_regex is used to match against
        folder content. Each regex should have exactly one match within
        'subject_dir'.

        Args:
            subject_dir:      (str)         File path to a directory storing the
                                              subject data.
            psg_regex:        (str)         Optional regex used to select PSG file
            hyp_regex:        (str)         Optional regex used to select HYP file
            header_regex:     (str)         Optional regex used to select a header file
                                            OBS: Rarely used as most formats store headers internally, or
                                              have header paths which are inferrable from the psg_path.
            no_hypnogram      (bool)        Initialize without ground truth data.
            annotation_dict   (dict)        A dictionary mapping from labels in the hyp_file_path file to integers
            period_length      (int/float)  Sleep 'epoch' (segment/period) length in units 'time_unit' (see below)
            time_unit          (TimeUnit)   TimeUnit object specifying the unit of time of 'period_length'
            internal_time_unit (TimeUnit)   TimeUnit object specifying the unit of time to use internally for storing
                                              times. Affects the values returned by methods or attributes such as
                                              self.period_length.
            on_overlapping:     (str)        One of 'FIRST', 'LAST', 'MAJORITY', , 'RAISE'.
                                               Controls the behaviour when a discrete period of length
                                               self.period_length overlaps 2 or more different classes
                                               in the original hypnogram. See SparseHypnogram.get_period_at_time for
                                               details.
            load              (bool)        Load the PSG object at init time.
        """
        super(SleepStudy, self).__init__(
            subject_dir=subject_dir,
            psg_regex=psg_regex,
            hyp_regex=hyp_regex,
            header_regex=header_regex,
            no_hypnogram=no_hypnogram,
            annotation_dict=annotation_dict,
            period_length=period_length,
            time_unit=time_unit,
            internal_time_unit=internal_time_unit,
            on_overlapping=on_overlapping
        )
        # Hidden attributes controlled in property functions to limit setting
        # of these values to the load() function
        self._scaler = None
        self._scaler_obj = None
        self._load_time_random_channel_selector = None
        self._strip_func = None
        self._quality_control_func = None
        self._filter_settings = None
        self._notch_filter_settings = None
        self._sample_rate = None
        self._date = None
        self._org_sample_rate = None

        # Define attributes that will be dumped on self.unload calls
        self._none_on_unload = (
            '_psg', '_date', '_org_sample_rate',
            '_hypnogram', '_scaler_obj', '_class_to_period_dict'
        )
        # Temp fix to stop QA warnings on each load in a Queue object
        self.times_loaded = 0

        if load:
            self.load()

    def __str__(self):
        if self.loaded:
            t = (self.identifier, len(self.select_channels), self.date,
                 self.sample_rate, self.hypnogram is not False)
            return "SleepStudy(loaded=True, identifier={:s}, N channels: " \
                   "{}, date: {}, sample_rate={:.1f}, hypnogram={})".format(*t)
        else:
            return repr(self)

    def __repr__(self):
        return "SleepStudy(loaded={}, identifier={})".format(self.loaded,
                                                             self.identifier)

    @property
    def class_to_period_dict(self) -> dict:
        """
        Returns the class_to_period_dict, which maps a class integer
        (such as 0) to an array of period indices that correspond to PSG
        periods/epochs/segments that in the ground truth is scored as the that
        class (such as 0).
        """
        return self._class_to_period_dict

    @property
    def load_time_random_channel_selector(self) -> Union[RandomChannelSelector, None]:
        """
        TODO

        Returns:

        """
        return self._load_time_random_channel_selector

    @load_time_random_channel_selector.setter
    def load_time_random_channel_selector(self, channel_selector):
        """
        TODO

        Args:
            channel_selector:

        Returns:

        """
        if channel_selector and self.select_channels:
            raise RuntimeError("Setting the 'load_time_random_channel_selector' "
                               "attribute is not possible with set values in "
                               "'select_channels'")
        if channel_selector is not None and not \
                isinstance(channel_selector, RandomChannelSelector):
            raise TypeError("Expected 'channel_selector' argument to be of "
                            "type {}, got {}".format(type(RandomChannelSelector),
                                                     type(channel_selector)))
        self._load_time_random_channel_selector = channel_selector

    @property
    def sample_rate(self) -> int:
        """ Returns the currently set sample rate """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate: int):
        """
        Set a new sample rate
        Is considered at load-time
        Setting with self.loaded == True forces a reload.
        """
        sample_rate = int(sample_rate)
        if sample_rate <= 0:
            raise ValueError("Sample rate must be a positive integer, "
                             "got {}".format(sample_rate))
        self._sample_rate = sample_rate
        if self.loaded:
            self.reload(warning=True)

    @property
    def org_sample_rate(self) -> int:
        """
        Returns the original sample rate
        """
        return self._org_sample_rate

    @property
    def date(self):
        """ Returns the recording date, may be None """
        return self._date

    @property
    def scaler(self) -> Union[str, None]:
        """ Returns the scaler type (string), see setter method """
        return self._scaler

    @scaler.setter
    def scaler(self, scaler: str):
        """
        Sets a scaler type.
        Is considered at load-time
        Setting with self.loaded == True forces a reload.

        Args:
            scaler: String, naming a sklearn.preprocessing scaler.
        """
        if not assert_scaler(scaler):
            raise ValueError("Invalid scaler, does not exist {}".format(scaler))
        self._scaler = scaler
        if self.loaded:
            self.reload(warning=True)

    @property
    def scaler_obj(self):
        """ Reference to the scaler object """
        return self._scaler_obj

    @property
    def strip_func(self) -> Union[None, Tuple[str, dict]]:
        """
        See setter method
        strip_func - when set - is a 2-tuple (strip_func_name, kwargs)
        """
        return self._strip_func

    def set_strip_func(self, strip_func: str, **kwargs):
        """
        Sets a strip function. Strip functions are applied to the PSG/HYP pair
        at load time and may deal with minor differences between the length
        of the PSG and HYP (e.g. if the PSG is longer than the HYP file).
        See psg_utils.preprocessing.strip_funcs

        Forces a reload if self.loaded is True

        Args:
            strip_func: A string naming a strip_func in:
                        psg_utils.preprocessing.strip_funcs
            kwargs:     Other kw arguments that will be passed to the strip
                        function.
        """
        if strip_func not in strip_funcs.__dict__:
            self.raise_err(ValueError, "Invalid strip function "
                                       "{}".format(strip_func))
        self._strip_func = (strip_func, kwargs)
        if self.loaded:
            self.reload(warning=True)

    @property
    def quality_control_func(self) -> Union[None, Tuple[str, dict]]:
        """ See setter method """
        return self._quality_control_func

    def set_quality_control_func(self, quality_control_func: str, **kwargs):
        """
        Sets a quality control function which is applied to all segments
        of a PSG (as determined by self.period_length) and may alter the
        values of said segments.

        Applies at load-time, forces a reload if self.loaded == True.

        Args:
            quality_control_func:  A string naming a quality control function in:
                                   psg_utils.preprocessing.quality_control_funcs
            **kwargs:              Parameters passed to the quality control func at load
        """
        if quality_control_func not in quality_control_funcs.__dict__:
            self.raise_err(ValueError, "Invalid quality control function "
                                       "{}".format(quality_control_func))
        self._quality_control_func = (quality_control_func, kwargs)
        if self.loaded:
            self.reload(warning=True)

    @property
    def filter_settings(self) -> Union[None, dict]:
        """ See setter method """
        return self._filter_settings

    @filter_settings.setter
    def filter_settings(self, filter_settings: dict):
        """
        TODO
        """
        self._filter_settings = filter_settings
        if self.loaded:
            self.reload(warning=True)

    @property
    def notch_filter_settings(self) -> Union[None, dict]:
        """ See setter method """
        return self._notch_filter_settings

    @notch_filter_settings.setter
    def notch_filter_settings(self, notch_filter_settings: dict):
        """
        TODO
        """
        self._notch_filter_settings = notch_filter_settings
        if self.loaded:
            self.reload(warning=True)

    @property
    def loaded(self) -> bool:
        """
        Returns whether the SleepStudy data is currently loaded or not
        """
        return not any((self.psg is None,
                        self.hypnogram is None))

    def _load_with_any_in(self, channel_sets, allow_missing_channels=False):
        """
        Normally not called directly, usually called from self._load.

        Circulates a list of lists of proposed channel names to load,
        attempting to load using any of the sets (in specified order), raising
        ChannelNorFound error if none of the sets could be loaded.

        Args:
            channel_sets: List of lists of strings, each naming a channel to
                          load.
            allow_missing_channels: A bool to indicate if missing channels are allowed or not.

        Returns:
            If one of the sets of channels could be loaded, returns the
            PSG array of shape [-1, n_channels], the header and the list of
            channels that were successfully loaded (an elem. of channel_sets).
        """
        for i, channel_set in enumerate(channel_sets):
            try:
                if self.load_time_random_channel_selector:
                    # On reloads, the set_load_channel group will have been set
                    # if using a load_time_channel_selector, remove it here.
                    channel_set = None
                temp = self.load_time_random_channel_selector
                psg, header = load_psg(psg_file_path=self.psg_file_path,
                                       load_channels=channel_set or None,
                                       load_time_channel_selector=temp,
                                       header_file_path=self.header_file_path,
                                       allow_missing_channels=allow_missing_channels)
                return psg, header
            except errors.ChannelNotFoundError as e:
                if i < len(channel_sets) - 1:
                    # Try nex set of channels
                    continue
                else:
                    s, sa = self.select_channels, \
                            self.alternative_select_channels
                    err = errors.ChannelNotFoundError("Could not load "
                                                      "select_channels {} or "
                                                      "alternative_select_"
                                                      "channels "
                                                      "{}".format(s, sa))
                    raise err from e

    def _load(self, allow_missing_channels=False):
        """
        Loads data from the PSG and HYP files
        -- If self.select_channels is set (aka non empty list), only the column
           names matching this list will be kept.
        -- PSG data is kept as a numpy array. Use self.select_channels to map
           between names and the numpy array
        -- If self.scaler is set, the PSG array will be scaled according to
           the specified sklearn.preprocessing scaler
        -- If self.hyp_strip_func is set, this function will be applied to the
           hypnogram object.
        """
        self._psg, header = self._load_with_any_in(self._try_channels, allow_missing_channels)
        self._set_loaded_channels(header['channel_names'])
        self._set_header_fields(header)

        if self.hyp_file_path is not None and not self.no_hypnogram:
            self._hypnogram, self.annotation_dict = load_hypnogram(
                self.hyp_file_path,
                period_length=self.get_period_length_in(self.data_time_unit),
                time_unit=self.data_time_unit,
                annotation_dict=self.annotation_dict,
                sample_rate=header["sample_rate"]
            )
        else:
            self._hypnogram = False

        if self.strip_func:
            # Strip the data using the passed function on the passed class
            self._psg, self._hypnogram = apply_strip_func(self, self.org_sample_rate)
        elif self.hypnogram:
            try:
                assert_equal_length(self.psg, self.hypnogram, self.org_sample_rate)
            except errors.StripError as e:
                self.raise_err(RuntimeError, "PSG and hypnogram are not equally "
                                             "long in seconds. Consider setting a "
                                             "strip_function. "
                                             "See psg_utils.preprocessing.strip_funcs.", _from=e)

        if self.filter_settings:
            # Apply mne.mne.filter.filter_data function with specified settings
            self._psg = apply_filtering(self._psg, self.org_sample_rate, **self.filter_settings)

        if self.notch_filter_settings:
            # Apply mne.mne.filter.notch_filter function with specified settings
            self._psg = apply_notch_filtering(self._psg, self.org_sample_rate, **self.notch_filter_settings)

        if self.quality_control_func:
            # Run over epochs and assess if epoch-specific changes should be
            # made to limit the influence of very high noise level ecochs etc.
            self._psg = apply_quality_control_func(self,
                                                   self.org_sample_rate,
                                                   warn_fraction=0.15,
                                                   warn=not bool(self.times_loaded))

        # Set different sample rate of PSG?
        if self.org_sample_rate != self.sample_rate:
            self._psg = set_psg_sample_rate(self._psg,
                                            new_sample_rate=self.sample_rate,
                                            old_sample_rate=self.org_sample_rate)
        if self.scaler:
            self._psg, self._scaler_obj = apply_scaling(self.psg, self.scaler)

        # Store dictionary mapping class integers to period idx of that class
        if self.hypnogram:
            self._class_to_period_dict = create_class_int_to_period_idx_dict(
                self.hypnogram, self.on_overlapping
            )
        # Ensure converted to float32 ndarray
        self._psg = self._psg.astype(np.float32)
        self.times_loaded += 1

    def _set_header_fields(self, header: dict):
        """
        TODO

        Args:
            header:

        Returns:

        """
        # Ensure all header information is available
        assert_header_fields(header)
        self._date = header["date"]
        self._org_sample_rate = header["sample_rate"]
        self._sample_rate = self._sample_rate or self._org_sample_rate

    def load(self, reload=False, allow_missing_channels=False):
        """
        High-level function invoked to load the SleepStudy data
        """
        if reload or not self.loaded:
            try:
                self._load(allow_missing_channels)
            except Exception as e:
                raise errors.CouldNotLoadError("Unexpected load error for sleep "
                                               "study {}. Please refer to the "
                                               "above traceback.".format(self.identifier),
                                               study_id=self.identifier) from e
        return self

    def unload(self):
        """ Unloads the PSG, header and hypnogram data """
        for attr in self._none_on_unload:
            setattr(self, attr, None)

    def reload(self, warning=True, allow_missing_channels=False):
        """ Unloads and loads """
        if warning and self.loaded:
            print("Reloading SleepStudy '{}'".format(self.identifier))
        self.load(reload=True, allow_missing_channels=allow_missing_channels)

    def get_psg_shape(self) -> tuple:
        """
        TODO

        Returns:

        """
        return self.psg.shape

    def get_class_counts(self, as_dict=False) -> Union[dict, np.ndarray]:
        """
        Computes the class counts for the loaded hypnogram.

        Args:
            as_dict: (bool) return a dictionary mapping from class labels
                            (ints) to the count (int) for that class instead of
                            the typical array of class counts.

        Returns:
            An ndarray of length n_classes of counts if as_dict == False
            Otherwise a dictionary mapping class labels to counts.
        """
        classes = sorted(self._class_to_period_dict.keys())
        counts = np.array([len(self._class_to_period_dict[c]) for c in classes])
        if as_dict:
            return {cls: count for cls, count in zip(classes, counts)}
        else:
            return counts

    def get_class_indices(self, class_int: int) -> np.ndarray:
        return self.class_to_period_dict[class_int]
