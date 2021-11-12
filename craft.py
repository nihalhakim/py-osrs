from RepeatedTimer import RepeatedTimer
import pyautogui
import random
import time
import sys
import keyboard


# from bank, click smelt
# click bracelet on menu
# wait
# click bank
# click bracelets to deposit
# click gold bar, click ruby

#repeat above

# face north, camera UP all the way, zoom location saved on runelite (111)

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

smelt = Box("smelt")
smelt.set_loc((1285,347),(1288,354))

make = Box("make")
make.set_loc((846,468),(857,481))

bank = Box("bank")
bank.set_loc((696,590),(699,594))

bracelet = Box("bracelet")
bracelet.set_loc((1258,673),(1264,682))

bar = Box("bar")
bar.set_loc((1007,279),(1019,289))

ruby = Box("ruby")
ruby.set_loc((1055,279),(1065,291))

while(True):
	pyautogui.moveTo(smelt.get_coord()[0], smelt.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(5.5)

	pyautogui.moveTo(make.get_coord()[0], make.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(24)


	pyautogui.moveTo(bank.get_coord()[0], bank.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


	time.sleep(5.5)

	pyautogui.moveTo(bracelet.get_coord()[0], bracelet.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(0.6)

	pyautogui.moveTo(bar.get_coord()[0], bar.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(ruby.get_coord()[0], ruby.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
