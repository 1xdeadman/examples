from pymongo import MongoClient, WriteConcern, ReadPreference
from pymongo.read_concern import  ReadConcern


client = MongoClient()
wc_majority = WriteConcern("majority", wtimeout=1000)

client.get_database(
    "mydb1", write_concern=wc_majority).foo.insert_one({'abc': 0})
client.get_database(
    "mydb2", write_concern=wc_majority).bar.insert_one({'xyz': 0})


def callback(session):
    collection_one = session.client.mydb1.foo
    collection_two = session.client.mydb2.bar

    # Important:: You must pass the session to the operations.
    collection_one.insert_one({'abc': 1}, session=session)
    collection_two.insert_one({'xyz': 999}, session=session)


with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or abort on error).
    session.with_transaction(
        callback, read_concern=ReadConcern('local'),
        write_concern=wc_majority,
        read_preference=ReadPreference.PRIMARY)

'''
ReadPreference:
primary
primaryPreferred
secondary
secondaryPreferred
nearest
'''
'''
read concern:
local
majority
snapshot

'''