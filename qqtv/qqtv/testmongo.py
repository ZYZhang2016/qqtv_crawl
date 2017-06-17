import pymongo

connection = pymongo.MongoClient()
testdb = connection.qqtv_yayaya
post_info = testdb.qq

name = {'name':'zzy','age':25,'skill':'Python'}
god = {'name':'cwy','age':'','skill':'ceshi'}
godness = {'name':'Mongo','age':'123456','other':'haochi'}

post_info.insert(name)
#post_info.insert(god)
#post_info.insert(godness)
