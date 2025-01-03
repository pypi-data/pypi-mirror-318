import logging
import warnings
from itertools import product
from psg_utils.io.channels import ChannelMontageTuple, ChannelMontageCreator
from psg_utils.errors import ChannelNotFoundError, DuplicateChannelError, DuplicateChannelWarning

logger = logging.getLogger(__name__)


def can_create_channels(asked_channels, channels_in_file):
    try:
        ChannelMontageCreator(
            existing_channels=channels_in_file,
            channels_required=asked_channels,
            allow_missing=False
        )
        return True
    except ValueError:
        return False


def check_duplicate_channels(channels, ref_channels=None, raise_or_warn="raise"):
    raise_or_warn = raise_or_warn.lower()
    assert raise_or_warn in ("warning", "warn", "raise")
    ref_channels = ChannelMontageTuple(ref_channels or channels, relax=True)
    channels = ChannelMontageTuple(channels, relax=True)
    for channel in channels:
        if ref_channels.count(channel) > 1:
            s = f"File header contains a channel with name \"{channel.original_name}\" " \
                f"which occurs multiple times in the file: {ref_channels.original_names}). " \
                f"This may cause an error to be raised now or later when the file is loaded " \
                f"if the file is loaded using that channel. " \
                f"Duplicate channel names could result from longer channel names " \
                f"being truncated to identical, shorter names due to limitations in the used file format. " \
                f"Consider renaming your channels uniquely and then try again."
            if raise_or_warn.lower() == "raise":
                raise DuplicateChannelError(s)
            elif raise_or_warn.lower() in ("warn", "warning"):
                warnings.warn(s, DuplicateChannelWarning)


def get_org_include_exclude_channel_montages(load_channels, header,
                                             ignore_reference_channels=False,
                                             allow_missing_channels=True,
                                             allow_auto_referencing=True,
                                             check_duplicates=True):
    """
    TODO

    Args:
        load_channels:
        header:
        ignore_reference_channels:
        allow_missing_channels:
        allow_auto_referencing:
        check_duplicates:

    Returns:

    """
    channels_in_file = ChannelMontageTuple(header['channel_names'], relax=True)
    channel_montage_creator = None
    if load_channels:
        if not isinstance(load_channels, ChannelMontageTuple):
            load_channels = ChannelMontageTuple(load_channels, relax=True)
        if ignore_reference_channels:
            include_channels = load_channels.match_ignore_reference(channels_in_file, take_target=True)
        else:
            include_channels = load_channels.match(channels_in_file, take_target=True)
        if len(include_channels) != len(load_channels):
            if allow_auto_referencing and can_create_channels(load_channels, channels_in_file):
                # Specified channels are referenced, e.g. C3-A2 and may be created from the available C3 and A2
                channel_montage_creator = ChannelMontageCreator(
                    existing_channels=channels_in_file,
                    channels_required=load_channels,
                    allow_missing=False
                )
                include_channels = channel_montage_creator.channels_to_load.match(channels_in_file, take_target=True)
            elif not allow_missing_channels or len(include_channels) == 0:
                raise ChannelNotFoundError(
                    "Could not load {} channels ({}) from file with {} channels "
                    "({}). Found the following {} matches: {}".format(
                        len(load_channels), load_channels.original_names,
                        len(channels_in_file), channels_in_file.original_names,
                        len(include_channels), include_channels.original_names
                    )
                )
            else:
                logger.warning(f"Loading only {len(include_channels)} ({include_channels.original_names}) "
                               f"channels although {len(load_channels)} ({load_channels.original_names}) "
                               f"were requested. This is allowed only because the 'allow_missing_channels' "
                               f"parameter was explicitly set True for this call.")
    else:
        include_channels = channels_in_file
    if check_duplicates:
        check_duplicate_channels(load_channels, channels_in_file, raise_or_warn="raise")
    exclude_channels = [c for c in channels_in_file if c not in include_channels]
    exclude_channels = ChannelMontageTuple(exclude_channels)
    return channels_in_file, include_channels, exclude_channels, channel_montage_creator


def get_channel_group_combinations(*channel_groups, remove_unordered_duplicates=False):
    """
    TODO
    """
    combinations = list(product(*channel_groups))
    if remove_unordered_duplicates:
        # Remove entries that are duplicates after sorting of each channel combination tuple
        # I.e., with combinations [['EEG 1', 'EEG 2'], ['EEG 2', 'EEG 1'], ...] return -> [['EEG 1', 'EEG 2'], ...]
        combs_no_dups = []
        sorted_combs = []
        for combination in combinations:
            sorted_comb = sorted(combination)
            if tuple(sorted_comb) not in sorted_combs:
                combs_no_dups.append(combination)
                sorted_combs.append(tuple(sorted_comb))
        combinations = combs_no_dups
    return combinations
