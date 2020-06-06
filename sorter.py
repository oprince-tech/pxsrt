import args
import numpy as np


def mode_index():
    modes = {'H': 0, 'S': 1, 'V':2}
    return modes[args.mode]

def quicksort(partition_array, m):
    sorted_partition = partition_array[partition_array[:,m].argsort()]
    if args.reverse:
        sorted_partition = sorted_partition[::-1]
    return sorted_partition


def partition(row, thresh_row):
    m = mode_index()
    sorted_row = np.empty((0, 3), np.uint8)
    partition_array = np.empty((0, 3), np.uint8)

    for p, t in zip(row, thresh_row):
        if t[2] == 255:
            partition_array = np.append(partition_array, np.array([p]), axis=0)

        else:
            if len(partition_array) >= 1:
                sorted_partition = quicksort(partition_array, m)
                sorted_row = np.append(sorted_row, np.array(sorted_partition), axis=0)
                sorted_row = np.append(sorted_row, np.array([p]), axis=0)
            else:
                sorted_row = np.append(sorted_row, np.array([p]), axis=0)
            partition_array = np.empty((0, 3), int)
    if len(partition_array) >= 1:
        sorted_partition = quicksort(partition_array, m)
        sorted_row = np.append(sorted_row, np.array(sorted_partition), axis=0)

    return sorted_row

def sort_pixels(row, thresh_row):
    ### more efficient to buffer the new rows using python than using numpy
    sorted_pixels = []
    sorted_row = partition(row, thresh_row)
    sorted_pixels.extend(sorted_row)

    return sorted_pixels
