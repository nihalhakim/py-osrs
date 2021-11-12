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

north_rock.set_loc((992,362),(1024,396))
south_rock.set_loc((997,576),(1025,604))
west_rock.set_loc((872,465),(908,498))


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

def pick_rock(some_rock, other_rock):
    global last_rock
    global laster_rock
    rocks = [north_rock, south_rock, west_rock]
    # print("last rock when called is: " + last_rock.name)
    # print("laster rock when called is: " + laster_rock.name)
    rocks.remove(last_rock)
    rocks.remove(laster_rock)
    rock = random.choice(rocks)
    # print("rock picked is: " + rock.name)
    laster_rock = last_rock
    last_rock = rock
    # print("new last rock is: " + last_rock.name)
    # print("new laster rock is: " + laster_rock.name)
    print()
    return rock

def miner2():
    rock = pick_rock(last_rock, laster_rock)
    pyautogui.moveTo(rock.get_coord()[0], rock.get_coord()[1], random.uniform(0.1,0.2))
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    # pyautogui.moveTo(1220,560,random.uniform(0.18,0.2))
    # pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    # pyautogui.moveTo(rock.get_coord()[0], rock.get_coord()[1], random.uniform(0.18,0.2))
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

def click_all_inv():
    for j in range(7):
        for i in range (4):
            # temp = Box("temp")
            # temp.set_loc((1204+(40*i),554+(j*40)),((1204+(40*i)+40),554+(j*40)+40))
            # pyautogui.moveTo(temp.get_coord()[0], temp.get_coord()[1], random.uniform(0.1,0.2))
            pyautogui.moveTo(1220 + 40*i,560+ 40*j,random.uniform(0.04,0.15))
            pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


def check_full():
    global mn
    if pyautogui.locateOnScreen('inv_full.png', confidence=0.9):
        print("inv full stopping now")
        mn.stop()
        click_all_inv()
        mn = RepeatedTimer(2, miner2)
        mn.thread.start()

last_rock = west_rock
laster_rock = south_rock

# for i in range(5):
#     time.sleep(1.8)
#     miner2()
#     check_full()

# for i in range(10):
#     print(miner2())


mn = RepeatedTimer(2, miner2)
cf = RepeatedTimer(1, check_full)
mn.thread.start()
cf.thread.start()


