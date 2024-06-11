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
integrifiles = "gamedata\\integri" # Variable for main game files.
integrisaves = "gamedata\\integri\\saves" # Variable for the saves folder.
integrist = "gamedata\\integri\\soundtrack" # Variable for the soundtrack folder.

increment()

# Make the savegame function
print("Making savegame function..")
def savegame(savename, world, worldtype, plr, single):
    if single == True: # If single is equal to True,
        with open(integrisaves + "\\" + savename + ".py", "w+") as f: # Open the save from the saves folder in the integri game files folder and call it "f".
            # Define what will go in there in a variable called "data", then write it to the file.
            # plr = the current player character
            # world = the current world
            # api.player(character=\"{plr.character}\",maxhealth=""" + str(plr.maxhealth) + """,health=""" + str(plr.health) + """,armor=""" + str(plr.armor) + """,attack=""" + str(plr.attack) + """,defense=""" + str(plr.defense) + """,speed=""" + str(plr.speed) + f""",position=[{plr.position[0]}, {plr.position[1]}],replace=api.{api.turntoblock(plr.replace)}]""" + """,inventory=api.inventory(slotnum=""" + str(plr.inventory.slotnum) + """,slotdata=""" + str(plr.inventory.slots) + """,selectedindex=\"""" + plr.inventory.selectedindex + """\"),dead=""" + str(plr.dead) + """,deffactor=""" + str(plr.deffactor) + """,atkfactor=""" + str(plr.atkfactor) + """)
            data = f"""from ..utilityfolder.blocks import *
import api

plr = {api.turntoblock(block=plr)}
world = {api.turnarraytoblocks(arrayofblocks=world)}
worldtype = {worldtype}"""

            f.write(data.replace("'", ""))

increment()

# - Folder Checking -

# Check for and (if it doesn't exist) create a folder to store game data.

print("Checking game data..")
api.checkandmake(integrifiles)

increment()

# Check the Saves folder, and create one if it doesn't exist.

print("Making checksaves function and running it to check saves..")
def checksaves():
    if api.checkpath(integrisaves): # Check if the Saves folder exists.
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
print("Checking soundtrack and installing if it doesn't exist..")
api.checkandmake(integrist)

# Check the music subfolder.
print("Checking music and installing if it doesn't exist..")
api.checkandmake(f"{integrist}\\music")

# Check the sfx subfolder.
print("Checking sfx and installing if it doesn't exist..")
api.checkandmake(f"{integrist}\\sfx")

# Check utilityfolder.
print("Checking utilityfolder and installing if it doesn't exist..")
api.checkandmake(f"{integrifiles}\\utilityfolder")

# Check the blocks file.
print("Checking blocks file..")
if not api.checkpath(f"{integrifiles}\\utilityfolder\\blocks.py"):
    with open(f"{integrifiles}\\utilityfolder\\blocks.py", "w+") as f:
        data = """import api

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = api.block(varname="Air",image="#00AAFF",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Air. 
Grs = api.block(varname="Grs",image="#00FF00",passable=False,breakablebytool=True,droptoolvalue=1,drop="Dirt",falling=False) # Define Grass.
Drt = api.block(varname="Drt",image="#945035",passable=False,breakablebytool=True,droptoolvalue=2,drop=None,falling=False) # Define Dirt.
Stn = api.block(varname="Stn",image="#606060",passable=False,breakablebytool=True,droptoolvalue=3,drop="Stone",falling=False) # Define Stone.
Snd = api.block(varname="Snd",image="#DDDD55",passable=False,breakablebytool=True,droptoolvalue=1,drop=None,falling=False) # Define Sand.
Bdr = api.block(varname="Bdr",image="#000000",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Bedrock.
plr = api.entity(varname="plr",character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],replace=Air,inventory=api.inventory(slotnum=20),dead=False,deffactor=0.5,atkfactor=0.5) # Define the player.
Iro = api.block(varname="Iro",image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False) # Define Iron ore.
Col = api.block(varname="Col",image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False) # Define Coal.
Irn = api.block(varname="Irn",image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False) # Define Iron bar.

Air.light_level = 0
Grs.light_level = 0
Drt.light_level = 0
Stn.light_level = 0
Snd.light_level = 0
Bdr.light_level = 0
plr.light_level = 0
Iro.light_level = 0
Col.light_level = 0
Irn.light_level = 0

# Oreconfig
print("Loading ore configuration..")

oreconfig = [
    api.OreConfiguration(
        2,
        1,
        10,
        20,
        Iro
    ),
    
    api.OreConfiguration(
        2,
        2,
        20,
        40,
        Col
    ),
    
    api.OreConfiguration(
        5,
        3,
        30,
        100,
        Iro
    ),
    
    api.OreConfiguration(
        5,
        3,
        50,
        120,
        Col
    ),
    
    api.OreConfiguration(
        7,
        5,
        100,
        200,
        Iro
    ),
    
    api.OreConfiguration(
        15,
        13,
        120,
        400,
        Col
    ),
    
    api.OreConfiguration(
        15,
        10,
        180,
        300,
        Iro
    ),
    
    api.OreConfiguration(
        25,
        17,
        390,
        700,
        Col
    ),
    
    api.OreConfiguration(
        25,
        20,
        300,
        700,
        Iro
    ),
    
    api.OreConfiguration(
        30,
        30,
        700,
        1500,
        Col
    ),
    
    api.OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    api.OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    api.OreConfiguration(
        35,
        50,
        1500,
        2500,
        Iro
    ),
    
    api.OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    api.OreConfiguration(
        45,
        60,
        2500,
        4000,
        Iro
    ),
    
    api.OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    api.OreConfiguration(
        50,
        100,
        4000,
        6000,
        Iro
    ),
    
    api.OreConfiguration(
        50,
        100,
        4000,
        6000,
        Col
    ),
    
    api.OreConfiguration(
        60,
        300,
        6000,
        10000,
        Iro
    ),
    
    api.OreConfiguration(
        60,
        300,
        6000,
        10000,
        Col
    )
]

# Biomes
print("Loading biomes..")

# Gonna do the oreconfig shenanigans with biomes.
biomes = [
    api.Biome(
        50,
        10,
        50,
        [Grs, Grs, Drt, Drt, Drt, Drt]
    ),
    
    api.Biome(
        50,
        10,
        50,
        [Snd, Snd, Snd]
    )
]"""
        if f.read != data:
            f.write(data)

# Check generateworldpackage.
print("Checking generateworldpackage..")
if not api.checkpath(f"{integrifiles}\\utilityfolder\\generateworldpackage.py"):
    with open(integrifiles + "\\utilityfolder\\generateworldpackage.py", "w+") as f:
        data = """from ...integri.utilityfolder.blocks import *
import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype):
    match worldtype:
        case 1:
            newworldtype = [500, api.Limit(25, 495)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 2:
            newworldtype = [1000, api.Limit(50, 950)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 3:
            newworldtype = [1500, api.Limit(100, 1400)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 4:
            newworldtype = [2000, api.Limit(100, 1900)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 5:
            newworldtype = [3500, api.Limit(200, 3300)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 6:
            newworldtype = [5000, api.Limit(500, 4500)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 7:
            newworldtype = [7000, api.Limit(500, 6500)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 8:
            newworldtype = [8000, api.Limit(500, 7500)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 9:
            newworldtype = [10000, api.Limit(1000, 8000)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
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
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " |   \\     | | " + Back.GREEN + " |_____   _____| " + Back.BLUE + " |  ______|",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |\\ \\    | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |       ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | | \\ \\   | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |______ ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |  \\ \\  | | " + Back.GREEN + "       | |       " + Back.BLUE + " |  ______|",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |   \\ \\ | | " + Back.GREEN + "       | |       " + Back.BLUE + " | |       ",
    Back.LIGHTBLACK_EX + " | | " + Back.RED + " | |    \\ \\| | " + Back.GREEN + "       | |       " + Back.BLUE + " | |______ ",
    Back.LIGHTBLACK_EX + " |_| " + Back.RED + " |_|     \\___| " + Back.GREEN + "       |_|       " + Back.BLUE + " |________|" + Style.RESET_ALL,
    "",
    "        " + Back.RED + "  __________  " + Back.GREEN + "  ________  " + Back.BLUE + "  _ " + Style.RESET_ALL,
    "        " + Back.RED + " |  ______  | " + Back.GREEN + " |  _____ | " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |      |_| " + Back.GREEN + " | |    | | " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |          " + Back.GREEN + " | |____| | " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |   _____  " + Back.GREEN + " |    ____| " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |  |___  | " + Back.GREEN + " | | \\ \\    " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |      | | " + Back.GREEN + " | |  \\ \\   " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " | |______| | " + Back.GREEN + " | |   \\ \\  " + Back.BLUE + " | |" + Style.RESET_ALL,
    "        " + Back.RED + " |__________| " + Back.GREEN + " |_|    \\_\\ " + Back.BLUE + " |_|" + Style.RESET_ALL,
    "\n"
]
def displaytitle(): # Define a function named displaytitle.
    api.fullclear() # Clear the screen.
    for row in title: # Check, and
        print(row) # Print out every row in the title variable.

print("Making function Add If Reachable (air)")
def air(listt, index, index2): # "air" stands for "Add If Reachable"
    global Bdr
    try:
        return listt[index][index2]
    except(IndexError):
        return Bdr

increment()

# - Loading Finished -

# Main Game Loop

while True:
    # Main Menu
    option = None # Set the currently selected option (variable name option's value) to None.
    displaytitle() # Display the title.
    # Present the options and how to select one of them.
    print(Fore.LIGHTBLACK_EX + "Press the number before the option to select it.")
    print(Fore.GREEN +         "                1. Singleplayer                 ")
    print(Fore.BLUE +          "                2. Multiplayer                  ")
    print(Fore.YELLOW +        "                3. Options                      ")
    print(Fore.RED +           "                4. Quit                         ")
    print()
    
    # Take keybaord input.
    option = api.wait_any()
    
    # Decide what to do with the keyboard input.
    if option == "1":
        displaytitle()
        
        # Initialize the save options
        availablesaveoptions = ["1", "2", "3", "4"]
        availabledeletesaveoptions = ["5", "6", "7", "8"]
        backtomenu = False

        while True:
            api.wait(0.1) # Delay so the user doesn't accidentally delete the wrong saves.
            Saves = checksaves()
            displaytitle()
            print(Fore.LIGHTBLACK_EX + "            Please select an option.            ")
            print("Press the number before the option to select it.")
            print(Fore.GREEN + "                1. " + Saves[0])
            print("                2. " + Saves[1])
            print("                3. " + Saves[2])
            print("                4. " + Saves[3])
            print(Fore.RED + "                5. Delete " + Saves[0])
            print("                6. Delete " + Saves[1])
            print("                7. Delete " + Saves[2])
            print("                8. Delete " + Saves[3])
            selectedsave = api.wait_any() # await a key press
            if selectedsave in availabledeletesaveoptions:
                match int(selectedsave):
                    case 5: api.delete("integri\\saves\\" + Saves[0] + ".py"); del Saves[0]
                    case 6: api.delete("integri\\saves\\" + Saves[1] + ".py"); del Saves[1]
                    case 7: api.delete("integri\\saves\\" + Saves[2] + ".py"); del Saves[2]
                    case 8: api.delete("integri\\saves\\" + Saves[3] + ".py"); del Saves[3]
                continue
            elif selectedsave not in availablesaveoptions:
                continue

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
                print(                     "Press the number before the option to select it.")
                print(Fore.GREEN +         "1. Very small - Over quicker than you in bed.")
                print(                     "2. Small - I'm 35 and have an hour for this.")
                print(Fore.CYAN +          "3. Medium - For messing around.")
                print(                     "4. Medium Large - It's ok, the bigger ones hurt.")
                print(Fore.BLUE +          "5. Large - Not sure what exact size I want.")
                print(                     "6. Large Large - I have a friend to play with.")
                print(Fore.YELLOW +        "7. Larger - Hurry up, I can't wait too long.")
                print(                     "8. Very Large - I don't mind waiting.")
                print(Fore.RED +           "9. MAXIMUM - Finally, a reasonable world size.")
                print(Fore.LIGHTBLACK_EX + "0. Back to Menu." + Style.RESET_ALL)

                availableoptions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                while True:
                    selectedoption = api.wait_any()

                    if selectedoption in availableoptions:
                        worldtype = int(selectedoption)
                        break
                    elif selectedoption == "0":
                        backtomenu = True
                        break

                if backtomenu == True: break

                api.fullclear()

                worlddata = generateworld(worldtype) # Create the world
                world = worlddata[0] # Initialize a few variables
                worldtype = worlddata[1]

                plr.position[0] = ceil(worldtype[0] / 2) # Set the X Value of the player to be the middle of the world

                for Ycoord in world:
                    if Ycoord[plr.position[0]].passable and world[world.index(Ycoord) + 1][plr.position[0]].passable == False:
                        # If the player can pass through the currently selected block and below that is a solid surface,
                        plr.replace = Ycoord[plr.position[0]] # Add the element to plr.position.
                        Ycoord[plr.position[0]] = plr # Spawn the player there.
                        plr.position[1] = world.index(Ycoord) # Also adjust the Y value of the player to be accurate.
                        if plr.position[1] != world.index(Ycoord): # If the Y value is not adjusted,
                            plr.position[1] = world.index(Ycoord) # Adjust it again.
                        break
                print("Saving the world..")
                savegame(savename=savename,world=world,worldtype=worldtype,single=True,plr=plr)
                # Save the game
                print("Success. We will get to work now.")
            else:
                print("Loading..")
                savename = str(Saves[int(selectedsave) - 1])
                save = import_module("gamedata.integri.saves." + savename)
                plr = save.plr
                world = save.world
                worldtype = save.worldtype
                del save
                print("Success. We will get to work now.")

            api.initiatewindow()
            screen = api.setres(800, 600)

            global quittime
            global frames
            quittime = False
            frames = 0

            def framecounter():
                global quittime
                global frames
                while not quittime:
                    api.wait(1)
                    print(f"fps: {frames}")
                    frames = 0

            def applylightingsystem(world):
                # Set the top of the world's light level to 15.
                for block in world[0]:
                    block.light_level = 15

                for timesY in range(2):
                    # timesY is approximately how many iterations I expect it to take
                    # to apply the lighting system and leave without any lighting glitches.
                    for Ylevel_coordinate in range(1, len(world)):
                        Ylevel = world[Ylevel_coordinate]
                        # Since the light level of the top blocks is already 15, there is
                        # no need to apply the lighting system to it.
                        lightlevelsaroundblock = []

                        for block_coordinate in range(len(Ylevel)):
                            above_block = world[Ylevel_coordinate - 1][block_coordinate].light_level
                            try:
                                left_block = Ylevel[block_coordinate - 1].light_level
                            except(IndexError):
                                left_block = 0

                            try:
                                right_block = Ylevel[block_coordinate + 1].light_level
                            except(IndexError):
                                right_block = 0

                            lightlevelsaroundblock.append(above_block)
                            lightlevelsaroundblock.append(left_block)
                            lightlevelsaroundblock.append(right_block)

                            block = Ylevel[block_coordinate]
                            block.light_level = api.average(lightlevelsaroundblock)
                            block.image = api.color_with_light(block.image, block.light_level, 15)

                return world

            def displaythread(screen):
                global quittime
                global frames
                while not quittime:
                    # LET HIM COOK :fire:
 #                   cookingdisplayoutput = []
                    displayoutput = []

#                    for n in range(worldtype[0]):
#                        cookingdisplayoutput.append([])
#
                    #    for m in range(100):
                    #        cookingdisplayoutput[n].append(air(world, plr.position[1] - (n - worldtype[0]), plr.position[0] - (m - 50)))

#                    cookingdisplayoutput = applylightingsystem(cookingdisplayoutput)

                    # I came up with a math formula to line up player coordinates
                    # between cookingdisplayoutput and displayoutput
                    # coordinate of player in cookingdisplayoutput =
                    # X - (X - (X_radius_around_player + 1))

                    for n in range(100):
                        displayoutput.append([])

                        for m in range(100):
                            displayoutput[-1].append(air(world, plr.position[1] - (n - 50), plr.position[0] - (m - 50)))

                    api.display(screen, reversed(displayoutput), 8, 6)
                    frames += 1
                    api.wait(1/60) # "60 fps"
                    # How does this work again
                    # lmao this shit ain't even CLOSE to 60 fps it runs at *~15*
                    # how does this run at ~23 fps

            displayfunc = Thread(target=displaythread,args=[screen],daemon=True)
            displayfunc.start()
            framecounterfunc = Thread(target=framecounter)
            framecounterfunc.start()

            gravtimer = 0 # Initialize a few variables
            gravmltp = 1
            holdingW = False
            newdata = [world, plr.replace]
            while api.isquit() == False:

                # Player interaction

                # Keys
                wpressed = api.ispressed_key("w")
                apressed = api.ispressed_key("a")
                spressed = api.ispressed_key("s")
                dpressed = api.ispressed_key("d")
                breakmode = api.ispressed_key("shift")

                # Actions
                if wpressed and not breakmode: newdata = plr.move("w", newdata[0], newdata[1]); holdingW = True
                if dpressed and not breakmode: newdata = plr.move("a", newdata[0], newdata[1])
                if spressed and not breakmode: newdata = plr.move("s", newdata[0], newdata[1])
                if apressed and not breakmode: newdata = plr.move("d", newdata[0], newdata[1])
                if wpressed and breakmode: newdata[0] = plr.breakblock("w", newdata[0], newdata[1])
                if dpressed and breakmode: newdata[0] = plr.breakblock("a", newdata[0], newdata[1])
                if spressed and breakmode: newdata[0] = plr.breakblock("s", newdata[0], newdata[1])
                if apressed and breakmode: newdata[0] = plr.breakblock("d", newdata[0], newdata[1])

                # Apply Gravity

                if world[plr.position[1] + 1][plr.position[0]].passable and holdingW: # If the block below the player can be fallen through and the player is holding down W
                    gravtimer += 1 # then (self-explanatory code)
                elif world[plr.position[1] + 1][plr.position[0]].passable and not holdingW: # If the block below the player can be fallen through but the player isn't holding down W
                    if gravtimer < 25: gravtimer = 25 # then (self-explanatory code)
                    else: gravtimer += 1
                else:
                    gravmltp = 0
                    gravtimer = 0
                if gravtimer >= 25: gravmltp += 0.3
                if gravmltp > 0: newdata = plr.move("s", newdata[0], newdata[1], floor(gravmltp))

                # Other stuff

                world = newdata[0] # Update display
                plr.replace = newdata[1] # Update what used to be at a position before the player was.
                holdingW = False # Tell the game the player has not moved up (this is used for gravity in the next tick/update).
                api.wait(1/20) # "20 tps/ups"
            quittime = True
            api.closewindow()

            print("Saving..")
            world = newdata[0] # Quickly update the world
            plr.replace = newdata[1] # Then update replace
            # May not be 100% accurate as in might be 1 frame behind but that is acceptable
            savegame(savename=savename,world=world,worldtype=worldtype,plr=plr,single=True)
            print("Saved.")
        displaytitle()
