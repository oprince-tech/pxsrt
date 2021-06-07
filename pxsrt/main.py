from itertools import repeat
from multiprocessing import Pool

import numpy as np
from PIL import Image  # type: ignore

from pxsrt import sorter
from pxsrt import utils
from pxsrt.load import load_image
from pxsrt.mode import target_mode
from pxsrt.reader import read_thresh


def pxsrt(
    image: str,
    mode: str = 'V',
    direction: str = 'h',
    L_threshold: int = 0,
    U_threshold: int = 255,
    outer: bool = False,
    reverse: bool = False,
    preview: bool = False,
    save: bool = False,
    cli: bool = False,
) -> Image:
    """To use as a package:
            from pxsrt.main import pxsrt
            pxsrt('tokyo.jpg', [OPTIONS]) -> returns PIL image
    """
    target = target_mode(mode.upper())
    data = load_image(image, target, mode, direction)
    thresh_data = read_thresh(
        data,
        L_threshold,
        U_threshold,
        outer,
        mode,
    )
    if cli and preview:
        thresh_data, final_args = utils.generate_preview(data, thresh_data)
    else:
        final_args = {
            'threshold': [L_threshold, U_threshold],
            'outer': outer,
            'mode': mode,
        }

    if final_args['threshold'][0] == 0 and final_args['threshold'][1] == 255:
        full_sort = True
    else:
        full_sort = False

    with Pool() as pool:
        sorted_ndarray = pool.starmap(
            sorter.sort_pixels,
            zip(
                data,
                thresh_data,
                repeat(mode),
                repeat(reverse),
                repeat(full_sort),
            ),
        )

    del data, thresh_data

    sorted_pixels = np.asarray(sorted_ndarray)
    if direction.lower() == 'v':
        sorted_pixels = np.transpose(sorted_pixels, (1, 0, 2))

    output_image = Image.fromarray(
        (sorted_pixels).astype(np.uint8), mode=target,
    )
    del sorted_pixels

    output_image = output_image.convert('RGB')

    if cli and save:
        utils.save_sort(
            output_image,
            input_image=image,
            mode=final_args['mode'],
            direction=direction,
            L_threshold=final_args['threshold'][0],
            U_threshold=final_args['threshold'][1],
            outer=final_args['outer'],
            reverse=reverse,
        )

    return output_image
