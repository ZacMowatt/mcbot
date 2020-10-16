from time import sleep
from pynput.mouse import Button, Controller as mController
from pynput.keyboard import KeyCode, Listener, Controller as kbController
import threading
import pyautogui
import time
import cv2
import numpy as np
macOS = False
if not macOS:
    import mouse as mouse
    import keyboard

kbController = kbController()
mController = mController()

# horrisontal pixel offset for turning 90 deg
horr_offset = 605
horr_look_offset = 300
ver_look_offset = 200
look_speed = 10
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='p')
configure_key = KeyCode(char='/')
delay = .5
depth = 1  # int(input("Depth:"))
width = 1  # int(input("Width:"))
height = 0  # int(input("Height:"))


# breaking times for block types:
buffer_time = .25
andesite_time = .4
coal_time = .75
cobble_time = .5
diamond_time = .75
dorite_time = .4
dirt_time = .15
emerald_time = .75
gold_time = .75
gravel_time = .15
iron_time = .75
lapis_time = .75
sand_time = .15
sandstone_time = .2
stone_time = .4


class Bot(threading.Thread):

    blocks_mined = 0
    iron_pick_durability = 240
    pick_slot_index = 0
    pick_slot = ['1', '2', '3', '4', '5', '6']
    mode = -1
    sand_slot = '9'

    def __init__(self, delay, depth, width, height):
        super().__init__()
        print("init")
        self.delay = delay
        self.running = False
        self.program_running = True

        self.depth = depth
        self.width = width
        self.height = height
        self.lengths = int(width / 2)

    def start_bot(self):
        if self.mode == -1:
            self.configure_bot()
        self.countdown()
        self.running = True
        print("start working")

    def configure_bot(self):
        self.mode = int(input("MODE {1 = 1x2, 2 = 2x2}"))
        self.depth = int(input("Depth:"))

    def countdown(self):
        for x in range(4, 0, -1):
            print("{}".format(x))
            sleep(1)

    def dig():
        self.running = True

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
                # Need to find a more accurate movement method
                # to make the code reliable
                # for x in range(int(self.height / 2)):
                # if self.running:
                # for y in range(self.lengths):
                # if self.running:
                # for x in range(self.depth - 2):
                # if y != 0 & y + 1 != self.lengths:
                # x += 2
                # else:
                # self.mine_4()
                # self.walk_forward()
                # if y + 1 != self.lengths:
                # self.corner(y)
                ##
                # if x + 1 != int(height / 2):
                # self.mine_down()
                print("Bot depth: {}".format(self.depth))
                for x in range(self.depth):
                    if self.running:

                        if self.mode == 3:
                            for y in range(8):
                                self.look_right()
                                self.mine()
                        elif self.mode == 2:
                            self.look_right()
                            self.mine()
                            self.look_right()
                            self.mine()
                            self.look_left()
                            self.look_left()
                            self.mine()
                        elif self.mode == 0:
                            self.mine()

                        if self.mode > 0:
                            self.mine()
                            self.look_down()
                            self.mine()
                            self.look_up()

                self.place_sand()
                self.stop()

    def step(self):
        keyboard.press('w')
        sleep(.1)
        keyboard.release('w')

    def place_sand(self):
        keyboard.press_and_release(self.sand_slot)
        self.look_down()

        print("Depth: {}".format(self.depth))
        for x in range(0, self.depth):
            print("x: {}".format(x))
            keyboard.press('space')
            time.sleep(.2)
            keyboard.release('space')
            mouse.press(button='right')
            mouse.release(button='right')
            time.sleep(.3)

    def mine_4(self):
        self.look_left()
        self.mine()
        self.look_down()
        self.mine()
        self.look_up()
        self.look_right()
        self.look_right()
        self.mine()
        self.look_down()
        self.mine()
        self.look_up()
        self.look_left()

    def mine_corner(self):
        self.mine_4()
        self.walk_forward()
        self.mine_4()

    def corner(self, y):
        right = y % 2
        self.mine_corner()
        if right:
            self.turn_right()
        else:
            self.turn_left()
        self.step()
        self.step()
        self.mine_corner()
        self.step()
        if right:
            self.turn_right()
        else:
            self.turn_left()
        self.walk_forward()

    def mine_down(self):
        print("Mining down")

    def mine(self):
        if self.blocks_mined >= self.iron_pick_durability:
            self.pick_slot_index += 1
            if self.pick_slot_index < len(self.pick_slot):
                keyboard.press_and_release(
                    self.pick_slot[self.pick_slot_index])
            else:
                self.running = False
                print("No more picks")
            self.blocks_mined = 0
        mController.press(Button.left)
        sleep(diamond_time + buffer_time)
        mController.release(Button.left)

    def mine_straight(self):
        self.mine()
        self.mine()
        self.walkForward()

    def walkForward(self):  # walks an average of 0.99 blocks per call
        print("Walking")
        # kbController.press(KeyCode(char='w'))
        keyboard.press('w')
        sleep(.23)
        keyboard.release('w')
        # kbController.release(KeyCode(char='w'))

    def turn_left(self):
        remainder = horr_offset % look_speed
        step = int(horr_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mouse._os_mouse.move_relative(-step, 0)
        mouse._os_mouse.move_relative(-remainder, 0)

    def turn_right(self):
        remainder = horr_offset % look_speed
        step = int(horr_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mouse._os_mouse.move_relative(step, 0)
        mouse._os_mouse.move_relative(remainder, 0)

    def look_left(self):
        remainder = horr_look_offset % look_speed
        step = int(horr_look_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mouse._os_mouse.move_relative(-step, 0)
        mouse._os_mouse.move_relative(-remainder, 0)

    def look_right(self):
        remainder = horr_look_offset % look_speed
        step = int(horr_look_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mouse._os_mouse.move_relative(step, 0)
        mouse._os_mouse.move_relative(remainder, 0)

    def look_up(self):
        remainder = ver_look_offset % look_speed
        step = int(ver_look_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mouse._os_mouse.move_relative(0, -step)
        mouse._os_mouse.move_relative(0, -remainder)

    def look_down(self):
        remainder = ver_look_offset % look_speed
        step = int(ver_look_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mouse._os_mouse.move_relative(0, step)
        mouse._os_mouse.move_relative(0, remainder)

    def _lookRight():
        remainder = horr_offset % look_speed
        step = int(horr_offset / look_speed)
        for x in range(0, look_speed):
            sleep(0.001)
            mController.move(step, 0)
        mController.move(remainder, 0)


def main():

    print("Depth: {}".format(depth))

    if depth <= 0 | width <= 0:
        print("Bad Dimensions, bot not started")
    else:
        print("Starting bot")
        bot_thread.start()


bot_thread = Bot(delay, depth, width, height)


def _main():
    print("starting bot")
    bot_thread.start()


if macOS:
    _main()
else:
    main()


def on_press(key):
    if key == start_stop_key:
        if bot_thread.running:
            bot_thread.stop()
        else:
            bot_thread.start_bot()
    elif key == exit_key:
        bot_thread.exit()
        listener.stop()
    elif key == configure_key:
        bot_thread.configure_bot()
    elif key == KeyCode(char='j'):
        bot_thread.turn_left()
    elif key == KeyCode(char='k'):
        bot_thread.turn_right()
    elif key == KeyCode(char='m'):
        bot_thread.mine()
    elif key == KeyCode(char='o'):
        bot_thread.walk_forward()
    elif key == KeyCode(char='b'):
        bot_thread.look_left()


with Listener(on_press=on_press) as listener:
    listener.join()
