import numpy as np


def sort_worthy(thresh_row: np.ndarray) -> bool:
    """Determines if any of pixels in row need sorting according to thresh"""
    return True if np.any(thresh_row) else False


def mode_index(mode: str) -> int:
    """Returns an index value based on user mode"""
    modes = {'H': 0, 'S': 1, 'V': 2, 'R': 0, 'G': 1, 'B': 2}
    return modes[mode]


def quicksort(
    partition_array: np.ndarray,
    m: int,
    reverse: bool,
) -> np.ndarray:
    """Sorts partition using np.argsort"""
    sorted_partition = partition_array[
        partition_array[:, m].argsort(kind='stable')
    ]
    if reverse:
        sorted_partition = sorted_partition[::-1]

    return sorted_partition


def partition(
    row: np.ndarray,
    thresh_row: np.ndarray,
    mode: str,
    reverse: bool,
    full_sort: bool,
) -> np.ndarray:
    """Takes group of consecutive white pixels and sends them to quicksort"""
    m = mode_index(mode)
    # Skip pixel loop if sorting all pixels (significant speed increase)
    if full_sort:
        sorted_row = quicksort(row, m, reverse)
    else:
        sorted_row = np.empty((0, 3), np.uint8)
        t_mask = np.ma.make_mask(thresh_row)

        indicies = np.nonzero(t_mask[1:] != t_mask[:-1])[0] + 1
        spr = np.split(row, indicies)
        spm = np.split(t_mask, indicies)

        for i, s in enumerate(spr):
            if spm[i].any():
                srt = quicksort(s, m, reverse)
                sorted_row = np.concatenate((sorted_row, srt))
            else:
                sorted_row = np.concatenate((sorted_row, s))
    return sorted_row


def sort_pixels(
    row: np.ndarray,
    thresh_row: np.ndarray,
    mode: str,
    reverse: bool,
    full_sort: bool,
) -> np.ndarray:
    """Each row in image data is sorted and stacked back int one image"""
    if sort_worthy(thresh_row):
        sorted_ndarray = np.empty((0, 3), np.uint8)
        sorted_row = partition(row, thresh_row, mode, reverse, full_sort)
        sorted_ndarray = np.vstack((sorted_ndarray, sorted_row))

        return sorted_ndarray

    else:
        # No pixels to be sorted in this row.
        return row
