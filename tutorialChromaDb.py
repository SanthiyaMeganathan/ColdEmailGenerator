import chromadb

client = chromadb.Client()
collection =client.create_collection(name="my_collection")

collection.add(
    documents=[
        'This  document is about newyork',
        'this document is about delhi'
    ],
    ids=['id1','id2']
)

all_docs = collection.get()
print(all_docs)

documents = collection.get(ids=["id1"])
print(documents)


results = collection.query(
    query_texts=['Query is about the  pizza'],
    n_results=2
)
print("......................................")
print(results)

print("?????")

collection.delete(ids=all_docs['ids'])
collection.get()

collection.add(
    documents=[
        "This document is about the newYork",
        "This document is about delhi"
    ],
    ids=["ids3","ids4"],
    metadatas=[
        {"source":"https://en.wikipedia.org/wiki/New_York_City"},
        {"source":"https://en.wikipedia.org/wiki/New_Delhi"}
    ]
)

results = collection.query(
    query_texts=["Query is about the chhole Bhature"],
    n_results=2
)
print("<<<<<<<<<")
print(results)


