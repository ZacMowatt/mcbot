import numpy as np
import cv2
import time
import pyautogui
from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
from pynput import mouse as mMouse
from time import sleep

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
  keyboard.press('u')
  sleep(2)
  keyboard.release('u')

def turnRight():
  mouse.move(30, 0)

def on_move(x, y):
  print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
  print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
  #if not pressed:
    # Stop listener
      #return False

def on_scroll(x, y, dx, dy):
  print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

def lookUp():
  keyboard.press('8')
  sleep(3)
  keyboard.release('8')

# Collect events until released
#with mMouse.Listener(
#  on_move=on_move,
#  on_click=on_click,
#  on_scroll=on_scroll) as listener:listener.join()

def main():
  sleep(2)
  lookUp()
  turnLeft()

main()


