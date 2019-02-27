from PIL import Image
im = Image.open("0.jpg")
pix = list(im.getdata())

pd = {}
count = 1
temp = 0

for x in pix:
    rgb = str(x)
    rgb = rgb.replace(' ', '').replace('(', '').replace(')', '').replace(',', '')

    if(rgb not in pd):
        pd[rgb] = count
    else:
        temp = pd[rgb]
        temp += 1
        pd[rgb] = temp

print(pd)
