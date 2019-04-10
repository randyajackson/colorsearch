from pymongo import MongoClient
from os import listdir, remove

client = MongoClient()
db = client['art-data']
pictures = db.art_data_full

results = db.art_data_full.find( {}, {"fileName" : 1, "_id": 0})

inDB = []
allFiles = []

for x in results:
    inDB.append(x['fileName'].replace('colorsearch/img/', ''))

for f in listdir('/var/www/randyjackson.net/public_html/colorsearch/img/'):
    allFiles.append(f)

for x in allFiles:
    if x not in inDB:
        remove(x)