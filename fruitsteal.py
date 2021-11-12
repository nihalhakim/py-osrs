from RepeatedTimer import RepeatedTimer
import pyautogui
import random
import time
import sys
import keyboard

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

# look east and zoom all the way in

stall = Box("stall")
stall.set_loc((1000,186),(1082,261))

finv = Box("finv")
finv.set_loc((1258,570),(1262,574))

def stealer():
    time.sleep(1)
    pyautogui.moveTo(stall.get_coord()[0], stall.get_coord()[1], random.uniform(0.18,0.22))
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

    time.sleep(1)

    pyautogui.moveTo(finv.get_coord()[0], finv.get_coord()[1], random.uniform(0.1,0.2))
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


def click_all_inv():
    for j in range(7):
        for i in range (4):
            # temp = Box("temp")
            # temp.set_loc((1204+(40*i),554+(j*40)),((1204+(40*i)+40),554+(j*40)+40))
            # pyautogui.moveTo(temp.get_coord()[0], temp.get_coord()[1], random.uniform(0.1,0.2))
            pyautogui.moveTo(1220 + 40*i,560+ 40*j,random.uniform(0.02,0.3))
            pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


def check_full():
    global mn
    if pyautogui.locateOnScreen('inv_full.png', confidence=0.9):
        print("inv full stopping now")
        mn.stop()
        click_all_inv()
        mn = RepeatedTimer(1, stealer)
        mn.thread.start()


# mn = RepeatedTimer(1, stealer)
# cf = RepeatedTimer(1, check_full)
# mn.thread.start()
# cf.thread.start()

while True:
    stealer()