import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
print(client)

db = client['test_db']
print(db)

db.create_collection('create_coll')
print(db.list_collection_names())
db.drop_collection('create_coll')

client.drop_database('test_db')
client.close()
