import pymongo

client = pymongo.MongoClient()

db = client['test_db']
collection = db['ex_2']

data = [
    {
        "data": 123,
        "pic": "text2"
    },
    {
        "data": 234,
        "pic": "text2"
    },
    {
        "data": 345,
        "pic": "text3"
    }
]


def count():
    print("\ncount:", collection.count_documents(filter={}))


def insert_one():
    res = collection.insert_one(document=data[0])
    print("\ninsert_one:", type(res))
    print("-acknowledged:", res.acknowledged)
    if res.acknowledged:
        print("-inserted_id:", res.inserted_id)


def insert_many():
    res = collection.insert_many(documents=data[1:])
    print("\ninsert_many:", type(res))
    print("-acknowledged:", res.acknowledged)
    if res.acknowledged:
        print("-inserted_id:", res.inserted_ids)


def find_one():
    res = collection.find_one(filter={"data": 130})
    print("\nfind_one:", res)


def find_all():
    print("\nfind_all:")

    for data in collection.find(filter={}, skip=1, limit=5):
        print('---', data)
    # for data in collection.find(filter={}):
    #     print('---', data)


def find_proj():
    print("\nfind_proj")
    for data in collection.find(filter={}, projection={"data": 1, "_id": 0}):
        print('---', data)


def update_one():
    res_1 = collection.update_one(
        filter={'data': 123},
        update={"$set": {'data': 222, "data2": 'check this'}},
        upsert=True
    )
    res_2 = collection.update_one(
        filter={'data': 234},
        update={"$unset": {"pic": ''}}
    )
    print("\nupdate_one:", type(res_1))
    print("-acknowledged:", res_1.acknowledged)
    print("-matched_count:", res_1.matched_count)
    print("-modified_count:", res_1.modified_count)
    print("-upserted_id:", res_1.upserted_id)
    print("-raw_result:", res_1.raw_result)
    # print(res_2)


def update_many():
    res = collection.update_many(filter={"data": {"$gt": 200}}, update={"$set": {"update": None}}, upsert=False)
    print("\nupdate_many:", type(res))
    print("-acknowledged:", res.acknowledged)
    print("-matched_count:", res.matched_count)
    print("-modified_count:", res.modified_count)
    print("-upserted_id:", res.upserted_id)
    print("-raw_result:", res.raw_result)


def replace_one():
    res = collection.replace_one(filter={}, replacement={})
    print("replace_one:", type(res))
    print("-acknowledged:", res.acknowledged)
    print("-matched_count:", res.matched_count)
    print("-modified_count:", res.modified_count)
    print("-upserted_id:", res.upserted_id)
    print("-raw_result:", res.raw_result)


def find_and():
    res = collection.find_one_and_update({
        "$and": [{"data": {"$lt": 500}}, {"pic": "text3"}]},
        {"$set": {"find_and_update": 0}}
    )
    print("\nfind_and:", res)


def delete_one():
    res = collection.delete_one(filter={'data': 345})
    print("\ndelete_one:", type(res))
    print("-acknowledged:", res.acknowledged)
    print("-deleted_count:", res.deleted_count)
    print("-raw_result:", res.raw_result)


def delete_many():
    res = collection.delete_many(filter={})
    print("\ndelete_many:", type(res))
    print("-acknowledged:", res.acknowledged)
    print("-deleted_count:", res.deleted_count)
    print("-raw_result:", res.raw_result)


def create_index():
    res = collection.create_index([('data', pymongo.ASCENDING)], unique=True, name="data_index")
    print("\ncreate_index:", type(res))
    print("-res:", res)
    # result = collection.create_index([('data', pymongo.DESCENDING)], unique=True)


def drop_index():
    res = collection.drop_index("data_index")
    print("\ndrop_index:", type(res))
    print("-res:", res)
    # result = collection.create_index([('data', pymongo.DESCENDING)], unique=True)


def show_indexes():
    for data in collection.list_indexes():
        print("-", data)


show_indexes()

delete_many()
insert_one()
insert_many()

count()

find_one()
find_all()
find_proj()
find_and()

update_one()
update_many()

create_index()
drop_index()
