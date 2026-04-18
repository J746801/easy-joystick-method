import joystick
from time import sleep

j = joystick.Joystick(maxNum=20, giveNeg=True, maxX=53400, maxY=53400, revY=True)

while True:
    print(j.read())
    sleep(0.05)