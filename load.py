from PIL import Image, ImageFilter
import args


def load_image():
    with Image.open('./images/'+args.input_image).convert("HSV") as img:
        if args.blur > 0:
           img = img.filter(ImageFilter.GaussianBlur(radius=int(args.blur)))
        thresh_img = img.convert("HSV")
        data = img.load()
        thresh_data = thresh_img.load()
    preview_img = Image.new('RGB', img.size)
    output = Image.new('HSV', img.size)

    return img, thresh_img, data, thresh_data, preview_img, output



    # img = Image.open('./images/'+args.input_image).convert("HSV")
    # if args.blur > 0:
    #    img = img.filter(ImageFilter.GaussianBlur(radius=int(args.blur)))
    # thresh_img = img.convert("HSV")
    # data = img.load()
    # thresh_data = thresh_img.load()
    # preview_img = Image.new('RGB', img.size)
    # output = Image.new('HSV', img.size)
    #
    # return img, thresh_img, data, thresh_data, preview_img, output
