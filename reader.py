import args
import numpy as np


def read_thresh(data, user_threshold):
    thresh_data = np.copy(data)


    if args.upper:
        thresh_data[thresh_data >= user_threshold] = 255
        thresh_data[thresh_data != 255] = 0
    else:
        thresh_data[thresh_data < user_threshold] = 255
        thresh_data[thresh_data != 255] = 0

    if args.mode == 'H':
        thresh_data = np.flip(thresh_data, axis=2)
        thresh_data[:,:,:2] = 0
    elif args.mode == 'S':
        thresh_data = np.roll(thresh_data, 1 ,axis=2)
        thresh_data[:,:,:2] = 0
    else:
        thresh_data[:,:,:2] = 0


    return thresh_data
