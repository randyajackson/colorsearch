from PIL import Image
im = Image.open("0.jpg")
pix = list(im.getdata())
print(pix)