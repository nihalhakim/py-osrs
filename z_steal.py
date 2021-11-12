# from RepeatedTimer import RepeatedTimer
from Box import Box
import pyautogui
import random
import time
import sys

# 'C:\Users\NIHAL\AppData\Local\Programs\Python\Python38-32'

# print(pyautogui.size())

# pyautogui.moveTo(100, 100, duration = 1)


class Box:
    def __init__(self,name,tl=0,tr=0,bl=0,br=0):
        self.name = name
    
    def set_loc(self,tl,br):
        self.tl = tl
        self.br = br
        self.tr = (tl[1], br[0])
        self.bl = (tl[0], br[1])

    def get_coord(self):
        x = random.uniform(self.bl[0], self.br[0])
        y = random.uniform(self.bl[1], self.tl[1])
        return (x,y)


pouch = Box("pouch")
pouch.set_loc((2329,251),(2342,261))

stall = Box("stall")
stall.set_loc((2187,190),(2204,212))

# time.sleep(random.uniform(1.5,1.7))
while(True):
    
    for i in range(40):
        pyautogui.moveTo(stall.get_coord()[0], stall.get_coord()[1], random.uniform(0.1,0.2))
        pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
        time.sleep(2.4)

    pyautogui.moveTo(pouch.get_coord()[0], pouch.get_coord()[1], random.uniform(0.1,0.2))
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

