from machine import ADC
import math

class Joystick:
    def __init__(self, x=ADC(0), y=ADC(1), maxNum=20, giveNeg=False, maxX=65535, maxY=65535, minX=0, minY=0, revX=False, revY=False):
        self.x = x # The ADC pin for the x direction
        self.y = y # The ADC pin for the y direction
        self.maxNum = maxNum # The maximum number shown in either direction (when giveNeg=False). If maxNum=20 then values can range from 0-20 and middle would be 10
        self.giveNeg = giveNeg # If false, values range from 0-maxNum. If True, values range from -(maxNum/2) to (maxNum/2), rounded
        self.maxX = maxX # The maximum raw ADC value from x, used if x is lower than roughly 65535 when joystick is pushed to the maximum x position
        self.maxY = maxY # The maximum raw ADC value from y
        self.minX = 0 # The minimum raw ADC value from x, similar to maxX, but for all the way down
        self.minY = 0 # The minimum raw ADC value from y
        self.revX = revX # Reverse which way for x makes it go higher/lower, so it would be 0 instead of 20 and vice-versa (if maxNum=20)
        self.revY = revY # Same as revY, but for y
        self.savex = self.readX()
        self.savey = self.readY()
        
    def readX(self): # Reads x and returns a value based on __init__ data
        xval = int(round((self.x.read_u16())/(self.maxX-self.minX)*(self.maxNum),0))
        if self.revX:
            xval = self.maxNum-xval
        if self.giveNeg:
            xval -= math.floor(self.maxNum/2)
        return xval
    def readY(self): # Reads y and returns a value based on __init__ data
        yval = int(round((self.y.read_u16())/(self.maxY-self.minY)*(self.maxNum),0))
        if self.revY:
            yval = self.maxNum-yval
        if self.giveNeg:
            yval -= math.floor(self.maxNum/2)
        return yval
    def read(self): # Returns both x and y
        xval = self.readX()
        yval = self.readY()
        return (xval, yval)
    def save(self): # Saves the value of x and y to be looked at later (by getSaved())
        self.savex = self.readX()
        self.savey = self.readY()
    def getSaved(self): # Returns the values of x and y by save()
        return (self.savex, self.savey)
    def __str__(self): # Returns a str() of x and y when used as str(<Joystick_object>)
        return (str(self.readX()), str(self.readY()))
    
    