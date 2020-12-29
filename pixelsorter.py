import args, mode, load, reader, preview, sorter, save

import sys, time
from multiprocessing import Pool
from PIL import Image
import numpy as np
from LogDecorator import logger, exception

@exception(logger)
def main():
    np.set_printoptions(threshold=sys.maxsize)

    print("Initializing...")
    target = mode.target_mode()

    print("Importing...")
    data = load.load_image(target)

    print("Reading Pixels...")
    thresh_data = reader.read_thresh(data, args.threshold)

    print("Loading Preview...")
    if args.preview:
        thresh_data = preview.generate_preview(data, thresh_data)

    print("Sorting Pixels...")
    with Pool() as pool:
        sorted_pixels = pool.starmap(sorter.sort_pixels, zip(data, thresh_data))
    del data, thresh_data

    print("Outputting Pixels..")
    sorted_pixels = np.asarray(sorted_pixels)
    if args.direction.lower() == 'v':
        sorted_pixels = np.transpose(sorted_pixels, (1,0,2))
    output = Image.fromarray((sorted_pixels).astype(np.uint8), mode=target)
    del sorted_pixels
    output = output.convert("RGB")
    output.show()

    if args.save:
        save_choice = (input("Would you like to save? Y/N: ")).lower()
        if save_choice == "y":
            print("Saving Image..")
            save.save(output)

if __name__ == "__main__":
    main()
