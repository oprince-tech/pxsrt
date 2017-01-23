import argparse

p = argparse.ArgumentParser(
    print("""
  | Pixel Sorter |
    """),
    usage='%(prog)s [-h] [IMAGE] [-m MODE] [-d DIRECTION] [-t THRESHOLD] [-r REVERSE] [-u UPPER]'
)
p.add_argument("Image", help="Name of file in images folder. Ex: earth.jpg")
p.add_argument("-m", "--mode", help="1/L/P", default="P", metavar='\b')
p.add_argument("-d", "--direction", help="v (vertical) or h (horizontal)", default="h", metavar='\b')
p.add_argument("-t", "--threshold", help="integer 0 to 255", type=int, default=255, metavar='\b')
p.add_argument("-r", "--reverse", help="Reverse the order pixels are sorted.", default='', action="store_const", const="r")
p.add_argument("-u", "--upper", help="Sort the lighter pixels.", default='', action="store_const", const="u")
__args = p.parse_args()

input_image =   __args.Image
mode        =   __args.mode
direction   =   __args.direction
threshold   =   __args.threshold
reverse     =   __args.reverse
upper       =   __args.upper

if upper == 'u':
    u   = (255, 255, 255)
    l   = (0, 0, 0)
else:
    u = (0, 0, 0)
    l = (255, 255, 255)
