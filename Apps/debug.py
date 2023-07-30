from api import display
from api import reachableindex
try: from colorama import init, Back
except(ModuleNotFoundError): import os; os.system("pip install colorama"); from colorama import init, Back; os.system("cls")
import random

init(convert=True)

width = 84
height = 47
Air = "Air"
Grs = "Grs"
Drt = "Drt"
Stn = "Stn"
Bdr = "Bdr"
Leaf = "Leaf"
Logg = "Logg"
Aire = Air
I_ore = "I_ore"
L_ore = "L_ore"
config = [Grs, Grs, Drt, Drt, Drt, Drt]
oreconfig = {
    "ironore": [5, 10, 20, I_ore],
    "Luxian": [15, 20, 40, L_ore]
}
colors = {
    "Air": ["lightblue", "back", "  "],
    "Grs": ["green", "back", "  "],
    "Drt": ["yellow", "back", "  "],
    "Stn": ["lightblack", "back", "  "],
    "Bdr": ["lightwhite", "back", "  "],
    "Leaf": ["green", "back", "  "],
    "Logg": ["lightyellow", "back", "  "],
    "I_ore": ["white", "back", "  "],
    "L_ore": ["blue", "back", "  "]
}
structures = {
    "tree": {
        "struct": {
            "y4": [Aire, Leaf, Leaf, Leaf, Aire],
            "y3": [Leaf, Leaf, Leaf, Leaf, Leaf],
            "y2": [Leaf, Leaf, Logg, Leaf, Leaf],
            "y1": [Aire, Aire, Logg, Aire, Aire],
            "y0": [Aire, Aire, Logg, Aire, Aire],
        },
        "spawnchance": 5,
        "ylevel": -1,
        "totalspace": [-4, 5]
    }
}
limit = [20, 30]

def generate(width,height, config, Air, Stn, Bedrock, limit, structures, oreconfig={}):
    # Air = literally the air, the thing that permeates open spaces.
    
    # Stn = the thing that permeates closed spaces deep underground.
    
    # Bedrock = the bottom layer of the world that separates the player from the void.
    
    # config = Layers, e.g. if there should be two layers of dirt at the top then one layer of Crs, then
    # config should be [Drt,Drt,Crs] provided Drt and Crs are variables.
    
    # Create the initial space
    
    space = {}
    for i in range(height):
        space["y" + str(i + 1)] = []
        for n in range(width): # Do it for every X
            if i != range(height)[-1]: # And Y value
                space["y" + str(i + 1)].append(Air) # Add Air if the Y value is not the last one (if the selected Y value is not at the bottom)
            else:
                space["y" + str(i + 1)].append(Bedrock) # Add Bedrock otherwise

    # Add blocks (finally use config)
    
    # The top solid layer of the world
    originalY = random.randint(limit[0],limit[1])
    # Y is used for config, to generate things belwo the top layer.
    Y = originalY
    # X is used for.. Well, X.
    X = 0
    # Used later for structure and ore generation
    toplayer = []
    toplayer.append([originalY, X])
    # First initial layer
    space["y" + str(Y)][X] = config[0]

    for i in range(width): # Width has been chosen for 3. (1)

        for i in range(height): # Height has been chosen to use Y.
            if Y == 0: Y += 1 # If Y is somehow higher than the height limit, increase it.
            elif Y < 0: Y = abs(Y); Y += 1 # If Y is somehow even HIGHER than the height limit, convert it to a positive or at least 1.
            elif Y >= height:
                while Y >= height: Y-= 1 # If Y is somehow lower than or at the Bedrock layer, decrease it.
            if (i - 1) >= 0 and space["y" + str(Y)][X] != Bedrock: # If Y is not 0 and the currently selected Block isn't Bedrock.
                if reachableindex(config, i - 1): space["y" + str(Y)][X] = config[i - 1] # If the config hasn't ran out, apply the latest layer.
                elif reachableindex(config, i - 1) == False: space["y" + str(Y)][X] = Stn # Otherwise, may the block be Stone.
                if Y < height: Y += 1 # If Y is not at the Bedrock layer, increase it.
        # nextplace can be one of three values chosen randomly: 1, 2, and 3.
        # No matter what value nextplace is, X will always increase as long as it doesn't surpass width while doing so.
        above = 1
        below = 3
        if originalY + 1 < limit[0] or originalY + 1 < 1:
            above = 2
        if originalY - 1 > limit[1] or originalY - 1 > (height - 1):
            below = 2
        
        try: nextplace = random.randint(above,below)
        except(ValueError): nextplace = 2
        
        f = open("logs.txt", "a")
        f.write(f"originalY: {originalY}\nnextplace: {nextplace}\nlimit[0]: {limit[0]}\nlimit[1]: {limit[1]}\ni: {i}\nwidth: {width}\nabove: {above}\nbelow: {below}\n\n")
        if X < width - 1:
            if nextplace == 1: # If nextplace is equal to 1, the block placed in the next X coord's Y coord will be higher than the last X coord block's Y coord.
                f.write("Up.\n\n")
                originalY -= 1
                X += 1
            elif nextplace == 2: # If nextplace is equal to 2, the block placed in the next X coord's Y coord will be the same as the last X coord block's Y coord.
                f.write("Middle.\n\n")
                X += 1
            elif nextplace == 3 : # If nextplace is equal to 3, the block placed in the next X coord's Y coord will be lower than the last X coord block's Y coord.
                f.write("Down.\n\n")
                originalY += 1
                X += 1
            Y = originalY # Set Y to the top solid block.
                # All of this is code jargon for "If nextplace = 1, go up a block.
                # If nextplace = 2, stay at the same height.
                # If nextplace = 3, go down a block.
                # Otherwise select a different value for nextplace.
                # Then start generating blocks from the top to the bottom."
        f.close()
        toplayer.append([originalY, X])
    
    # Ore and Structure Generation

    # Ore -
    for n in toplayer:
        if oreconfig != {}:
            for i in list(oreconfig.values()):
            
                spawnchance = random.randint(1, i[0])

                if spawnchance == 1 and reachableindex(space,"y" + str(n[0] + i[1])):
                    area = random.randint(i[1], i[2])
                    carea = n[0] + area
                    if carea >= height:
                        while carea >= height: carea -= 1
                    space["y" + str(carea)][n[1]] = list(oreconfig.values())[list(oreconfig.values()).index(i)][3]
    
    # Structures -
    for n in toplayer:
        for i in list(structures.values()):
            spawnchance = random.randint(1, i["spawnchance"])
            totalspace = i["totalspace"]
            
            if True:
                if spawnchance == 1 and reachableindex(space["y" + str(n[0])], totalspace[1] + 1):
                    for x in reversed(i["struct"].values()):
                        for y in x:
                            if reachableindex(space["y" + str(n[0] - i["ylevel"])], X + x.index(y)):
                                space["y" + str(n[0] - i["ylevel"])][X + x.index(y)] = y
    
    # FINALLY return the world.
    
    return list(space.values())
import time
import os
space = generate(width, height, config, Air, Stn, Bdr, limit=limit, oreconfig=oreconfig, structures=structures)
while True:
    display(space,colors)
    time.sleep(1/20)
    os.system("cls")
