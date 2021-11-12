from RepeatedTimer import RepeatedTimer
from Box import Box
import pyautogui
import random
import time
import sys

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


herb = Box("herb")
herb.set_loc((909,349),(923,364))

herb2 = Box("herb2")
herb2.set_loc((959,354),(971,361))

close = Box("close")
close.set_loc((1118,59),(1129,71))

banker = Box("banker")
banker.set_loc((931,378),(1067,433))

deposit = Box("deposit")
deposit.set_loc((1068,641),(1091,664))

# time.sleep(random.uniform(1.5,1.7))
while(True):
	pyautogui.moveTo(herb.get_coord()[0], herb.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	# pyautogui.moveTo(herb2.get_coord()[0], herb2.get_coord()[1], random.uniform(0.02,0.04))
	# pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(close.get_coord()[0], close.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


	# click all items in inventory
	for j in range(7):
		for i in range (4):
			# temp = Box("temp")
			# temp.set_loc((1204+(40*i),554+(j*40)),((1204+(40*i)+40),554+(j*40)+40))
			# pyautogui.moveTo(temp.get_coord()[0], temp.get_coord()[1], random.uniform(0.1,0.2))
			
			pyautogui.moveTo(1220 + 40*i,560+ 40*j,random.uniform(0.02,0.06))
			# pyautogui.moveTo(1220 + 40*i,560+ 40*j,random.uniform(0.001,0.01))

			pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(banker.get_coord()[0], banker.get_coord()[1], random.uniform(0.1,0.3))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(random.uniform(0.65,1.2))

	pyautogui.moveTo(deposit.get_coord()[0], deposit.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])




# click herb
# click X
# click clean x 28
# click banker
# click deposit all
# click click herb