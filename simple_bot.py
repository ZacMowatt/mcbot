import numpy as np
import cv2
import time
import pyautogui
from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
from pynput import mouse as mMouse
from time import sleep
import mouse as testMouse

keyboard = keyboardController()
mouse = mouseController()

deg90 = 606

run = True

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
    for x in range(0, int(deg90 / 6)):
        sleep(0.001)
        testMouse._os_mouse.move_relative(6, 0)

def on_move(x, y):
    pass
  #print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
  print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
  if button == Button.right:
      run = False
      print("Stopping")
  #if not pressed:
    # Stop listener
      #return False

def on_scroll(x, y, dx, dy):
    pass
  #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

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
  count = 1
  sleep(2)
  turnRight()

main()



