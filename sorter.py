from PIL import Image
import random
import args

def quick_sort(pixels):
	if pixels == []:
		return pixels
	else:
		p = pixels[random.choice(range(0, len(pixels)))]
		if args.reverse:
			l = quick_sort([x for x in pixels[1:] if (x[0]+x[1]+x[2]) >= (p[0]+p[1]+p[2])])
			r = quick_sort([x for x in pixels[1:] if (x[0]+x[1]+x[2]) < (p[0]+p[1]+p[2])])
			return l + [p] + r
		else:
			l = quick_sort([x for x in pixels[1:] if (x[0]+x[1]+x[2]) < (p[0]+p[1]+p[2])])
			r = quick_sort([x for x in pixels[1:] if (x[0]+x[1]+x[2]) >= (p[0]+p[1]+p[2])])
			return l + [p] + r

def sort_pixels(pixels, thresh):
	white = (255, 255, 255)
	black = (0, 0, 0)
	sorted_pixels = []
	sort_cache = []

	def pixel_dump(sort_cache):
		dump = quick_sort(sort_cache)
		for c in dump:
			sorted_pixels.append(c)

	for (p, t) in zip(pixels, thresh):
		if t == white:
			sort_cache.append(p)
		elif t == black:
			if len(sort_cache) >= 1:
				pixel_dump(sort_cache)
				sorted_pixels.append(p)
			else:
				sorted_pixels.append(p)
			sort_cache = []
	if len(sort_cache) >= 1:
		pixel_dump(sort_cache)
	return sorted_pixels