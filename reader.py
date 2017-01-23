import args, direction

def threshold(value, thresh_pixels, user_threshold, index):
    if value >= user_threshold:
        thresh_pixels[index].append(args.u)
    else:
        thresh_pixels[index].append(args.l)

def read(img, data, thresh_data, user_threshold):
    def get_value(x, y):
        return thresh_data[x, y]
    def get_data(x, y):
        return data[x, y]
    pixels = []
    thresh_pixels = []
    for y in range(img.size[1]):
        pixels.append([])
        thresh_pixels.append([])
        for x in range(img.size[0]):
            value = get_value(x, y)
            p_data = get_data(x, y)
            pixels[y].append(p_data)
            threshold(value, thresh_pixels, user_threshold, y)

    return pixels, thresh_pixels
