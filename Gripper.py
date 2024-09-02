import math
from servo import Servo

class Gripper:
    maxDist = 90
    maxAngle = 90
    armLength = 45
    fingerLengthToPivot = 15
    
    def __init__(self):
        # Create our Servo object, assigning the
        # GPIO pin connected the PWM wire of the servo
        self.motor = Servo(pin_id=16)
        self.setToDistance(0)
    
    def jogOpen(self):
        angle = self.motor.read()
        if (angle < 1):
            return False
        angle = angle - 1
        self.motor.write(angle)
        return self.fingerDistance()
        
    def jogClose(self):
        angle = self.motor.read()
        if (angle > self.maxAngle - 1):
            return False
        angle = angle + 1
        self.motor.write(angle)
        return self.fingerDistance()
    
    def fingerDistance(self):
        angle = math.radians(self.motor.read())
        dist = (self.armLength * math.cos(angle)) * 2
        return round(dist, 2)
    
    def setToDistance(self, distance):
        if (distance < 0 or distance > self.maxDist):
            return False
        angle = math.acos((distance/2) / self.armLength)
        self.motor.write(math.degrees(angle))
        return True
        
    
gripper = Gripper()
