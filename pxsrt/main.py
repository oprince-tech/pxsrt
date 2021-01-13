import numpy as np
from PIL import Image
from pxsrt import sorter
from pxsrt.mode import target_mode
from pxsrt.load import load_image
from pxsrt.reader import read_thresh
from pxsrt.utils import generate_preview
from pxsrt.defaults import defaults
from multiprocessing import Pool


def pxsrt(image,
          mode=defaults['mode'],
          direction=defaults['direction'],
          l_threshold=defaults['l_threshold'],
          u_threshold=defaults['u_threshold'],
          outer=defaults['outer'],
          reverse=defaults['reverse'],
          preview=defaults['preview'],
          save=defaults['save']) -> str:
    """To use as a package:
            from pxsrt.main import pxsrt
            pxsrt('earth.jpg', [OPTIONS]) -> returns PIL image
    """

    target = target_mode(mode.upper())
    data = load_image(image, target, mode, direction)
    thresh_data = read_thresh(data,
                              l_threshold,
                              u_threshold,
                              outer,
                              mode)
    if preview:
        thresh_data = generate_preview(data, thresh_data)

    with Pool() as pool:
        sorted_ndarray = pool.starmap(sorter.sort_pixels,
                                      zip(data, thresh_data))
    del data, thresh_data

    sorted_pixels = np.asarray(sorted_ndarray)
    if direction.lower() == 'v':
        sorted_pixels = np.transpose(sorted_pixels, (1, 0, 2))

    output = Image.fromarray((sorted_pixels).astype(np.uint8), mode=target)
    del sorted_pixels

    output = output.convert("RGB")
    print(type(output))
    return output


if __name__ == "__main__":
    pxsrt()
