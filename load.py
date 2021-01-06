from typing import List
from PIL import Image
import args
import numpy as np
import sys

def load_image(target: str) -> np.ndarray:
    try:
        """Locate file and return image data as an np array."""
        with Image.open('./images/'+args.input_image) as img:
            if img.mode != target:
                print(f"Converting ({img.mode} -> {target})...")
                img = img.convert(target)
            if args.direction == 'v':
                img = img.rotate(90, expand=True)
            test_data = img.load()
            data = np.asarray(img)

    except FileNotFoundError as e:
        print(e)
        raise SystemExit
    except Exception as e:
        print(f"Error: {e}")
        raise SystemExit
    else:
        return data
