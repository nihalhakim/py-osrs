from RepeatedTimer import RepeatedTimer
import pyautogui
import random
import time
import sys


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


def check_nr():
	try:
		# print("trying to detect north rock")
		north_avl = pyautogui.locateOnScreen('northrock.png', confidence=0.9)
		if north_avl and (north_rock not in rocks_available):
			# print(north_rock.name + " is available")
			rocks_available.append(north_rock)
		else:
			pass
			# rocks_available.remove(north_rock.name)
	except:
		print("something isnt right with north rock detection")

def check_sr():
	try:
		# print("trying to detect south rock")
		south_avl = pyautogui.locateOnScreen('southrock.png', confidence=0.9)
		if south_avl and (south_rock not in rocks_available):
			# print(south_rock.name + " is available")
			rocks_available.append(south_rock)
		else:
			pass
			# rocks_available.remove(south_rock.name)
	except:
		print("something isnt right with south rock detection")

def check_wr():
	try:
		# print("trying to detect west rock")
		west_avl = pyautogui.locateOnScreen('westrock2.png', confidence=0.9)
		if west_avl and (west_rock not in rocks_available):
			# print(west_rock.name + " is available")
			rocks_available.append(west_rock)
		else:
			pass
			# rocks_available.remove(south_rock.name)
	except:
		print("something isnt right with west rock detection")

def list_all_rocks():
	print(rocks_available)

def mine():
	rock = random.choice(rocks_available)
	pyautogui.moveTo(rock.get_coord()[0], rock.get_coord()[1], random.uniform(0.4,0.8))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
	rocks_available.remove(rock)


def click_all_inv():
	for j in range(7):
		for i in range (4):
			# temp = Box("temp")
			# temp.set_loc((1204+(40*i),554+(j*40)),((1204+(40*i)+40),554+(j*40)+40))
			# pyautogui.moveTo(temp.get_coord()[0], temp.get_coord()[1], random.uniform(0.1,0.2))
			pyautogui.moveTo(1220 + 40*i,560+ 40*j,random.uniform(0.02,0.3))
			pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


cnr = RepeatedTimer(0.4, check_nr)
csr = RepeatedTimer(0.5, check_sr)
cwr = RepeatedTimer(0.6, check_wr)
# lrocks = RepeatedTimer(1.2, list_all_rocks)
mn = RepeatedTimer(2, mine)

cnr.thread.start()
csr.thread.start()
cwr.thread.start()
# lrocks.thread.start()
mn.thread.start()
