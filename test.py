from PIL import Image

img = Image.open('./images/sakura.jpg').convert('RGB')
pal = img.histogram()
print(pal)
