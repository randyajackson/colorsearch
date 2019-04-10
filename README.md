# colorsearch

Color Search
____________

Components used:\
-Django\
-MongoDB\
-Python\
-HTML/CSS\
-Javascript\
-Pymongo\
-PIL\
-Pandas\
-iro.js - the color wheel [https://iro.js.org/]\
-screenfull.js - full screen functionality [ https://github.com/sindresorhus/screenfull.js/ ]\

Dataset comes from:
https://www.kaggle.com/c/painter-by-numbers/data

First project using MongoDB and Django framework

I tried to think of different ways to search for a picture.
If you had a room and you want a picture of a certain color, that is what this search is for.\

I learned a lot about Django and MongoDB from the project.\

Complications with Django:\
-Initial setup\
-Using template tags (ended up not having to use this)\
The template tags were used for getting RGB value from MongoDB and using that value as a key for obtaining other values within Django template.\

Complications with MongoDB:\
-Originally thought that MongoDB worked like a hashtable, it does not (at all).\
-Restructured the data multiple times for the RGB value and count\

First data structure attempt: {(0, 0, 0): 1 , (0, 1, 1): 2, fileName: 'test', ....}\
Bad return time, cannot use indexes.\

Second data structure attempt: {      {(0, 0, 0) : 1}, {(0, 1, 1): 2},...      }, fileName: 'test', ...}\
I thought this would work better as it is a key/value combination.\
Still did not return quickly and not able to index well.\

Third data strucure attempt: {     [ {color: '(0, 0, 0)', value: 1}, ... ], fileName: 'test', ...}\
Return times significantly dropped after this.\
Allows for better indexing.\

Another big problem was sorting by the number of occurences of the color in descending order.

I eventually sought help on Stack Overflow:
https://stackoverflow.com/questions/55389043/unable-to-project-sort-field-located-inside-array-of-multiple-3-element-dictiona

I learned a lot about agregate queries and this is the query inside of views.py:

results = db.art_data_full.aggregate(  [{ "$match" : { "colors.color" : request.POST.get('q') } }, {"$limit" : 20},  { "$project": {"_id" : 1, "fileName": 1, "artist" : 1, "date": 1, "genre": 1, "style": 1, "title" : 1, "colors": {"$filter": { "input": '$colors', "as": 'color', "cond": {"$eq": ['$$color.color', request.POST.get('q')]}}}   } }, { "$sort" : { "colors.value" : -1}}])

The $filter command was key to the faster return times with pictures in ascending order based on number of occurences.

All in all, good learning experience and hope you enjoy it!



