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

# to mine:
# scirpt uses threads to keep a running list of available
# rocks at any point in time
# randomly selects a rock to mine

rocks_available = []

north_rock = Box("north_rock")
south_rock = Box("south_rock")
west_rock = Box("west_rock")

north_rock.set_loc((978,330),(1032,380))
south_rock.set_loc((995,549),(1034,590))
west_rock.set_loc((873,436),(924,487))


def miner():
	while True:
		time.sleep(1.8)
		pyautogui.moveTo(north_rock.get_coord()[0], north_rock.get_coord()[1], random.uniform(0.2,0.4))
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

		time.sleep(1.8)

		pyautogui.moveTo(south_rock.get_coord()[0], south_rock.get_coord()[1], random.uniform(0.2,0.4))
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

		time.sleep(1.8)

		pyautogui.moveTo(west_rock.get_coord()[0], west_rock.get_coord()[1], random.uniform(0.2,0.4))
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
	if pyautogui.locateOnScreen('inv_full.png', confidence=0.9):
		print("inv full dropping now")
		click_all_inv()

def bot():
	mining = False
	while True:
		if keyboard.read_key() == "`":
			if mining:
				print("already mining")
			else:
				print("starting a mining loop now")
				mn = RepeatedTimer(4.8, miner)
				mn.thread.start()
				mining = True

		elif keyboard.read_key() == "1":
			print("trying to turn off miner")
			try:
				mn.stop()
			except:
				print("miner already off")
			mn = RepeatedTimer(4.8, miner)
			mining = False
	try:
		mn.stop()
	except:
		foo = 1
	return 0

bot()


