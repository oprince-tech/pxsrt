import argparse


def parse_args() -> dict:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='pxsrt by Oliver Prince',
        usage='%(prog)s <IMAGE> [-m MODE] [-d DIRECTION] [-t THRESHOLD] '
              '[-o OUTER] [-r REVERSE] [-p PREVIEW] [-s SAVE]',
    )
    parser.add_argument(
        'Image',
        help='Name of image file. Ex: earth.jpg',
    )
    parser.add_argument(
        '-m', '--mode',
        help='H/S/V* R/G/B',
        default='V',
        choices=('H', 'S', 'V', 'R', 'G', 'B'),
        metavar='\b',
    )
    parser.add_argument(
        '-d', '--direction',
        help='v (vertical) or h (horizontal).',
        choices=('v', 'h'),
        default='h',
        metavar='\b',
    )
    parser.add_argument(
        '-t', '--threshold',
        help='Two integers ranging from 0-255.',
        nargs='+',
        default=['0', '255'],
        metavar='\b',
    )
    parser.add_argument(
        '-o', '--outer',
        help='Sort pixels outside of the threshold range.',
        action='store_true',
    )
    parser.add_argument(
        '-r', '--reverse',
        help='Reverse the order pixels are sorted.',
        action='store_true',
    )
    parser.add_argument(
        '-p', '--preview',
        help='Display preview of threshold map.',
        action='store_true',
    )
    parser.add_argument(
        '-s', '--save',
        help='Save sorted image.',
        action='store_true',
    )
    __args = parser.parse_args()

    return {
        'input_image': __args.Image,
        'mode': __args.mode,
        'direction': __args.direction,
        'L_threshold': int(__args.threshold[0]),
        'U_threshold': int(__args.threshold[1]),
        'outer': __args.outer,
        'reverse': __args.reverse,
        'preview': __args.preview,
        'save': __args.save,
    }
