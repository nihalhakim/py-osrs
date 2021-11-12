
import keyboard
from Box import Box
import pyautogui
import random
from RepeatedTimer import RepeatedTimer
import time
import sys

last_item = Box("last_item")
last_item.set_loc((1339,780),(1351,793))

quantity = Box("quantity")
quantity.set_loc((936,756),(988,786))

vent = Box('vent')
vent.set_loc((1026,331),(1051,349))

bank = Box("bank")
bank.set_loc((1151,447),(1197,479))

deposit = Box("deposit")
deposit.set_loc((1077,650),(1086,660))

karambwan = Box("karambwan")
karambwan.set_loc((912,209),(922,222))

close = Box("close")
close.set_loc((1119,57),(1125,69))


# click bank
# deposit all
# click karambwan
# click close
# click last item then vent then quantity, 28 times



while(True):

	pyautogui.moveTo(bank.get_coord()[0], bank.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(random.uniform(0.5,0.8))

	pyautogui.moveTo(deposit.get_coord()[0], deposit.get_coord()[1], random.uniform(0.1,0.2))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(0.2)

	pyautogui.moveTo(karambwan.get_coord()[0], karambwan.get_coord()[1], random.uniform(0.1,0.3))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(0.2)

	pyautogui.moveTo(close.get_coord()[0], close.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

	time.sleep(0.2)

	for i in range(50):
		if keyboard.is_pressed('q'):
			print("exiting script")
			sys.exit()

		pyautogui.moveTo(last_item.get_coord()[0], last_item.get_coord()[1], random.uniform(0.05,0.1))
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

		pyautogui.moveTo(vent.get_coord()[0], vent.get_coord()[1], random.uniform(0.05,0.1))
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

		


		# pyautogui.moveTo(quantity.get_coord()[0], quantity.get_coord()[1], random.uniform(0.2,0.4))
		# pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


