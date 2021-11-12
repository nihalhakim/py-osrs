import pyautogui
import random
import time
from threading import Timer
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

def doubletap():
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

pray = Box("pray")
pray.set_loc((1226,136),(1238,151))

pyautogui.moveTo(pray.get_coord()[0], pray.get_coord()[1], random.uniform(0.01,0.02))


Timer(0.6,doubletap).start()



# d = 0
# while(True):
# 	st = time.time()
# 	time.sleep(0.37 - d)
# 	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
# 	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
# 	et = time.time() - st
# 	d = et - 0.6
# 	print("et:",et,"  ","dt: ", d)

