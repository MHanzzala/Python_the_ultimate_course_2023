
db = {} 
 

db.update({"names":["Babar","Hamid"]})
db.update({"age":[27,29]})

index= db["names"].index("Babar")

del db["names"][index]
del db["age"][index]

 
print(db)


db = {} 
 

db.update({"names":["Babar","Hamid"]})
db.update({"age":[27,29]})

index= db["names"].index("Babar")

del db["names"][index]
del db["age"][index]

 
print(db)

