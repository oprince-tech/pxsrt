from pxsrt import args
import numpy as np


def read_thresh(data: np.ndarray,
                l: int=args.l_threshold,
                u: int=args.u_threshold) -> np.ndarray:
    """
    Creates a threshold map from image data and desire threshold range (0-255).
    """
    thresh_data = np.copy(data)

    if args.outer:
        thresh_data[thresh_data < l] = 255
        thresh_data[thresh_data >= u] = 255
        thresh_data[thresh_data != 255] = 0

    else:
        thresh_data[thresh_data <= l] = 0
        thresh_data[thresh_data > u] = 0
        thresh_data[thresh_data != 0] = 255

    if args.mode == 'H' or args.mode == 'R':
        thresh_data = np.flip(thresh_data, axis=2)
        thresh_data[:,:,:2] = 0
    elif args.mode == 'S' or args.mode == 'G':
        thresh_data = np.roll(thresh_data, 1 ,axis=2)
        thresh_data[:,:,:2] = 0
    else:
        thresh_data[:,:,:2] = 0

    return thresh_data
