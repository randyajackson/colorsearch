from PIL import Image
import pandas as pd
import numpy as np
from pymongo import MongoClient

client = MongoClient()
db = client['art-data']
pictures = db.art_full_info

print(pictures)

Image.MAX_IMAGE_PIXELS = None

data = pd.read_csv("data_condensed.csv")

for z in range(10):
    im = Image.open("img/" + data['new_filename'][z], 'r')
    print("in " + str(z))
    fullDict = {}

    initial = 1
    id = 0

    for x in iter(im.getdata()):
        if(str(x) not in fullDict):
            fullDict[str(x)] = initial
        else:
            temp = fullDict[str(x)]
            temp += 1
            fullDict[str(x)] = temp

    fullDict['genre'] = data['genre'][z]
    fullDict['style'] = data['style'][z]
    fullDict['title'] = data['title'][z]
    fullDict['fileName'] ="img/" + data['new_filename'][z]
    result = pictures.insert_one(fullDict)
    print(result)
