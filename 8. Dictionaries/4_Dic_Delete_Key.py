
db = {}


db["names"] = "Hanzala"
db["age"] = 29

db.update({"names": ["Muhammad", "Hanzala"]})
db.update({"age": [27, 29]})

db["names"].append("Zain")
db["age"].append(23)
if "names" in db:

    db = {}

    db["names"] = "Hanzala"
    db["age"] = 29

    db.update({"names": ["Muhammad", "Hanzala"]})
    db.update({"age": [27, 29]})

    db["names"].append("Zain")
    db["age"].append(23)
    if "names" in db:
        del db["names"]

    print(db)
