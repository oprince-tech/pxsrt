import args, load, reader, preview, sorter, save
import sys, time
from multiprocessing import Pool
from PIL import Image
import numpy as np
# import memory_profiler

# @profile
def main():

    print("Importing..")
    data = load.load_image()

    print("Reading Pixels..")
    thresh_data = reader.read_thresh(data, args.threshold)

    print("Loading Preview...")
    if args.preview:
        thresh_data = preview.generate_preview(data, thresh_data)

    print("Sorting Pixels..")
    t1 = time.time()
    with Pool() as pool:
        sorted_pixels = pool.starmap(sorter.sort_pixels, zip(data, thresh_data))
    del data, thresh_data

    print("Outputting Pixels..")
    sorted_pixels = np.asarray(sorted_pixels)
    if args.direction == 'v':
        sorted_pixels = np.transpose(sorted_pixels, (1,0,2))
    output = Image.fromarray((sorted_pixels).astype(np.uint8), mode='HSV')
    del sorted_pixels
    output = output.convert("RGB")
    output.show()

    t2 = time.time() - t1
    print('{} seconds'.format(t2))
    save_flag = (input("Would you like to save? Y/N: ")).lower()
    if save_flag == "y":
        print("Saving Image..")
        save.save(output)


if __name__ == "__main__":
    main()
