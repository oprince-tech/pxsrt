from PIL import Image, ImageFilter
import args
import numpy as np
import sys

def load_image(target):

    try:
        with Image.open('./images/'+args.input_image) as img:
            #future# avoid converting image already in correct mode
            try:
                img = img.convert(target)
            except:
                exit()

            if args.direction == 'v':
                img = img.rotate(90, expand=True)
            test_data = img.load()
            print(sys.getsizeof(test_data))
            data = np.asarray(img)
            print(data.nbytes)

    return data


    except FileNotFoundError as e:
        print(e)
        exit()

    print(img.size)
