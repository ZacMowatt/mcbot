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

    def startScript(self):
        self.running = True

    def stopScript(self):
        self.running = False
        print("Total distance = {}".format(self.totalSteps * self.step))

    def run(self):
        while True:
            while self.running:
                mouse._os_mouse.move_relative(self.step, 0)
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

with MouseListener(on_click=on_click, on_move=on_move) as listener:
    listener.join()
