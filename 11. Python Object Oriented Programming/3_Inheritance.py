# -*- coding: utf-8 -*-
"""
Spyder Editor
 
"""

class employee :
    
    def __init__(self):
        pass
    
    def accessMeetingRoom(self):
        print("accessMeetingRoom")
    
    def accessKitchen():
        print("accessKitchen")
    
    def accessPersonalOffice(self):
         print("accessPersonalOffice")


class advancedEmployee(employee):
    
    def accessPrivateMeetingRoom(self):
        print("accessPrivateMeetingRoom")


employee4 = advancedEmployee()

employee4.accessMeetingRoom()
employee4.accessPrivateMeetingRoom()