#Function & global variables

db1=["Ali", "Hamza", "Bilal"]
db2=["Sahid", "Babar"]
db3=["Shaheen", "Rizwan"]



def addToDatabase(name): 
   
    global db1
    global db2
    global db3
    
    db1=[name]
    db2=[name]
    db3=[name]
    

addToDatabase("Hanzala")
addToDatabase("Zain")
print("Db 1 is: ", db1)
print("Db 2 is: ", db2)
print("Db 3 is: ", db3)