import argparse

parser = argparse.ArgumentParser(
    description='Pixelsorter by Oliver Prince',
    usage='%(prog)s <IMAGE> [-m MODE] [-d DIRECTION] [-t THRESHOLD] ' \
          '[-o OUTER] [-r REVERSE] [-b BLUR] [-p PREVIEW]'
)
parser.add_argument("Image",
                    help="Name of file in images folder. Ex: earth.jpg")
parser.add_argument("-m", "--mode",
                    help="H/S/V* R/G/B",
                    default="V",
                    metavar='\b')
parser.add_argument("-d", "--direction",
                    help="v (vertical) or h (horizontal)",
                    default="h",
                    metavar='\b')
parser.add_argument("-t", "--threshold",
                    help="Two integers ranging from 0-255",
                    nargs='+',
                    default=['0', '255'],
                    metavar='\b')
parser.add_argument("-o", "--outer",
                    help="Sort the pixels outside of your threshold range.",
                    action="store_true")
parser.add_argument("-r", "--reverse",
                    help="Reverse the order pixels are sorted.",
                    action="store_true")
parser.add_argument("-p", "--preview",
                    help="Display preview of threshold map",
                    action="store_true")
parser.add_argument("-s", "--save",
                    help="Save sorted image",
                    action="store_true")
__args = parser.parse_args()

input_image = __args.Image
mode = __args.mode
direction = __args.direction
l_threshold = int(__args.threshold[0])
u_threshold = int(__args.threshold[1])
outer = __args.outer
reverse = __args.reverse
preview = __args.preview
save = __args.save
