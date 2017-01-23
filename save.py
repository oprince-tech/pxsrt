from PIL import Image
import os, args

def save(output):
    sub_path        = './images/export/'
    file_extension  = '.jpg'

    if not os.path.exists(sub_path):
        os.makedirs(sub_path)
    base = os.path.splitext(os.path.basename(args.input_image))[0]
    output_base = base + '_' + str(args.mode) + str(args.direction) + str(args.threshold) + str(args.reverse) + str(args.upper) + str(file_extension)
    output_path = ('/').join(args.input_image.split('/')[:-1])
    output_file = output_path + sub_path + output_base
    if args.direction == 'v':
        output = output.transpose(Image.FLIP_LEFT_RIGHT)
    output.save(output_file)
    output.show()
