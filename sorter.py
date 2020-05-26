from PIL import Image
import args
from statistics import median #to find median pivot

def find_pivot(cache):
    clen = int(len(cache))
    a = sum(cache[0])
    b = sum(cache[int(clen/2)])
    c = sum(cache[-1])
    if a <= b and b <= c:
        return int(clen/2)
    if b <= a and c <= b:
        return int(clen/2)
    if a <= c and c <= b:
        return -1
    if c <= a and b <= c:
        return -1
    else:
        return 0


def quick_sort(cache):
    if cache == []:
        return cache
    else:
        pivot = find_pivot(cache)
        p = cache[int(pivot)]
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
