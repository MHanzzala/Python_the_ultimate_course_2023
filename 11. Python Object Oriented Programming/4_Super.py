class employee :
    
    def __init__(self, name, age):
        self._name= name
        self._age= age
    
    def accessMeetingRoom(self):
        print("accessMeetingRoom")
    
    def accessKitchen():
        print("accessKitchen")
    
    def accessPersonalOffice(self):
         print("accessPersonalOffice")


class advancedEmployee(employee):
    
    def __init__(self ,businessNumber, *args, **kwargs,  ):
        self._businessNumber= businessNumber
        super().__init__(*args, **kwargs)
        
        
    
    
    def accessPrivateMeetingRoom(self):
        print("accessPrivateMeetingRoom")


aEmployee = advancedEmployee(7891,"John",25, )
print(aEmployee._name)
print(aEmployee._businessNumber)
print(aEmployee._age)