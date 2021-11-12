import pyautogui
import random
import time
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


alch = Box("alch")
ALCH_TL = (1355,649)
ALCH_BR = (1366,660)
alch.set_loc(ALCH_TL,ALCH_BR)

item = Box("item")
item.set_loc((1337,633),(1351,649))

tele = Box("tele")
tele.set_loc((1333,628),(1338,634))


# totally working driver, 714 per hour = 86k exp per hour

# count = 0
# while(True):
# 	pyautogui.moveTo(alch.get_coord()[0], alch.get_coord()[1], duration = 1)
# 	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

# 	time.sleep(random.uniform(0.8,1.4))

# 	pyautogui.moveTo(item.get_coord()[0], item.get_coord()[1], duration = random.uniform(0.2,0.5))
# 	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

# 	time.sleep(random.uniform(0.6,0.9))
# 	pyautogui.moveTo(tele.get_coord()[0], tele.get_coord()[1], duration = random.uniform(0.2,0.5))
# 	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
# 	count += 1
# 	print("tele-alch count = " + str(count))

count = 0
while(True):
	pyautogui.moveTo(alch.get_coord()[0], alch.get_coord()[1], random.uniform(0.2,0.5))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(random.uniform(1.5,1.7))

	pyautogui.moveTo(item.get_coord()[0], item.get_coord()[1], duration = random.uniform(0.15,0.3))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(random.uniform(0.3,0.4))
	pyautogui.moveTo(tele.get_coord()[0], tele.get_coord()[1], duration = random.uniform(0.2,0.3))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
	count += 1
	print("tele-alch count = " + str(count))
