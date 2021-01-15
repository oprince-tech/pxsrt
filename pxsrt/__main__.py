from pxsrt.args import parse_args
from pxsrt.main import pxsrt
from pxsrt.utils import save


def cli():
    """Handles command line calls (E.g., pxsrt tokyo.jpg -m B -t 0 100 -o)"""
    args = parse_args()
    print("NOTE: Larger resolution images will take longer to sort.")
    output = pxsrt(args['input_image'],
                   args['mode'],
                   args['direction'],
                   args['L_threshold'],
                   args['U_threshold'],
                   args['outer'],
                   args['reverse'],
                   args['preview'],
                   args['save'],
                   cli=True)

    if args['save']:
        save(output)

    output.show()