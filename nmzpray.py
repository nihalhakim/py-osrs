from RepeatedTimer import RepeatedTimer
from Box import Box
import pyautogui
import random
import time
import sys

# move mouse to prayer icon
# start double tapping in time
# every few seconds, check for prot melee icon. If not found give on extra click else continue


# define functions to repeat
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

def logout():
	pyautogui.moveTo(logout1.get_coord()[0], logout1.get_coord()[1], random.uniform(0.4,0.8))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
	time.sleep(0.4)
	pyautogui.moveTo(logout2.get_coord()[0], logout2.get_coord()[1], random.uniform(0.2,0.4))
	pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
	print("Successfully logged out @ "  + str(time.asctime()))
	cl.stop()
	sys.exit()

def checklogout():
	try:
		in_nmz = pyautogui.locateOnScreen('points.png', confidence=0.9)
		if not in_nmz:
			print("CHAR OUTSIDE INSTANCE @ " + str(time.asctime()))
			dt.stop()
			cm.stop()
			print("logging out @ " + str(time.asctime()))
			logout()
		elif in_nmz:
			print("Char still in instance")
		else:
			print("Did pyautogui detect the points image?")
			
	except:
		pass

# Declare globals
pray = Box("pray")

pray.set_loc((1226,136),(1238,151))

# If you have the xp/hr open, use this one
# pray.set_loc((986,139),(995,146))




dt = RepeatedTimer(0.6, doubletap)
cm = RepeatedTimer(3, checkmelee)

cl = RepeatedTimer(12, checklogout)

logout1 = Box("logout1")
logout1.set_loc((1275,815),(1291,835))
logout2 = Box("logout2")
logout2.set_loc((1244,771),(1322,780))


# Driver
pyautogui.moveTo(pray.get_coord()[0], pray.get_coord()[1], random.uniform(0.01,0.02))
dt.thread.start()
cm.thread.start()
cl.thread.start()
