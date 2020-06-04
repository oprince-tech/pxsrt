import args, load, reader, direction, preview, sorter, save, sys, time, math, itertools
from multiprocessing import Pool
from PIL import Image
import numpy as np


def main():
    t1 = time.time()
    # sys.setrecursionlimit(10**5)
    print("Importing..")
    img, thresh_img, data, thresh_data, preview_img = load.load_image()

    print("Reading Pixels..")
    img, data, thresh_img, thresh_data = direction.get_direction(img, data, thresh_img, thresh_data)
    pixels = reader.read_img(img, data)
    thresh_pixels = reader.read_thresh(img, thresh_data, args.threshold)

    print("Loading Preview...")
    if args.preview:
        thresh_pixels = preview.generate_preview(img, preview_img, thresh_pixels, thresh_data)

    print("Sorting Pixels..")
    sorted_pixels = []
    with Pool() as pool:
        sorted_pixels = pool.starmap(sorter.sort_pixels, zip(pixels, thresh_pixels))

    print("Outputting Pixels..")
    #Converting python array to nparray
    sorted_pixels = np.asarray(sorted_pixels)
    output = Image.fromarray((sorted_pixels).astype(np.uint8), mode='HSV')
    output.convert("RGB")
    output.show()

    t2 = time.time() - t1
    print('{} seconds'.format(t2))
    # save_flag = (input("Would you like to save? Y/N: ")).lower()
    # if save_flag == "y":
    #     print("Saving Image..")
    #     save.save(output)


if __name__ == "__main__":
    main()
