

import keyboard
from Box import Box
import pyautogui
import random
from RepeatedTimer import RepeatedTimer
import time

pray = Box("pray")
pray.set_loc((1226,136),(1238,151))


def doubletap():
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(0.02)
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

def checkmelee():
	try:
		melee_icon = pyautogui.locateOnScreen('image0.png', confidence=0.9)
		if melee_icon:
			print("Image found @ " + str(time.asctime()))
		else:
			pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
			print("***** Extra click given @ " + str(time.asctime()))
	except ImageNotFoundException:
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
		print("Extra click given due to ImageNotFoundException")

def checkmage():
	try:
		mage_icon = pyautogui.locateOnScreen('image1.png', confidence=0.9)
		if mage_icon:
			print("Image found @ " + str(time.asctime()))
		else:
			pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
			print("***** Extra click given @ " + str(time.asctime()))
	except ImageNotFoundException:
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
		print("Extra click given due to ImageNotFoundException")

def checkrange():
	try:
		range_icon = pyautogui.locateOnScreen('image2.png', confidence=0.9)
		if range_icon:
			print("Image found @ " + str(time.asctime()))
		else:
			pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
			print("***** Extra click given @ " + str(time.asctime()))
	except ImageNotFoundException:
		pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
		print("Extra click given due to ImageNotFoundException")


def tick_pray():
	on = False
	# t_end = time.time() + 10
	# while time.time() < t_end:
	while True:
		if keyboard.read_key() == "`":
			if on:
				print("already on")
			else:
				print("tick pray hotkey detected - turning ON")
				dt = RepeatedTimer(0.6, doubletap)
				cm = RepeatedTimer(1.8, checkmelee)
				# cm = RepeatedTimer(1.8, checkmage)
				# cm = RepeatedTimer(1.8, checkrange)
				pyautogui.moveTo(pray.get_coord()[0], pray.get_coord()[1], random.uniform(0.005,0.01))
				dt.thread.start()
				cm.thread.start()
				on = True
		elif keyboard.read_key() == "q":
			print("tick pray hotkey detected - turning OFF")
			try:
				dt.stop()
				cm.stop()
			except:
				print("off")
			dt = RepeatedTimer(0.6, doubletap)
			cm = RepeatedTimer(1.8, checkmelee)
			# cm = RepeatedTimer(1.8, checkmage)
			# cm = RepeatedTimer(1.8, checkrange)
			on = False
	try:
		dt.stop()
		cm.stop()
	except:
		foo = 1
	print("test time limit")
	return 0

tick_pray()