from pynput.mouse import Button, Listener as MouseListener, Controller as mController
import pyautogui
import threading
import mouse as mouse
import keyboard
from time import sleep

firstPos = (0, 0)
secondPos = (0, 0)
first = True
active = False

moveListener = False


class Bot(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = False
        self.step = 1
        self.totalSteps = 0
        self.totalDistance = 0

        self.setup()

    def startScript(self):
        self.running = True

    def setup(self):
        self.needInput = True
        while(self.needInput):
            try:
                mode = int(input("Mode: Horizontal(1) Vertical(2) >>"))
                if(mode == 1 or mode == 2):
                    self.mode = mode
                    self.needInput = False
            except:
                print("Please enter a number")

        self.needInput = True
        while(self.needInput):
            try:
                self.step = int(input("Step Value >>"))
                self.needInput = False
            except:
                print("Please enter a number")

    def stopScript(self):
        self.running = False
        print("Total distance = {}".format(self.totalSteps * self.step))
        self.setup()

    def run(self):
        while True:
            while self.running:
                mouse._os_mouse.move_relative(
                    self.step if self.mode == 1 else 0, 0 if self.mode == 1 else self.step)
                self.totalSteps = self.totalSteps + 1
                sleep(0.001)


script = Bot()


def on_click(x, y, button, pressed):
    global active, first, firstPos, secondPos

    if pressed and button == Button.right:
        if not active:
            print("Activating")
            active = True
            first = True
            firstPos = (0, 0)
            script.startScript()
        else:
            print("Deactivating")
            active = False
            script.stopScript()


def on_move(x, y):
    if moveListener:
        global first, active, firstPos, secondPos
        print("x:{0} y:{1}".format(x, y))

        if active:
            if first:
                firstPos = (x, y)
            else:
                secondPos = (x, y)


script.start()

with MouseListener(on_click=on_click) as listener:
    listener.join()
