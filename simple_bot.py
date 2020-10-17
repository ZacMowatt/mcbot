macOS = True

import numpy as np
import cv2
import time
import pyautogui
import threading
from pynput.keyboard import KeyCode, Listener, Controller as kb_controller
from pynput.mouse import Button, Controller as m_controller
from time import sleep
#uncomment mouse inport on Windows 
if not macOS:
  import mouse as test_mouse

kb_controller = kb_controller()
m_controller = m_controller()

#horrisontal pixel offset for turning 90 deg
hor_offset = 606
look_speed = 100
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
        self.walk_forward()
        sleep(self.delay)

  def mine(self):
    m_controller.press(Button.left)
    sleep(.6)
    m_controller.release(Button.left)
  
  def mine_straight(self):
    self.mine()
    self.mine()
    self.walk_forward()
  
  def walk_forward(self): #walks an average of 0.99 blocks per call
    print("Walking")
    kb_controller.press('w')
    sleep(.22)
    kb_controller.release('w')

  def turn_left(self):
    remainder = hor_offset % look_speed
    step = int(hor_offset / look_speed)
    for x in range(0, look_speed):
      sleep(0.001)
      test_mouse._os_mouse.move_relative(step, 0)
    test_mouse._os_mouse.move_relative(remainder, 0)

  def look_right(self):
    remainder = hor_offset % look_speed
    step = int(hor_offset / look_speed)
    for x in range(0, look_speed):
      sleep(0.001)
      test_mouse._os_mouse.move_relative(step, 0)
    test_mouse._os_mouse.move_relative(remainder, 0)

  def _look_right(self):
    remainder = hor_offset % look_speed
    step = int(hor_offset / look_speed)
    for x in range(0, look_speed):
      sleep(0.001)
      m_controller.move(step, 0)
    m_controller.move(remainder, 0)

  def look_up(self):
    m_controller.press('8')
    m_controller.release('8')

def main():
  count = 1
  sleep(2)
  look_right()

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


