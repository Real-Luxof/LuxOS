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

void = blackvoid()


def generate(colors: list, width: int, height: int, chanceofvoid: float) -> list:
    """Generates a big ass list filled with either black or a color/particle.

    Args:
        colors (list): A list of all the colors/particles.
        width (int): The width of the world.
        height (int): The height of the world.
        chanceofvoid (float): What chance is there that there will be black void instead of a particle?

    Returns:
        list: The entire world that was just generated.
    """
    world = []
    for timesX in range(width):
        world.append([])
        for timesY in range(height):
            if random.randint(1, 100) <= chanceofvoid:
                world[-1].append(void)
            else:
                world[-1].append(random.choice(colors))
                

    return world

red = api.block("red","#0000FF",False,False,0,"red",False)
green = api.block("green","#00FF00",False,False,0,"green",False)
blue = api.block("blue","#FF0000",False,False,0,"blue",False)
allblocks = [red, green, blue]

world = generate(allblocks, 200, 200, 99)
new_world = world

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
screen = api.setres(800,600)
api.display(screen,world,2,2)
while not quittime:
    #if world != new_world:
    #    world = new_world
    api.display(screen,world,4,3)
    frames += 1
    
    if api.isquit():
        api.closewindow()
        quittime = True
