from PIL import Image
import args, load, reader, direction, sorter, save

def main():
	print("Importing..")
	user_threshold, img, thresh_img, data, thresh_data, output = load.load_image()

	print("Reading Pixels..")
	img, data, thresh_img, thresh_data = direction.get_direction(img, data, thresh_img, thresh_data)
	pixels, thresh_pixels = reader.read(img, data, thresh_data, user_threshold)

	print("Sorting Pixels..")
	sorted_pixels = [sorter.sort_pixels(pixels[y], thresh_pixels[y]) for y in range(img.size[1])]

	print("Outputting Pixels..")
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			if args.direction == 'h':
				output.putpixel((x, y), sorted_pixels[y][x])
			elif args.direction == 'v':
				output.putpixel((y, x), sorted_pixels[y][x])

	print("Saving Image..")
	save.save(output)

if __name__ == "__main__":
	main()
