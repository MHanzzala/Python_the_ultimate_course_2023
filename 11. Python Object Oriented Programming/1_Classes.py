class motor:
    
    def __init__(self):
        pass
    
    def turnON(self):
        print("Motor Is On")
    
    def turnOFF(self):
        print("Motor Is Off")
    
    def changeSpeed(self):
        print("Speed Changed")
    
    def changeDirections(self):
        print("Direction Changed")



fan = motor()
fan.turnOFF()

washingMachine = motor()
washingMachine.changeSpeed()

