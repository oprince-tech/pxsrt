from PIL import Image
import args


def quick_sort(cache):
    if cache == []:
        return cache
    else:
        p = cache[0]
        if args.reverse:
            l = quick_sort([x for x in cache[1:] if (x[0]+x[1]+x[2]) >= (p[0]+p[1]+p[2])])
            r = quick_sort([x for x in cache[1:] if (x[0]+x[1]+x[2]) < (p[0]+p[1]+p[2])])
            return l + [p] + r
        else:
            l = quick_sort([x for x in cache[1:] if (x[0]+x[1]+x[2]) < (p[0]+p[1]+p[2])])
            r = quick_sort([x for x in cache[1:] if (x[0]+x[1]+x[2]) >= (p[0]+p[1]+p[2])])
            return l + [p] + r


def sort_pixels(pixels, thresh):
    sorted_pixels = []
    sort_cache = []

    def pixel_dump(sort_cache):
        dump = quick_sort(sort_cache)
        sorted_pixels.extend(dump)

    for (p, t) in zip(pixels, thresh):
        if t == (255, 255, 255):
            sort_cache.append(p)
        elif t == (0, 0, 0):
            if sort_cache:
                pixel_dump(sort_cache)
                sorted_pixels.append(p)
            else:
                sorted_pixels.append(p)
            sort_cache = []
    if sort_cache:
        pixel_dump(sort_cache)
    return sorted_pixels
