from RepeatedTimer import RepeatedTimer
from Box import Box
import pyautogui
import random
import time
import sys

# click bank
# deposit logs (click inv with bank set to All)
# click logs
# close bank

# click knife
# click log
# click 

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


close = Box("close")
close.set_loc((1118,59),(1129,71))


banker = Box("banker")
banker.set_loc((959,323),(1023,353))


logs = Box("logs")
logs.set_loc((1006,244),(1019,256))

knife = Box("knife")
knife.set_loc((1215,570),(1221,576))

finv = Box("finv")
finv.set_loc((1258,570),(1262,574))

mshort = Box("mshort")
mshort.set_loc((792,755),(807,774))

mlong = Box("mlong")
mlong.set_loc((885,747),(916,780))

SLEEP_TIME = 49

count = 0
while True:
	pyautogui.moveTo(banker.get_coord()[0], banker.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(finv.get_coord()[0], finv.get_coord()[1], random.uniform(0.6,0.8))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(logs.get_coord()[0], logs.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(close.get_coord()[0], close.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(knife.get_coord()[0], knife.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	pyautogui.moveTo(finv.get_coord()[0], finv.get_coord()[1], random.uniform(0.05,0.13))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(0.4)

	pyautogui.moveTo(mlong.get_coord()[0], mlong.get_coord()[1], random.uniform(0.2,0.3))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(SLEEP_TIME)

	count += 27
	print("Running Total: " + str(count) + " maple longbows, " + str(count*58) + " exp")
