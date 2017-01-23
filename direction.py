import args

def get_direction(img, data, thresh_img, thresh_data):
    if args.direction == 'v':
        img = img.rotate(90, expand=True)
        img.size = ((img.size[0]-1), img.size[1])
        data = img.load()
        thresh_img = thresh_img.rotate(90, expand=True)
        thresh_img.size = img.size
        thresh_data = thresh_img.load()

        return img, data, thresh_img, thresh_data

    else:
        return img, data, thresh_img, thresh_data
