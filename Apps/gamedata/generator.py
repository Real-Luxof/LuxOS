import api
from numba import njit
from threading import Thread
import random
from math import ceil

# A black block designed to fool the Game Engine.
# The Engine thinks it's acceptable and it works exactly like a block,
# but with severely limited functionality to the point it is designed
# to sit around doing nothing.
# A bonus is that it theoretically takes way less memory.
class blackvoid:
    def __init__(self):
        self.passable = True
    def __repr__(self):
        return "#000000"
    def __str__(self):
        return "#000000"


def generate(colors: list, width: int, height: int, chanceofvoid: float) -> list:
    """Generates a big ass list filled with either black or a color/particle.

    Args:
        colors (list): A list of all the colors/particles.
        width (int): The width of the world.
        height (int): The height of the world.
        chanceofvoid (float): What chance is there that there will be black void instead of a particle?

        Examples for chanceofvoid:
            idk man just know the probability is calculated like ceil(len(colors) * chanceofvoid)

    Returns:
        list: The entire world that was just generated.
    """
    world = []
    for color in range(ceil(len(colors) * chanceofvoid)):
        colors.append(blackvoid())
    for timesX in range(width):
        world.append([])
        for timesY in range(height):
            world[-1].append(random.choice(colors))

    return world

red = api.block("red","#0000FF",False,False,0,"red",False)
green = api.block("green","#00FF00",False,False,0,"green",False)
blue = api.block("blue","#FF0000",False,False,0,"blue",False)
allblocks = [red, green, blue]

world = generate(allblocks, 200, 200, 15)

global frames
frames = 0
quittime = False
def framecounter():
    global frames
    while not quittime:
        api.wait(1)
        print(f"fps: {frames}")
        frames = 0

Thread(target=framecounter).start()

api.initiatewindow()
try:
    while True:
        api.display(api.setres(800,600),world,4,4)
        frames += 1
        api.wait(1/5)
except(KeyboardInterrupt):
    quittime = True
