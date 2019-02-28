import numpy as np
import cv2
import time
from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController

keyboard = keyboardController()
mouse = mouseController()

def mine():
    mouse.press(Button.left)
    time.sleep(.6)
    mouse.release(Button.left)

def walkForward():
    keyboard.press('w')
    time.sleep(.3)
    keyboard.release('w')

def turnLeft():
    mouse.move(-30, 0)

def turnRight():
    mouse.move(30, 0)

time.sleep(3)
mine()
mine()
walkForward()
turnLeft()
turnRight()
mine()
mine()
walkForward()
