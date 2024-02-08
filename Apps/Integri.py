# - Loading Started -

# Import os. It is needed to check for and create folders, as well as to install modules.
import os

# Loading Bar
l = "Loading." # Set l to "Loading."
bar = "|          |" # Set bar to "|          |"
print(l + "\n" + bar) # Display the loading bar
def increment(num=1):
    """Fill the loading bar a bit num many times, and then print it."""
    global l
    global bar
    api.clear() # Clear the screen and put the LuxOS logo there
    for times in range(num):
        match l:
            case "Loading.": l = "Loading.."
            case "Loading..": l = "Loading..."
            case "Loading...": l = "Loading."
        match bar:
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

# Try to import colorama. If it's not available, try to install it and then import it.
print("Importing colorama..")
try: from colorama import Fore, Back, Style, init
except(ModuleNotFoundError): api.install("colorama"); from colorama import Fore, Back, Style, init
init()

# Import the import_module function from the importlib module
print("Importing function: import_module from module: importlib")
from importlib import import_module

# Import the Thread function from the threading module
print("Importing function: Thread from module: threading")
from threading import Thread

# Import the ceil function from the math module
print("Importing function: ceil from module: math")
from math import ceil, floor

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
            data = """from blocks import *
from ... import api

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
    data = """from ... import api

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
plr = api.entity(character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],inventory=api.inventory(slotnum=20),dead=False,deffactor=0.5,atkfactor=0.5) # Define the player.
Iro = api.block(image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False) # Define Iron ore.
Col = api.block(image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False) # Define Coal.
Irn = api.block(image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False) # Define Iron bar.

# Oreconfig
print("Loading ore configuration..")

global oreconfig # Declare oreconfig a global variable.
oreconfig = { # oreconfigabove is used to define ore rarity and placement near the surface.
    "Ironore": (50, 10, 40, Iro),
    # Iron ore has a 1/50th (2%) chance of spawning between 10 and 40 blocks below the top solid block.
    # Its block is Iro.
    "Coalore": (50, 20, 30, Col),
    # Coal ore has a 1/50th (2%) chance of spawning between 20 and 30 blocks below the top solid block.
    # Its block is Col.
    
    # Switching to deeper blocks.
    
    "Ironore1": (45, 40, 60, Iro),
    # Iron ore has a 1/45th (2.2%) chance of spawning between 40 and 70 blocks below the top solid block.
    # Its block is Iro.
    "Coalore1": (45, 30, 50, Col),
    # Coal ore has a 1/45th (2.2%) chance of spawning between 30 and 70 blocks below the top solid block.
    # Its block is Col.
    
    # Just imagine this below every entry:
    # "[x] has a 1/[index0] chance of spawning between [index1] and [index2] blocks below the top solid block.
    # Its block is [index3]."
    # I don't wanna continue commenting.
    
    "Ironore2": (35, 70, 100, Iro),
    "Coalore2": (35, 70, 100, Col),
    
    "Ironore2": (30, 100, 200, Iro),
    "Coalore2": (30, 100, 200, Col),
    
    "Ironore2": (20, 200, 350, Iro),
    "Coalore2": (20, 200, 350, Col),
    
    "Ironore2": (15, 350, 450, Iro),
    "Coalore2": (15, 350, 450, Col),
    
    "Ironore2": (10, 450, 99999999999999, Iro),
    "Coalore2": (10, 450, 99999999999999, Col),
}

# Biome layers
print("Loading biome layers..")

# Gonna do the oreconfig shenanigans with biomes.
desert1 = [10, 30, Snd,Snd,Snd,Snd,Snd,Snd,Snd] # Biome layers for the Desert biome.
plains1 = [10, 30, Grs,Grs,Grs,Drt,Drt] # Biome layers for the Plains biome.
desert2 = [15,50,Snd,Snd,Snd,Snd,Snd,Snd]
plains2 = [15,50,Grs,Grs,Grs,Drt,Drt]
desert3 = [25,60,Snd,Snd,Snd,Snd,Snd,Snd]
plains3 = [25,60,Grs,Grs,Grs,Drt,Drt]
desert4 = [40,90,Snd,Snd,Snd,Snd,Snd,Snd]
plains4 = [40,90,Grs,Grs,Grs,Drt,Drt]
desert5 = [60,120,Snd,Snd,Snd,Snd,Snd,Snd]
plains5 = [60,120,Grs,Grs,Grs,Drt,Drt]
desert6 = [70,200,Snd,Snd,Snd,Snd,Snd,Snd]
plains6 = [70,200,Grs,Grs,Grs,Drt,Drt]
biomes = [desert1,plains1,desert2,plains2,desert3,plains3,desert4,plains4,desert5,plains5,desert6,plains6]"""
    if f.read != data:
        f.write(data)

# Check generateworldpackage.
print("Checking generateworldpackage..")
with open(integrifiles + "\\utilityfolder\\generateworldpackage.py", "w+") as f:
    data = """from ...integri.utilityfolder.blocks import *
from ... import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype):
    world = {}
    match worldtype:
        case 1: newworldtype = [100, 5, 95]
        case 2: newworldtype = [200, 10, 190]
        case 3: newworldtype = [400, 20, 380]
        case 4: newworldtype = [700, 35, 665]
        case 5: newworldtype = [1000, 50, 950]
        case 6: newworldtype = [1500, 75, 425]
        case 7: newworldtype = [2000, 100, 1900]
        case 8: newworldtype = [3000, 150, 2850]
        case 9: newworldtype = [10000, 500, 9500]
    world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,)
    return [world, newworldtype]"""
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
    Style.RESET_ALL,
    Back.LIGHTBLACK_EX + "  _  " + Back.RED + "  ___       _  " + Back.GREEN + "  _____________  " + Back.BLUE + "  ________ ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " |   \     | | " + Back.GREEN + " |_____   _____| " + Back.BLUE + " |  ______|",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |\ \    | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |       ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | | \ \   | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |______ ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |  \ \  | | " + Back.GREEN + "       | |       " + Back.BLUE + " |  ______|",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |   \ \ | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |       ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |    \ \| | " + Back.GREEN + "       | |       " + Back.BLUE + " | |______ ",
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

print("Making function Add If Reachable (air)")
def air(listt, index, index2): # "air" stands for "Add If Reachable"
    if api.reachableindex(listt, index) and not index < 0:
        if api.reachableindex(listt[index], index2) and not index2 < 0: return listt[index][index2]
        else: return "#000000"
    else: return "#000000"

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
    while True:
        if api.ispressed_key("1"):
            option = 1
            break
        elif api.ispressed_key("2"):
            option = 2
            break
        elif api.ispressed_key("3"):
            option = 3
            break
        elif api.ispressed_key("4"):
            quit()
    
    # Decide what to do with the variable option's value.
    if option == 1:
        displaytitle()
        
        # Initialize the save options
        availablesaveoptions = ["1", "2", "3", "4"]
        availabledeletesaveoptions = ["5", "6", "7", "8"]

        while True:
            api.wait(0.1) # Delay so the user doesn't accidentally delete the wrong saves.
            Saves = checksaves()
            displaytitle()
            print(Fore.LIGHTBLACK_EX + "            Please select an option.            ")
            print("Click the number before the option to select it.")
            print(Fore.GREEN + "                1. " + Saves[0])
            print("                2. " + Saves[1])
            print("                3. " + Saves[2])
            print("                4. " + Saves[3])
            print(Fore.RED + "                5. Delete " + Saves[0])
            print("                6. Delete " + Saves[1])
            print("                7. Delete " + Saves[2])
            print("                8. Delete " + Saves[3])
            selectedsave = api.wait_any() # await a key press
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
                    print("Click the number before the option to select it.\n")
                    print(Fore.GREEN + "1. Very small - I'm 35 and have two seconds for \nthis game.\n")
                    print("2. Small - I'm 30 and have about an hour for\nthis game.\n")
                    print(Fore.CYAN + "3. Medium - I want to play alone.\n")
                    print("4. Medium Large - I want the loading to hurt.\n")
                    print(Fore.BLUE + "5. Large - Hurry up, the boys are here.\n")
                    print("6. Very Large - Yeah, sure, I can wait a century \nor two.\n")
                    print(Fore.YELLOW + "7. Extremely Large - Is this thing cythonized?\nOh it isn't? crap.\n")
                    print("8. Too Large - I just don't ever want to worry\nabout world size.\n")
                    print(Fore.RED + "9. Never stop playing - I never want to stop\nplaying, and also waiting for the world to generate.\n" + Fore.RESET)
                    
                    availableoptions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    while True:
                        selectedoption = api.wait_any()
                        if selectedoption in availableoptions:
                            worldtype = int(selectedoption)
                            break
                    
                    api.fullclear()
                    
                    worlddata = generateworld(worldtype) # Create the world
                    world = worlddata[0] # Initialize a few variables
                    worldtype = worlddata[1]
                    
                    plr.position[0] = ceil(worldtype[0] / 2) # Set the X Value of the player to be the middle of the world
                    
                    for Ycoord in world:
                        if Ycoord[plr.position[0]].passable and world[world.index(Ycoord) + 1][plr.position[0]].passable == False:
                            # If the player can pass through the currently selected block and below that is a solid surface,
                            plr.position.append(Ycoord[plr.position[0]]) # Add the element to plr.position.
                            Ycoord[plr.position[0]] = plr # Spawn the player there.
                            plr.position[1] = world.index(Ycoord) # Also adjust the Y value of the player to be accurate.
                            if plr.position[1] != world.index(Ycoord): # If the Y value is not adjusted,
                                plr.position[1] = world.index(Ycoord) # Adjust it again.
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
                screen = api.setres(800, 600)
                global quittime
                quittime = False
                
                def displaythread(screen):
                    global quittime
                    while not quittime:
                        displayoutput = []
                        for n in range(100):
                            displayoutput.append([])
                            for m in range(100):
                                displayoutput[n].append(air(world, plr.position[1] - (n - 50), plr.position[0] - (m - 50)))
                        api.display(screen, reversed(displayoutput), 8, 6)
                        api.wait(1/60) # "60 fps"
                
                displayfunc = Thread(target=displaythread,args=[screen],daemon=True)
                displayfunc.start()
                
                gravtimer = 0 # Initialize a few variables
                gravmltp = 1
                movedup = False
                newdata = [world, plr.position[2]]
                while api.isquit() == False:
                    
                    # Player interaction
                    
                    # Keys
                    wpressed = api.ispressed_key("w")
                    apressed = api.ispressed_key("a")
                    spressed = api.ispressed_key("s")
                    dpressed = api.ispressed_key("d")
                    
                    # Actions
                    if wpressed: newdata = plr.move("w", newdata[0], newdata[1]); movedup = True
                    if apressed: newdata = plr.move("d", newdata[0], newdata[1])
                    if spressed: newdata = plr.move("s", newdata[0], newdata[1])
                    if dpressed: newdata = plr.move("a", newdata[0], newdata[1])
                    
                    # Apply Gravity
                    
                    if world[plr.position[1] + 1][plr.position[0]].passable and movedup: # If the block below the player can be fallen through and the player is holding down W
                        gravtimer += 1 # then (self-explanatory code)
                    elif world[plr.position[1] + 1][plr.position[0]].passable and not movedup: # If the block below the player can be fallen through but the player isn't holding down W
                        if gravtimer < 25: gravtimer = 25 # then (self-explanatory code)
                        else: gravtimer += 1
                    else:
                        gravmltp = 0
                        gravtimer = 0
                    if gravtimer >= 25: gravmltp += 0.3
                    if gravmltp > 0: newdata = plr.move("s", newdata[0], newdata[1], floor(gravmltp))
                    
                    # Other stuff
                    
                    world = newdata[0] # Update display
                    plr.position[2] = newdata[1] # Update what used to be at a position before the player was.
                    movedup = False # Tell the game the player has not moved up (this is used for gravity in the next tick/update).
                    api.wait(1/20) # "20 tps/ups"
                quittime = True
                
            elif selectedsave in availabledeletesaveoptions:
                match int(selectedsave):
                    case 5: api.delete("integri\\saves\\" + Saves[0] + ".py"); del Saves[0]
                    case 6: api.delete("integri\\saves\\" + Saves[1] + ".py"); del Saves[1]
                    case 7: api.delete("integri\\saves\\" + Saves[2] + ".py"); del Saves[2]
                    case 8: api.delete("integri\\saves\\" + Saves[3] + ".py"); del Saves[3]
        displaytitle()
