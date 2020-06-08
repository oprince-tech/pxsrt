from PIL import Image, ImageFilter
import args
import numpy as np


def load_image():
    with Image.open('./images/'+args.input_image).convert('HSV') as img:
        if args.direction == 'v':
            img = img.rotate(90, expand=True)
        data = np.asarray(img)

    return data
