class motor:
    
    def __init__(self, startButton, stopButton, changeDir, changeSpeed):
        
        self._startButton = startButton
        self._stopButton = stopButton
        self._changeDir = changeDir
        self._changeSpeed = changeSpeed
    
    def turnON(self):
        if self._stopButton == 1:
            self._stopButton = 0
        self._startButton = True
        print("Motor Is On")
    
    def turnOFF(self):
        if self._startButton == 1:
            self._startButton = 0
        self._stopButton= True
        
        print("Motor Is Off")
    
    def changeSpeed(self, value):
        self._changeSpeed = value
        print("Speed Changed")
    
    #0 clockwise rotation , 1 anti-clockwise rotation
    def changeRotationDir(self , value):
        self._changeDir = value
        print("Dir Changed")



fan = motor(0,0,0,0)
print("startButton is :",fan._startButton)
fan.turnON()
print("startButton is :",fan._startButton)
fan.turnOFF()
print("stopButton is :", fan._stopButton)
print("startButton is :",fan._startButton)

fan.changeSpeed(50)
print(fan._changeSpeed)


fan.changeRotationDir(1)
print(fan._changeDir)


 
