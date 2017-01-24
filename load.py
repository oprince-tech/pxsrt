from PIL import Image
import args

def load_image():
    img = Image.open('./images/'+args.input_image).convert("RGB")
    thresh_img = img.convert(args.mode)
    data = img.load()
    thresh_data = thresh_img.load()
    output = Image.new('RGB', img.size)

    return img, thresh_img, data, thresh_data, output
