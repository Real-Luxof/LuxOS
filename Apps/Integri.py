# - Loading Started -

# Import os. It is needed to check for and create folders, as well as to install modules.
import os

# Try to import colorama. If it's not available, try to install it and then import it.
try: from colorama import Fore, Back, Style, init
except(ModuleNotFoundError): api.install("colorama"); from colorama import Fore, Back, Style, init
init()

# Loading Bar
l = "Loading." # Set l to "Loading."
bar = "|          |" # Set bar to "|          |"
print(l + "\n" + bar) # Display the loading bar
def increment(num=1): # Fill the loading bar a bit num many times and then print it
    global l # Globalize the variable l
    global bar # Globalize the variable bar
    api.clear() # Clear the screen with the LuxOS logo
    for n in range(num): # For every number in num..
        match l: # Check l, the rest is self-explanatory.
            # If you really wanna know, it adds a dot to the end of the variable,
            # and if the variable has 3 dots at the end, it resets it to 1.
            case "Loading.": l = "Loading.."
            case "Loading..": l = "Loading..."
            case "Loading...": l = "Loading."
        match bar: # Check bar, The rest is self-explanatory.
            # If you really wanna know, it fills the bar up a bit.
            case "|          |": bar = "|█         |"
            case "|█         |": bar = "|██        |"
            case "|██        |": bar = "|███       |"
            case "|███       |": bar = "|████      |"
            case "|████      |": bar = "|█████     |"
            case "|█████     |": bar = "|██████    |"
            case "|██████    |": bar = "|███████   |"
            case "|███████   |": bar = "|████████  |"
            case "|████████  |": bar = "|█████████ |"
            case "|█████████ |": bar = "|██████████|"
    print(l + "\n" + bar)

# Initialize the Game Engine
print("Initializing Game Engine..")
try: import api # Try to import it.
except(ModuleNotFoundError): input("Couldn't find the engine, I'm gonna quit now! LUL."); quit
# If the program can't for whatever reason, quit.

# Import the import_module function from the importlib module
print("Importing function: import_module from module: importlib")
from importlib import import_module

# Import the Thread function from the threading module
print("Importing function: Thread from module: threading")
from threading import Thread

increment()
increment()

# Folder variables used for loading

print("Loading path variables..")
integrifiles = "gamedata\\integri" # Variable for main game files
integrisaves = "gamedata\\integri\\saves" # Variable for the saves folder.
integrist = "gamedata\\integri\\soundtrack" # Variable for the soundtrack folder.

increment()

# Make the savegame function
print("Making savegame function..")
def savegame(savename, world, worldtype, plr, single):
    if single == True: # If single is equal to True,
        with open(integrisaves + "\\" + savename + ".py", "w") as f: # Open the save from the saves folder in the integri game files folder and call it "f".
            # Define what will go in there in a variable called "data".
            # plr = the current player character
            # world = the current world
            data = """
import os
import sys
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

plr = api.player(character=\"""" + plr.character + """\",maxhealth=""" + str(plr.maxhealth) + """,health=""" + str(plr.health) + """,armor=""" + str(plr.armor) + """,attack=""" + str(plr.attack) + """,defense=""" + str(plr.defense) + """,speed=""" + str(plr.speed) + """,position=""" + str(plr.position) + """,inventory=api.inventory(slotnum=""" + str(plr.inventory.slotnum) + """,slotdata=""" + str(plr.inventory.slots) + """,selectedindex=\"""" + plr.inventory.selectedindex + """\"),dead=""" + str(plr.dead) + """,deffactor=""" + str(plr.deffactor) + """,atkfactor=""" + str(plr.atkfactor) + """)
world = """ + str(world) + """
worldtype = """ + str(worldtype) + """
"""
            f.write(data) # Write the contents of "data" into the file.

increment()

# - Folder Checking -

# Check for and (if it doesn't exist) create a folder to store game data.

print("Checking game data..")
if os.path.exists(integrifiles) == False: # Check if it exists.
    print("Installing integri in gamedata..") # If it doesn't, log that the program's creating a new one.
    os.system("md " + integrifiles) # Create the folder.

increment()

# Check the Saves folder, and create one if it doesn't exist.

print("Making checksaves function and running it to check saves..")
def checksaves():
    if os.path.exists(integrisaves): # Check if the Saves folder exists.
        Saves = os.listdir(integrisaves) # If yes, list all the files in there.
        if "__pycache__" in Saves:
            del Saves[Saves.index("__pycache__")]
        while len(Saves) < 4: # While there are less than 4 elements in Saves,
            Saves.append("") # Add an empty string to the list.
        for savename in Saves:
            savenamelist = savename.split(".py") # Separate ".py" from every string in the list.
            del savenamelist[-1] # Delete the ".py" from every string in the list..
            newsavename = ""
            for char in savenamelist:
                newsavename += char
            Saves[Saves.index(savename)] = newsavename
    else: # If it doesn't, then..
        print("Making saves folder..") 
        os.system("md " + integrisaves) # Create the saves folder,
        Saves = ["", "", "", ""] # and make the Saves variable blank because there aren't any saves yet.
    return Saves # Return the variable Saves.
Saves = checksaves() # Run the function to check all the saves.

increment()

# Check if the soundtrack folder and its subfolders exist.

# Check the soundtrack folder.
print("Checking soundtrack..")
if os.path.exists(integrist) == False: # Check if the Soundtrack folder doesn't exist.
    print("Installing soundtrack folder..")
    os.system("md " + integrist) # If it doesn't, make it.

# Check the music subfolder.
print("Checking music..")
if os.path.exists(integrist + "\\music") == False: # Check if the music subfolder exists.
    print("Installing music..")
    os.system("md " + integrist + "\\music") # If it doesn't, make it.

# Check the sfx subfolder.
print("Checking sfx..")
if os.path.exists(integrist + "\\sfx") == False: # Check if the sfx subfolder within the Soundtrack fodler exists.
    print("Installing sfx..")
    os.system("md " + integrist + "\\sfx") # If it doesn't, make it.

# Check utilityfolder.
print("Checking utilityfolder..")
if os.path.exists(integrifiles + "\\utilityfolder\\") == False:
    print("Installing utilityfolder..")
    os.system("md " + integrifiles + "\\utilityfolder")

# Check the blocks file.
print("Checking blocks file..")
with open(integrifiles + "\\utilityfolder\\blocks.py", "w+") as f:
    data = """import os
import sys
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

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = api.block(image="#00AAFF",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Air. 
Grs = api.block(image="#00FF00",passable=False,breakablebytool=True,droptoolvalue=1,drop="Dirt",falling=False) # Define Grass.
Drt = api.block(image="#945035",passable=False,breakablebytool=True,droptoolvalue=2,drop=None,falling=False) # Define Dirt.
Stn = api.block(image="#606060",passable=False,breakablebytool=True,droptoolvalue=3,drop="Stone",falling=False) # Define Stone.
Snd = api.block(image="#DDDD55",passable=False,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Sand.
Bdr = api.block(image="#000000",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Bedrock.
plr = api.player(character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],inventory=api.inventory(slotnum=20),dead=False,deffactor=0.5,atkfactor=0.5) # Define the player.
Iro = api.block(image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False) # Define Iron ore.
Col = api.block(image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False) # Define Coal.
Irn = api.block(image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False) # Define Iron bar.

# Oreconfig
print("Loading ore configurations..")

global oreconfigabove # Declare oreconfigabove a global variable.
oreconfigabove = { # oreconfigabove is used to define ore rarity and placement near the surface.
    "Ironore": [20, 10, 40, Iro],
    # Iron ore has a 1/20th (5%) chance of spawning on each Y level between 10 and 40.
    # Its block is Iro.
    "Coalore": [20, 20, 30, Col]
    # Coal ore has a 1/20th (5%) chance of spawning on each Y level between 20 and 30.
    # Its block is Col.
}

global oreconfigbelow # Declare oreconfigbelow a global variable.
oreconfigbelow = { # oreconfigbelow is used to define ore rarity and placement below the surface level.
    "Ironore": [10, 0, 30, Iro],
    # Iron ore has a 1/10th (10%) chance of spawning on each Y level between 0 and 20.
    # Its block is Iro.
    "Coalore": [8, 0, 30, Col]
    # Coal ore has a 1/8th (12.5%) chance of spawning on each Y level between 0 and 30.
    # Its block is Col.
}

# Biome layers
print("Loading biome layers..")

desertlayers = [Snd,Snd,Snd,Snd,Snd,Snd,Snd] # Biome layers for the Desert biome.
plainslayers = [Grs,Grs,Grs,Drt,Drt] # Biome layers for the Plains biome.
allbiomes = [desertlayers,plainslayers]"""
    if f.read != data:
        f.write(data)

# Check generateworldpackage.
print("Checking generateworldpackage..")
with open(integrifiles + "\\utilityfolder\\generateworldpackage.py", "w+") as f:
    data = """from ...integri.utilityfolder.blocks import *
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
    return world"""
    if f.read != data:
        f.write(data)

increment()
increment()

# - Folder Checking finished -

# generateworld function

from gamedata.integri.utilityfolder.blocks import *
from gamedata.integri.utilityfolder.generateworldpackage import *

increment()

# Title screen
print("Making title function..")
title = [ # Define the title characters and their colors.
    Back.LIGHTBLACK_EX + "  _  " + Back.RED + "  ___       _  " + Back.GREEN + "  _____________  " + Back.BLUE + "  ________ " + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " |   \     | | " + Back.GREEN + " |_____   _____| " + Back.BLUE + " |  ______|" + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |\ \    | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |       " + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | | \ \   | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |______ " + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |  \ \  | | " + Back.GREEN + "       | |       " + Back.BLUE + " |  ______|" + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |   \ \ | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |       " + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |    \ \| | " + Back.GREEN + "       | |       " + Back.BLUE + " | |______ " + Style.RESET_ALL,
    Back.LIGHTBLACK_EX + " |_| " + Back.RED + " |_|     \___| " + Back.GREEN + "       |_|       " + Back.BLUE + " |________|" + Style.RESET_ALL,
    "",
    "        " + Back.RED + "  __________  " + Back.GREEN + "  ________  " + Back.BLUE + "  _ " + Style.RESET_ALL,
    "        " + Back.RED + " |  ______  | " + Back.GREEN + " |  _____ | " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |      |_| " + Back.GREEN + " | |    | | " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |          " + Back.GREEN + " | |____| | " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |   _____  " + Back.GREEN + " |    ____| " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |  |___  | " + Back.GREEN + " | | \ \    " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |      | | " + Back.GREEN + " | |  \ \   " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |______| | " + Back.GREEN + " | |   \ \  " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " |__________| " + Back.GREEN + " |_|    \_\ " + Back.BLUE + " |_|" + Style.RESET_ALL,
    "\n"
]
def displaytitle(): # Define a function named displaytitle.
    api.fullclear() # Clear the screen.
    for row in title: # Check, and
        print(row) # Print out every row in the title variable.

increment()

# - Loading Finished -

# Main Game Loop

while True:
    # Main Menu
    option = None # Set the currently selected option (variable name option's value) to None.
    displaytitle() # Display the title.
    # Present the options and how to select one of them.
    print(Fore.LIGHTBLACK_EX + "Click the number before the option to select it.")
    print(Fore.GREEN +         "                1. Singleplayer                 ")
    print(Fore.BLUE +          "                2. Multiplayer                  ")
    print(Fore.YELLOW +        "                3. Options                      ")
    print(Fore.RED +           "                4. Quit                         ")
    print()
    
    # Decide what to do with the keyboard input.
    while True: # Until the loop is broken check if..
        if api.ispressed_key("1"): # The user presses 1.
            option = 1 # If they do, set option to 1 and
            break # Break the loop.
        elif api.ispressed_key("2"): # The user presses 2.
            option = 2 # If they do, set option to 2 and
            break # Break the loop.
        elif api.ispressed_key("3"): # The user presses 3.
            option = 3 # If they do, set option to 3 and
            break # Break the loop.
        elif api.ispressed_key("4"): # The user presses 4.
            quit() # If they do, close the program.
    
    # Decide what to do with the variable option's value.
    if option == 1: # If it's 1,
        displaytitle() # Clear the screen and display the title.
        '''
        if Saves == []:
            worldlimit = [5, 20]
            width = 40
            height = 25
            playerspawnY = 15
            playerspawn = 0
            space = api.generate(width=width,height=height,config=plainslayers,Air=Air,Stn=Stn,Bedrock=Bdr,limit=worldlimit,originalYY=playerspawnY)
            playerspawnY = 13
            space[playerspawnY][0] = plr
            display = Thread(target=displaythread,args=[space])
            display.start()
            playworld(save)
        '''
        
        availablesaveoptions = ["1", "2", "3", "4"]
        availabledeletesaveoptions = ["5", "6", "7", "8"]

        while True:
            Saves = checksaves()
            displaytitle()
            print(Fore.LIGHTBLACK_EX + "            Please select an option.            ")
            print(Fore.LIGHTBLACK_EX + "Click the number before the option to select it.")
            print(Fore.GREEN + "                1. " + Saves[0])
            print(Fore.GREEN + "                2. " + Saves[1])
            print(Fore.GREEN + "                3. " + Saves[2])
            print(Fore.GREEN + "                4. " + Saves[3])
            print(Fore.RED + "                5. Delete " + Saves[0])
            print(Fore.RED + "                6. Delete " + Saves[1])
            print(Fore.RED + "                7. Delete " + Saves[2])
            print(Fore.RED + "                8. Delete " + Saves[3])
            selectedsave = api.wait_any()
            if selectedsave in availablesaveoptions:
                if Saves[int(selectedsave) - 1] == "":
                    namepass = False
                    while True:
                        savename = input(Fore.LIGHTBLACK_EX + "    Input name: >" + Fore.RESET)
                        if savename.count(" ") > 0:
                            input(Fore.LIGHTBLACK_EX + "Invalid name." + Fore.RESET)
                        else:
                            break
                    displaytitle()
                    print(Fore.LIGHTBLACK_EX + "           Please select a world size.          ")
                    print(Fore.LIGHTBLACK_EX + "Click the number before the option to select it.\n")
                    print(Fore.GREEN + "1. Very small - I'm 35 and have an hour for this\ngame.\n")
                    print(Fore.GREEN + "2. Small - I want to play alone.\n")
                    print(Fore.CYAN + "3. Medium - I have someone to play with or wanna\nplay for a long time.\n")
                    print(Fore.CYAN + "4. Medium Large - There are 3-4 people here.\n")
                    print(Fore.BLUE + "5. Large - The entire family's playing.\n")
                    print(Fore.BLUE + "6. Very Large - I'm gonna be here for some\nmonths.\n")
                    print(Fore.YELLOW + "7. Extremely Large - This world will exist for\nyears.\n")
                    print(Fore.YELLOW + "8. Too Large - I just don't ever want to worry\nabout world size.\n")
                    print(Fore.RED + "9. Infinite - Generate as I go, I'm planning\ndecades!" + Fore.RESET)
                    
                    availableoptions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while True:
                        selectedoption = api.wait_any()
                        if selectedoption in availableoptions:
                            worldtype = int(selectedoption)
                            break
                    api.fullclear()
                    world = generateworld(worldtype,100,100)
                    match worldtype:
                        case 1: middleworld = world["22"]; middleworldindex = "22"
                        case 2: middleworld = world["33"]; middleworldindex = "33"
                        case 3: middleworld = world["44"]; middleworldindex = "44"
                        case 4: middleworld = world["66"]; middleworldindex = "66"
                        case 5: middleworld = world["88"]; middleworldindex = "88"
                        case 6: middleworld = world["1010"]; middleworldindex = "1010"
                        case 7: middleworld = world["1212"]; middleworldindex = "1212"
                        case 8: middleworld = world["2525"]; middleworldindex = "2525"
                    api.fullclear()
                    plr.position[0] = 50
                    # Set the X Value of the player to be the middle of the screen
                    plr.position = [plr.position[0], plr.position[1], middleworldindex, middleworld]
                    # Append "middleworldindex" and "middleworld" to plr.position
                    for i in plr.position[3]:
                        if i[plr.position[0]].passable and plr.position[3][plr.position[3].index(i) + 1][plr.position[0]].passable == False:
                            # If the player can pass through the currently selected block and below that is a solid surface,
                            plr.position.append(i[plr.position[0]]) # Add the element to plr.position.
                            i[plr.position[0]] = plr # Spawn the player there.
                            plr.position[1] = plr.position[3].index(i) # Also adjust the Y value of the player to be accurate.
                            if plr.position[1] != plr.position[3].index(i):
                                plr.position[1] = plr.position[3].index(i)
                            break
                    savegame(savename=savename,world=world,worldtype=worldtype,single=True,plr=plr)
                    # Save the game
                else:
                    save = import_module("gamedata.integri.saves." + str(Saves[int(selectedsave) - 1]))
                    plr = save.plr
                    world = save.world
                    worldtype = save.worldtype
                    break
                api.initiatewindow()
                screen = api.setres()
                
                def displaythread(screen):
                    while api.isquit() == False:
                        api.display(screen, plr.position[3], 8, 6)
                        api.wait(1/60)
                
                displayfunc = Thread(target=displaythread,args=[screen],daemon=True)
                displayfunc.start()
                
                gravtimer = 0
                gravmltp = 1
                newdata = [plr.position[3], plr.position[4]]
                while api.isquit() == False:
                    
                    # Player interaction
                    
                    if api.ispressed_key("w"):
                        newdata = plr.move("w", plr.position[3], plr.position[4])
                    elif api.ispressed_key("a"):
                        newdata = plr.move("a", plr.position[3], plr.position[4])
                    elif api.ispressed_key("s"):
                        newdata = plr.move("s", plr.position[3], plr.position[4])
                    elif api.ispressed_key("d"):
                        newdata = plr.move("d", plr.position[3], plr.position[4])
                    
                    # Apply Gravity
                    
                    #if plr.position[3][plr.position[1] + 1][plr.position[0]].passable == True:
                    #    gravtimer += 1
                    #else:
                    #    gravmltp = 0
                    #    gravtimer = 0
                    #if gravtimer >= 2:
                    #    gravmltp += 1
                    #if gravmltp > 0:
                    #    newdata = plr.move("s", plr.position[3], plr.position[4], gravmltp)
                    
                    # Other stuff
                    
                    plr.position[3] = newdata[0] # Update display
                    plr.position[4] = newdata[1] # Update what used to be at a position before the player was.
                    api.wait(1/20)
                
            elif selectedsave in availabledeletesaveoptions:
                match int(selectedsave):
                    case 5: api.delete("integri\\saves\\" + Saves[0] + ".py"); del Saves[0]
                    case 6: api.delete("integri\\saves\\" + Saves[1] + ".py"); del Saves[1]
                    case 7: api.delete("integri\\saves\\" + Saves[2] + ".py"); del Saves[2]
                    case 8: api.delete("integri\\saves\\" + Saves[3] + ".py"); del Saves[3]
        displaytitle()
