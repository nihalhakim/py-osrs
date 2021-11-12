import time
import pyautogui
import random
from threading import Event, Thread

class RepeatedTimer:

    """Repeat `function` every `interval` seconds."""

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()
        self.event = Event()
        self.thread = Thread(target=self._target)

    # def start(self):
    #     self.thread.start()

    def _target(self):
        while not self.event.wait(self._time):
            self.function(*self.args, **self.kwargs)

    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def stop(self):
        self.event.set()
        self.thread.join()

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

# define function to repeat
def doubletap():
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(0.02)
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])

def quadtap():
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(0.006)
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(0.006)
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(0.006)
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(0.006)

def slowdoubletap():
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
    time.sleep(1.8)
    pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])


pray = Box("pray")
pray.set_loc((1226,136),(1238,151))

# rapidheal = Box("rapidheal")
# rapidheal.set_loc((1349,601),(1361,617))

# pyautogui.moveTo(pray.get_coord()[0], pray.get_coord()[1], random.uniform(0.01,0.02))

# pyautogui.moveTo(rapidheal.get_coord()[0], rapidheal.get_coord()[1], random.uniform(0.01,0.02))

# start timer
dt = RepeatedTimer(0.6, doubletap)
qt = RepeatedTimer(0.6, quadtap)


# pyautogui.moveTo(pray.get_coord()[0], pray.get_coord()[1], random.uniform(0.01,0.02))
# pyautogui.click(pyautogui.position()[0], pyautogui.position()[1])
# time.sleep(1.2)

# while(True):
#     qt.thread.start()

#     time.sleep(12)

#     qt.stop()

#     time.sleep(1.2)

#     qt = RepeatedTimer(0.6, quadtap)

dt.thread.start()



# stop timer
# timer.stop()