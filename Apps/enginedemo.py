"""
Hello! This is a demo for the game engine.
Look around the code to understand how you can use the game engine for things.
"""

# Import the game engine.
import api
# We're gonna use choice() to randomly select a color from a
# list of them.
from random import choice
# We're also going to use Thread() to make a thread that counts
# the FPS or Frames Per Second of the program.
from threading import Thread


# Since making a whole block object is sorta inefficient, we're
# going to use placeholders.
# The api.display() function really only needs a color value to
# work.
# api.display()'s world argument:
# [
    # [Air, Air, Air, Air],
    # [Air, Air, Air, Plr],
    # [Air, Air, Air, Grs],
    # [Air, Air, Drt, Drt]
# ]
class placeHolder():
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color


# Make some variables.

# The colors list. This has three decoy blocks, red, green and
# blue.
colors = [placeHolder("#FF0000"), placeHolder("#00FF00"), placeHolder("#0000FF")]

# We will need frames to figure out the FPS of the program.
frames = 0

# This sets the resolution of the screen and also gives a var,
# which we name screen. This var will be the first thing passed
# into the api.display() function. For our purposes, the
# default options (800x600) is enough.
screen = api.setres()

# Display is what we're going to display.
display = []

# This is the framecounter function. It declares frames to be a
# global variable. Then, every second, it prints its value then
# sets it to zero.
def framecounter():
    global frames
    # api.isquit() tells us if the player has clicked the X on
    # the window or not.
    while not api.isquit():
        api.wait(1)
        print(f"fps: {frames}")
        frames = 0

# We will make display a 200x200 array filled with some colors from the
# colors variable.
for timesY in range(200):
    display.append([])
    for timesX in range(200):
        display[-1].append(choice(colors))

# This starts the framecounter thread. We don't need to make a
# variable out of it, since it will terminate itself upon
# api.isquit().
Thread(target=framecounter).start()

# api.isquit() tells us if the player has clicked the X on the
# window or not, as explained previously.
while not api.isquit():
    # The api.display() function takes 4 variables.

    # 1: screen: this is the screen that we obtain through the
    # api.setres() function.

    # 2: newscreen: This is an array that we want to display.

    # 3: widthofeachblock: How wide each block/tile should be.

    # 4: heightofeachblock: How tall each block/tile should be.

    api.display(screen=screen, newscreen=display, widthofeachblock=2, heightofeachblock=2)
    # This increments the frames variable after we display a
    # frame, which the framecounter thread prints and sets to
    # 0 every second. This is one way to measure FPS.
    frames += 1
