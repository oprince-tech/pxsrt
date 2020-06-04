from PIL import Image, ImageFilter
import args


def load_image():
    with Image.open('./images/'+args.input_image).convert('HSV') as img:
        thresh_img = img.convert('HSV')
        data = img.load()
        thresh_data = thresh_img.load()
    preview_img = Image.new('RGB', img.size)

    # print("IMG: %s" % (img))
    # print("thresh_img: %s" % (thresh_img))
    # print("data: %s" % (data))
    # print("thresh_data: %s" % (thresh_data))

    return img, thresh_img, data, thresh_data, preview_img
