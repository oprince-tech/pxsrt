from PIL import Image
import time
import subprocess
import numpy as np
from pxsrt import args
from pxsrt import reader

def generate_preview(data: np.ndarray, thresh_data: np.ndarray) -> np.ndarray:
    """Generate a preview of the pixels to be sorted.

    White -- Pixels to be sorted.
    Black -- Pixels that will be ignored.
    """
    user_preview_choice = False
    while not user_preview_choice:
        preview_img = Image.fromarray(thresh_data,
                                      mode='HSV').convert(mode='RGB')
        preview_img.save('./images/preview.png')

        p = subprocess.Popen(['eog', './images/preview.png'])

        choice = (input("Continue with this threshold map? Y/N: ")).lower()
        if choice == "y":
            p.kill()
            user_preview_choice = True
        else:
            user_new_threshold = False
            while not user_new_threshold:
                try:
                    l_threshold = int(input(
                            "Enter a new lower boundary (0-255): "))
                    u_threshold = int(input(
                            "Enter a new upper boundary (0-255): "))
                    p.kill()
                    thresh_data = reader.read_thresh(data,
                                                     l=l_threshold,
                                                     u=u_threshold)
                    user_new_threshold = True
                except ValueError as e:
                    print(f"{type(e).__name__}: " \
                          f"Invalid number. " \
                          f"Numbers must be within the range of 0 and 255")
                except Exception as e:
                    print(f"{type(e).__name__}: {e}")


    return thresh_data
