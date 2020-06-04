from PIL import Image
import args
from statistics import median #to find median pivot

def find_pivot(cache):
    clen = int(len(cache))
    if clen >= 100:
        a, b, c = sum(cache[0]), sum(cache[int(clen/2)]), sum(cache[-1])
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
    else:
        return 0

def mode_index():
    if args.mode == 'H':
        return 0
    elif args.mode == 'S':
        return 1
    else:
        return 2

def quick_sort(cache, m):
    if cache == []:
        return cache
    else:
        p_index = find_pivot(cache)
        p = cache[int(p_index)]
        if args.reverse:
            l = quick_sort([x for x in cache[1:] if (x[m]) >= (p[m])], m)
            r = quick_sort([x for x in cache[1:] if (x[m]) < (p[m])], m)
            return l + [p] + r
        else:
            l = quick_sort([x for x in cache[1:] if (x[m]) < (p[m])], m)
            r = quick_sort([x for x in cache[1:] if (x[m]) >= (p[m])], m)
            return l + [p] + r


def sort_pixels(pixels, thresh):
    m = mode_index()
    sorted_pixels, sort_cache = [], []

    def pixel_dump(sort_cache):
        dump = quick_sort(sort_cache, m)
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
