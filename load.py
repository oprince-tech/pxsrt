from PIL import Image
import args
import numpy as np
import sys

def load_image(target):
    """Locate file and return image data as an np array."""
    try:
        with Image.open('./images/'+args.input_image) as img:
            #future# avoid converting image already in correct mode
            try:
                img = img.convert(target)
            except:
                raise

            if args.direction == 'v':
                img = img.rotate(90, expand=True)
            test_data = img.load()
            data = np.asarray(img)

        return data

    except:
        raise
