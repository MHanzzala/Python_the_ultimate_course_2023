
db = {}


db.update({"names": ["Ali", "Muhammad"]})
db.update({"age": [27, 29]})

index = db["names"].index("Ali")

db = {}


db.update({"names": ["Ahmed", "Kamal"]})
db.update({"age": [27, 29]})

index = db["names"].index("Ahmed")


for value in db.values():
    for subvalue in value:
        print(subvalue)


# for key in db.keys():
#    del db[key][index]
