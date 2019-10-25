macOS = True

import numpy as np
import cv2
import time
import pyautogui
import threading
from pynput.keyboard import KeyCode, Listener, Controller as kbController
from pynput.mouse import Button, Controller as mController
from time import sleep
#uncomment mouse inport on Windows 
if not macOS:
  import mouse as testMouse

kbController = kbController()
mController = mController()

#horrisontal pixel offset for turning 90 deg
horOffset = 606
lookSpeed = 100
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='e')
delay = .5
straight_mode = 1

class Bot(threading.Thread):
  def __init__(self, delay):
    super().__init__()
    print("init")
    self.delay = delay
    self.running = False
    self.program_running = True
    self.mode = 0

  def start_bot(self):
    self.running = True
    print("start")

  def stop(self):
    self.running = False
    print("Stop")

  def exit(self):
    print("Exit")
    self.stop()
    self.program_running = False

  def run(self):
    while self.program_running:
      while self.running:
        #print("running")
        switch self.mode
          case 0
            pass
            break
          case 1
            self.mine_straight()
        self.walkForward()
        sleep(self.delay)

  def mine(self):
    mController.press(Button.left)
    sleep(.6)
    mController.release(Button.left)
  
  def mine_straight(self):
    self.mine()
    self.mine()
    self.walkForward()
  
  def walkForward(self): #walks an average of 0.99 blocks per call
    print("Walking")
    kbController.press('w')
    sleep(.22)
    kbController.release('w')

  def turnLeft():
    remainder = horOffset % lookSpeed
    step = int(horOffset / lookSpeed)
    for x in range(0, lookSpeed):
      sleep(0.001)
      testMouse._os_mouse.move_relative(step, 0)
    testMouse._os_mouse.move_relative(remainder, 0)

  def lookRight():
    remainder = horOffset % lookSpeed
    step = int(horOffset / lookSpeed)
    for x in range(0, lookSpeed):
      sleep(0.001)
      testMouse._os_mouse.move_relative(step, 0)
    testMouse._os_mouse.move_relative(remainder, 0)

  def _lookRight():
    remainder = horOffset % lookSpeed
    step = int(horOffset / lookSpeed)
    for x in range(0, lookSpeed):
      sleep(0.001)
      mController.move(step, 0)
    mController.move(remainder, 0)

  def lookUp():
    mController.press('8')
    mController.release('8')

def main():
  count = 1
  sleep(2)
  lookRight()

bot_thread = Bot(delay)

def _main():
  print("starting bot")
  bot_thread.start()


if macOS:
  _main()
else:
  main()

def on_press(key):
  print(key)
  if key == start_stop_key:
    if bot_thread.running:
      bot_thread.stop()
    else:
      bot_thread.start_bot()
  elif key == exit_key:
    bot_thread.exit()
    listener.stop()

with Listener(on_press=on_press) as listener:
  listener.join()


