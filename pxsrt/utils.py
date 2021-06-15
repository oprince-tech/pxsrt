import os
import subprocess
from pathlib import Path
from typing import Any
from typing import Optional
from typing import Tuple

import numpy as np
from PIL import Image  # type: ignore

from pxsrt import args
from pxsrt import reader


def check_dir_integrity(p: Path) -> None:
    if not p.exists():
        Path.mkdir(p)


def generate_preview(
    data: np.ndarray,
    thresh_data: np.ndarray,
) -> Tuple[np.ndarray, dict]:
    """Generate a preview of the pixels to be sorted.

    White -- Pixels to be sorted.
    Black -- Pixels that will be ignored.
    """

    _args = args.parse_args()
    final_args = {
        'threshold': [_args['L_threshold'], _args['U_threshold']],
        'outer': _args['outer'],
        'mode': _args['mode'],
    }

    while True:
        thresh_data = np.asarray(thresh_data)
        preview_img = Image.fromarray(
            thresh_data,
            mode='HSV',
        ).convert(mode='RGB')

        preview_folder = Path('./pxsrt_previews')
        check_dir_integrity(preview_folder)
        preview_file = preview_folder / 'preview.png'
        preview_img.save(preview_file)

        p = subprocess.Popen(['eog', './pxsrt_previews/preview.png'])

        choice = (input('Continue with this threshold map? Y/N: ')).lower()
        if choice == 'y':
            p.kill()
            break
        else:
            while True:
                try:
                    L_threshold = int(
                        input('Enter a new lower boundary (0-255): '),
                    )
                    U_threshold = int(
                        input('Enter a new upper boundary (0-255): '),
                    )
                    o = input('Target outer pixels? (Y/N): ')
                    outer = True if o.lower() == 'y' else False
                    possible_modes = ['H', 'S', 'V', 'R', 'G', 'B']
                    mode = input('Mode (H, S, V, R, G, B): ')
                    if mode not in possible_modes:
                        raise ValueError(
                            'Mode not accepted. '
                            'Please choose from (H, S, V, R, G, B).',
                        )

                    p.kill()
                    thresh_data = reader.read_thresh(
                        data,
                        outer=outer,
                        mode=mode,
                        L=L_threshold,
                        U=U_threshold,
                    )
                    final_args = {
                        'threshold': [L_threshold, U_threshold],
                        'outer': outer,
                        'mode': mode,
                    }
                except ValueError as e:
                    print(f'{type(e).__name__}: {e}')

                break

    return thresh_data, final_args


def convert(data: np.ndarray) -> None:
    """Convert between RGB and HSV
    In this future this will convert between modes rather than use PIL convert
    """


def create_save_filename(**kwargs: Any) -> Optional[str]:
    base, file_extension = os.path.splitext(
        os.path.basename(kwargs['input_image']),
    )

    save_choice = (input('Would you like to save? Y/N: ')).lower()
    if save_choice == 'y':
        save_as_choice = (input('Save as (leave blank for auto renaming): '))
        if save_as_choice == '':
            save_filename = '{}_{}{}({}-{}){}{}{}'.format(
                base,
                kwargs['mode'],
                kwargs['direction'],
                kwargs['L_threshold'],
                kwargs['U_threshold'],
                kwargs['outer'],
                kwargs['reverse'],
                file_extension,
            )

        else:
            save_filename = save_as_choice
    else:
        return None

    return save_filename


def save_sort(output_image: Image, **kwargs: Any) -> None:
    """Save pixel sorted image ('./pxsrt_exports/')"""
    export_folder = Path('./pxsrt_exports')

    check_dir_integrity(export_folder)
    save_filename = create_save_filename(
        input_image=kwargs['input_image'],
        mode=kwargs['mode'],
        direction=kwargs['direction'],
        L_threshold=kwargs['L_threshold'],
        U_threshold=kwargs['U_threshold'],
        outer=kwargs['outer'],
        reverse=kwargs['reverse'],
    )
    if save_filename:
        print('Saving Image..')
        output_file = export_folder / save_filename
        output_image.save(output_file)
