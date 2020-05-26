import argparse

parser = argparse.ArgumentParser(
    print("""
  | Pixel Sorter |
    """),
    usage='%(prog)s [-h] [IMAGE] [-m MODE] [-d DIRECTION] [-t THRESHOLD] [-r REVERSE] [-u UPPER]'
)
parser.add_argument("Image", help="Name of file in images folder. Ex: earth.jpg")
parser.add_argument("-m", "--mode", help="L/P [L (Luminance) / P (256 color Palette) {default}]", default="P", metavar='\b')
parser.add_argument("-d", "--direction", help="v (vertical) or h (horizontal)",
               default="h", metavar='\b')
parser.add_argument("-t", "--threshold", help="integer 0 to 255", type=int, default=255, metavar='\b')
parser.add_argument("-r", "--reverse", help="Reverse the order pixels are sorted.",
               action="store_true")
parser.add_argument("-u", "--upper", help="Sort the lighter pixels.",
               action="store_true")
#parser.add_argument("-b", "--blur", help="Blur Amount", type=int, default=0)
__args = parser.parse_args()

input_image = __args.Image
mode = __args.mode
direction = __args.direction
threshold = __args.threshold
reverse = __args.reverse
upper = __args.upper
#blur = __args.blur
