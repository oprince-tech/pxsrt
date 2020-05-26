import args


if args.upper:
    u, l = (255, 255, 255), (0, 0, 0)
else:
    u, l =  (0, 0, 0), (255, 255, 255)

def threshold(value, thresh_pixels, user_threshold, index):
    if value >= user_threshold:
        thresh_pixels[index].append(u)
    else:
        thresh_pixels[index].append(l)


def read_img(img, data):

    def get_data(x, y):
        return data[x, y]

    pixels = []
    for y in range(img.size[1]):
        pixels.append([])
        for x in range(img.size[0]):
            p_data = get_data(x, y)
            pixels[y].append(p_data)
    return pixels


def read_thresh(img, thresh_data, user_threshold):

    def get_value(x, y):
        return thresh_data[x, y]

    thresh_pixels = []
    for y in range(img.size[1]):
        thresh_pixels.append([])
        for x in range(img.size[0]):
            value = get_value(x, y)
            threshold(value, thresh_pixels, user_threshold, y)
    return thresh_pixels
