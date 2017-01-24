from PIL import Image
import args

def load_image():
    user_threshold = int(args.threshold)
    img = Image.open('./images/'+args.input_image).convert("RGB")
    thresh_img = img.convert(args.mode)
    data = img.load()
    thresh_data = thresh_img.load()
    output = Image.new('RGB', img.size)

    return user_threshold, img, thresh_img, data, thresh_data, output
