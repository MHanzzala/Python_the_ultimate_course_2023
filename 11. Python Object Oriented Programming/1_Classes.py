# -*- coding: utf-8 -*-
"""
Spyder Editor
 
"""

class motor:
    
    def __init__(self):
        pass
    
    def turnON(self):
        print("Motor Is On")
    
    def turnOFF(self):
        print("Motor Is Off")
    
    def changeSpeed(self):
        print("Speed Changed")
    
    def changeRotationDir(self):
        print("Dir Changed")



fan = motor()

fan.turnON()

washingMachine = motor()
washingMachine.changeSpeed()
