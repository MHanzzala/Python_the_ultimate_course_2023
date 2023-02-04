
db = {}


db.update({"names": ["Kamal", "Mudassar"]})
db.update({"age": [27, 29]})

index = db["names"].index("Kamal")


for value in db.values():
    for subvalue in value:

        db = {}

db.update({"names": ["Kamal", "Mudassar"]})
db.update({"age": [27, 29]})

index = db["names"].index("Kamal")


for value in db.values():
    for subvalue in value:
        print(subvalue)


# for key in db.keys():
#    del db[key][index]
