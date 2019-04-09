from django.shortcuts import render

from pymongo import MongoClient

client = MongoClient()
db = client['art-data']
pictures = db.art_data_full

# Create your views here.
def home_view(request, *args, **kwargs):
    #print(request.POST)
    #results = db.art_data_full.find({"title": request.POST.get('q', False)}, {"fileName" : 1, "_id": 0})
    if request.POST.get('q'):
        #results = db.art_data_full.find( { request.POST.get('q') : { "$type" : 16 } }, { "fileName" : 1 , "genre" : 1, "style" : 1, "title" : 1, request.POST.get('q') : 1}).limit(10)
        #results = db.art_data_full.aggregate([{ "$match" : { request.POST.get('q') : 1 } } ])
        #temp = "colors." + request.POST.get('q')
        #results = db.art_data_full.find( { "colors": { "$elemMatch": { "color": request.POST.get('q')} } } , { "_id" : 0 , "fileName" : 1 , "genre" : 1, "style" : 1, "title" : 1, "colors.color" : 1, "colors.value": 1}).limit(10)
        results = db.art_data_full.aggregate(  [{ "$match" : { "colors.color" : request.POST.get('q') } }, {"$limit" : 20},  { "$project": {"_id" : 1, "fileName": 1, "artist" : 1, "date": 1, "genre": 1, "style": 1, "title" : 1, "colors": {"$filter": { "input": '$colors', "as": 'color', "cond": {"$eq": ['$$color.color', request.POST.get('q')]}}}   } }, { "$sort" : { "colors.value" : -1}}])
        #.sort([("colors.value", -1)])
        #results = db.art_data_full.aggregate([{ "$match" : { "colors": { "$elemMatch" : { "color": request.POST.get('q') } } } },{ "$project": {"fileName": 1,"genre": 1,"style": 1,"title": 1,"artist":1,"colors.value": 1,"colors.color":1,}	},{ "$limit": 10 }])
        #{ "$sort": { "colors.value": -1 } },
        return render(request, "colorsearch.html", {'results': results, 'q': request.POST.get('q')})
    else:
        results = {}
        return render(request, "colorsearch.html", {'results' : results, 'q': request.POST.get('q')})