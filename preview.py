from PIL import Image
import reader

def generate_preview(img, preview_img, thresh_pixels, thresh_data):

    def display_preview(preview_img, thresh_pixels):
        for y in range(preview_img.size[1]):
            for x in range(preview_img.size[0]):
                preview_img.putpixel((x, y), thresh_pixels[y][x])
        preview_img.show()

    user_preview_choice = False
    while not user_preview_choice:
        display_preview(preview_img, thresh_pixels)
        choice = (input("Continue with this threshold map? Y/N: ")).lower()
        if choice == "y":
            user_preview_choice = True
            return thresh_pixels
        else:
            new_thresh_input = int(input("Enter a new threshold (0-255): "))
            thresh_pixels = reader.read_thresh(img, thresh_data, new_thresh_input)
