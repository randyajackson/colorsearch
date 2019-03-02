from PIL import Image
import pandas as pd
import numpy as np

Image.MAX_IMAGE_PIXELS = None

data = pd.read_csv("data_condensed.csv")

im = Image.open("img/" + data['new_filename'][0], 'r')

entry = {}

initial = 1
id = 0

for x in iter(im.getdata()):
    if(x not in entry):
        entry[x] = initial
    else:
        temp = entry[x]
        temp += 1
        entry[x] = temp

print(entry)
print(data['genre'][0])
print(data['style'][0])
print(data['title'][0])
print("img/" + data['new_filename'][0])