from ...integri.utilityfolder.blocks import *
import random
import os
import sys
import time
# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the parent directory of the current file
parent_dir = os.path.dirname(current_file_path)

# Get the parent directory of the parent directory
grandparent_dir = os.path.dirname(parent_dir)

# Get the parent directory of the grandparent directory
greatgrandparent_dir = os.path.dirname(grandparent_dir)

# Get the parent directory of the greatgrandparent directory
final_dir = os.path.dirname(greatgrandparent_dir)

# Get the path to final_dir
final_path = os.path.abspath(final_dir)

sys.path.append(final_path)

import api

# generateworld's generation dependencies "skygeneration", and "belowgeneration".
print("Making generateworld function's dependencies skygeneration, and belowgeneration..")
def skygeneration():
    global widdth
    global heeight
    return api.generate(widdth,heeight,config=[Air],Air=Air,Stn=Air,Bedrock=Air,limit=[heeight - heeight + 1, heeight])

def belowgeneration(multiplier):
    global widdth
    global heeight
    return api.generate(widdth,heeight,config=[Stn],Air=Stn,Stn=Stn,Bedrock=Bdr,limit=[heeight - heeight + 1, heeight],oreconfig=multiplyoreconfig(oreconfigbelow,multiplier),oreeverywhere=True)

# generateworld's dependency multiplyoreconfig
print("Making generateworld function's dependency multiplyoreconfig..")
def multiplyoreconfig(config,multiplier):
    product = {} # Declare an empty dictionary named "product".
    for i in range(multiplier): # For multiplier many times,
        for n in config.keys(): # go through every key in config,
            product[n + str(i)] = config[n] # add it to "product" but add the a number in front of it.
    return product

# generateworld's dependency findlastY
print("Making generateworld function's dependency findlastY..")
def findlastY(part, width):
    for i in part: # Scroll through all Y coordinates in part.
        if i[width - 1].passable == False and part[part.index(i) + 1][width - 1].passable == False:
            return part.index(i)
            # if the block at the last X coordinate in the current Y coordinate is solid and
            # The block below it is also solid, return the Y coordinate of that block.

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype, width, height):
    global widdth
    global heeight
    widdth = width
    heeight = height
    global oreconfigabove
    global oreconfigbelow
    world = {}
    if worldtype == 1:
        for i in range(1, 4):
            for n in range(1, 4):
                world["1" + str(i)] = skygeneration()
                world[str(n + 2) + str(i)] = belowgeneration(n)
            if i == 1:
                world["2" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["2" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 2:
        for i in range(1, 6):
            for n in range(1, 6):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 3) + str(i)] = belowgeneration(n)
            world["2" + str(i)] = skygeneration()
            if i == 1:
                world["3" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["3" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 3:
        for i in range(1, 10):
            for n in range(1, 10):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 4) + str(i)] = belowgeneration(n)
            if i == 1:
                world["4" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["4" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 4:
        for i in range(1, 14):
            for n in range (1, 14):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 6) + str(i)] = belowgeneration(n)
            if i == 1:
                world["6" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["6" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 5:
        for i in range(1, 20):
            for n in range (1, 20):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 8) + str(i)] = belowgeneration(n)
            if i == 1:
                world["8" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["8" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 6:
        for i in range(1, 26):
            for n in range (1, 26):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 10) + str(i)] = belowgeneration(n)
            if i == 1:
                world["10" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["10" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 7:
        for i in range(1, 30):
            for n in range (1, 30):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 12) + str(i)] = belowgeneration(n)
            if i == 1:
                world["12" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["12" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    elif worldtype == 8:
        for i in range(1, 50):
            for n in range (1, 50):
                world[str(n) + str(i)] = skygeneration()
                world[str(n + 25) + str(i)] = belowgeneration(n)
            if i == 1:
                world["25" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove)
            else:
                world["25" + str(i)] = api.generate(width,height,config=random.choice(allbiomes),Air=Air,Stn=Stn,Bedrock=Stn,limit=[20, height - 20],oreconfig=oreconfigabove,originalYY=findlastY(world["2" + str(i - 1)],width))
    return world