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

# Json.
print("Json.")
import json

increment()
increment()

# Folder variables used for loading

print("Loading path variables..")
integrifiles = "gamedata\\integri"
integrisaves = "gamedata\\integri\\saves"
integrist = "gamedata\\integri\\soundtrack"
integrisprites = "gamedata\\integri\\utilityfolder\\sprites.py"

if __name__ != '__main__':
    integrifiles = f"Apps\\{integrifiles}"
    integrisaves = f"Apps\\{integrisaves}"
    integrist = f"Apps\\{integrist}"
    integrisprites = f"Apps\\{integrisprites}"

increment()

# Make the savegame function
print("Making savegame function..")
def savegame(savename, world, worldtype, plr, single):
    if single == True: # If single is equal to True,
        with open(integrisaves + "\\" + savename + ".py", "w+") as f: # Open the save from the saves folder in the integri game files folder and call it "f".
            # Define what will go in there in a variable called "data", then write it to the file.
            # plr = the current player character
            # world = the current world
            # api.player(image=\"{plr.image}\",maxhealth=""" + str(plr.maxhealth) + """,health=""" + str(plr.health) + """,armor=""" + str(plr.armor) + """,attack=""" + str(plr.attack) + """,defense=""" + str(plr.defense) + """,speed=""" + str(plr.speed) + f""",position=[{plr.position[0]}, {plr.position[1]}],replace=api.{api.turntoblock(plr.replace)}]""" + """,inventory=api.inventory(slotnum=""" + str(plr.inventory.slotnum) + """,slotdata=""" + str(plr.inventory.slots) + """,selectedindex=\"""" + plr.inventory.selectedindex + """\"),dead=""" + str(plr.dead) + """,deffactor=""" + str(plr.deffactor) + """,atkfactor=""" + str(plr.atkfactor) + """)
            #json.dumps(vars(plr))
            data = f"""from ..utilityfolder.blocks import *
import api

plr = {api.turntoblock(block=plr)}
world = {api.turnarraytoblocks(arrayofblocks=world)}
worldtype = [{worldtype[0]}, api.Limit({worldtype[1].upper_limit}, {worldtype[1].lower_limit})]"""

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
    if not api.checkpath(integrisaves):
        print("Making saves folder..")
        os.system(f"md {integrisaves}")
        Saves = ["", "", "", ""]
        return Saves
    
    Saves = os.listdir(integrisaves)
    Saves = api.stripimportant(Saves, ["__pycache__"])
    
    while len(Saves) < 4:
        Saves.append("")
    
    for savename_index in range(len(Saves)):
        Saves[savename_index] = Saves[savename_index].removesuffix(".py")
    
    return Saves

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
        data = """from api import block, entity, inventory, Biome, OreConfiguration

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = block(
    varname="Air",
    image="#00AAFF",
    passable=True,
    breakablebytool=False,
    droptoolvalue=None,
    drop=None,
    falling=False
)
Grs = block(
    varname="Grs",
    image="#00FF00",
    passable=False,
    breakablebytool=True,
    droptoolvalue=1,
    drop="Grass",
    falling=False
)
Drt = block(
    varname="Drt",
    image="#945035",
    passable=False,
    breakablebytool=True,
    droptoolvalue=2,
    drop="Dirt",
    falling=False
)
Stn = block(
    varname="Stn",
    image="#606060",
    passable=False,
    breakablebytool=True,
    droptoolvalue=3,
    drop="Stone",
    falling=False
)
Snd = block(
    varname="Snd",
    image="#DDDD55",
    passable=False,
    breakablebytool=True,
    droptoolvalue=1,
    drop="Sand",
    falling=False
)
Bdr = block(
    varname="Bdr",
    image="#000000",
    passable=True,
    breakablebytool=False,
    droptoolvalue=None,
    drop=None,
    falling=False
)
plr = entity(
    varname="plr",
    image="#FFC000",
    maxhealth=100,
    health=100,
    armor=0,
    attack=5,
    defense=5,
    speed=1,
    position=[0,12],
    replace=Air,
    inventory=inventory(slotnum=25),
    dead=False,
    deffactor=0.5,
    atkfactor=0.5,
    handvalue=2
)
Iro = block(
    varname="Iro",
    image="#797979",
    passable=False,
    breakablebytool=True,
    droptoolvalue=4,
    drop="Iron ore",
    falling=False
)
Col = block(
    varname="Col",
    image="#202020",
    passable=False,
    breakablebytool=True,
    droptoolvalue=3,
    drop="Coal",
    falling=False
)
Irn = block(
    varname="Irn",
    image="#909090",
    passable=False,
    breakablebytool=True,
    droptoolvalue=4,
    drop="Iron bar",
    falling=False
)

# this is used for placing blocks
all_blocks_dict = {
    "Iron bar": Irn,
    "Coal": Col,
    "Iron ore": Iro,
    "Sand": Snd,
    "Stone": Stn,
    "Dirt": Drt,
    "Grass": Grs
}

# Placeholder
print("Loading placeholders..")
class placeholder:
    \"\"\"A block but for display purposes.\"\"\"
    def __init__(
        self,
        varname: str,
        image: str,
        light_level: int,
        passable: bool
    ):
        self.varname = varname
        self.image = image
        self.light_level = light_level
        self.passable = passable
    
    def __str__(self):
        return self.image
    
    def __repr__(self):
        return self.image

class placeholder_dry:
    def __init__(
        self,
        image: str
    ):
        self.varname = "gsgl3r9vkjs3r" # necessity
        self.image = image
    
    def __str__(self):
        return self.image

    def __repr__(self):
        return self.image

# Oreconfig
print("Loading ore configuration..")

oreconfig = [
    OreConfiguration(
        2,
        1,
        10,
        20,
        Iro
    ),
    
    OreConfiguration(
        2,
        2,
        20,
        40,
        Col
    ),
    
    OreConfiguration(
        5,
        3,
        30,
        100,
        Iro
    ),
    
    OreConfiguration(
        5,
        3,
        50,
        120,
        Col
    ),
    
    OreConfiguration(
        7,
        5,
        100,
        200,
        Iro
    ),
    
    OreConfiguration(
        15,
        13,
        120,
        400,
        Col
    ),
    
    OreConfiguration(
        15,
        10,
        180,
        300,
        Iro
    ),
    
    OreConfiguration(
        25,
        17,
        390,
        700,
        Col
    ),
    
    OreConfiguration(
        25,
        20,
        300,
        700,
        Iro
    ),
    
    OreConfiguration(
        30,
        30,
        700,
        1500,
        Col
    ),
    
    OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    OreConfiguration(
        35,
        50,
        1500,
        2500,
        Iro
    ),
    
    OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    OreConfiguration(
        45,
        60,
        2500,
        4000,
        Iro
    ),
    
    OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    OreConfiguration(
        50,
        100,
        4000,
        6000,
        Iro
    ),
    
    OreConfiguration(
        50,
        100,
        4000,
        6000,
        Col
    ),
    
    OreConfiguration(
        60,
        300,
        6000,
        10000,
        Iro
    ),
    
    OreConfiguration(
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
    Biome(
        "plains",
        50,
        10,
        50,
        [Grs, Drt, Drt, Drt, Drt]
    ),
    
    Biome(
        "desert",
        50,
        10,
        50,
        [Snd, Snd, Snd, Snd, Snd, Snd]
    )
]
"""
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
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
                ore_config=oreconfig
            )
    return [world, newworldtype]"""
        f.write(data)

# Check sprites.py.
print("Checking sprites.py..")
if not api.checkpath(integrisprites):
    with open(integrisprites, "w+") as sprites:
        data = """from ...integri.utilityfolder.blocks import *
from api import Surface

# this is for the inventory don't mind this
black = placeholder_dry("#000000")
filler_black = placeholder_dry("#3F3F3F")

filler_black_row = [filler_black, filler_black, filler_black, filler_black, filler_black, filler_black, filler_black]
filler_inv_row = [black]
black_inv_row = []
inventory_sprite = []
inventory_sprite_slot_coords = []

for i in range(20):
    black_inv_row.append(black)

for i in range(21):
    black_inv_row.append(black)

for i in range(5):
    filler_inv_row += filler_black_row
    filler_inv_row.append(black)

inventory_sprite.append(black_inv_row)
for i in range(5):
    for j in range(7):
        inventory_sprite.append(filler_inv_row)
    inventory_sprite.append(black_inv_row)

for i in range(5):
    for j in range(5):
        inventory_sprite_slot_coords.append(((i * 8) + 1, (j * 8) + 1))

all_sprites_text = f\"\"\"
health_bar
#NONE{"#10121C"*20}
#10121C{"#63101B"*4}{"#99192A"*4}{"#EC273F"*2}#FFA2AC{"#EC273F"*2}#FFA2AC#EC273F{"#FFA2AC"*3}{"#EC273F"*2}
#10121C{"#63101B"*3}{"#99192A"*4}{"#EC273F"*3}#FFA2AC{"#EC273F"*2}#FFA2AC#EC273F#FFA2AC{"#EC273F"*2}#FFA2AC#EC273F
#10121C{"#63101B"*2}{"#99192A"*4}{"#EC273F"*3}{"#FFA2AC"*4}#EC273F#FFA2AC{"#EC273F"*2}#FFA2AC#EC273F
#10121C{"#63101B"*2}{"#99192A"*4}{"#EC273F"*4}#FFA2AC{"#EC273F"*2}#FFA2AC#EC273F{"#FFA2AC"*3}#EC273F{"#EC273F"*2}
#10121C{"#63101B"*2}{"#99192A"*4}{"#EC273F"*4}#FFA2AC{"#EC273F"*2}#FFA2AC#EC273F#FFA2AC{"#EC273F"*4}
#NONE{"#10121C"*20}

Coal
{"#NONE"*7}
{"#NONE"*7}
{"#NONE"*7}
{"#NONE"*2}
#NONE{"#2E2E2E"*2}{"#NONE"*3}
#NONE{"#2E2E2E"*4}{"#NONE"*2}
{"#2E2E2E"*2}{"#141414"*2}{"#2E2E2E"*2}#NONE
#2E2E2E{"#141414"*4}{"#2E2E2E"*2}

Iron ore
{"#474747"*7}
#474747#ABABAB{"#474747"*5}
{"#474747"*5}#ABABAB#474747
{"#474747"*7}
{"474747"*2}#ABABAB{"474747"*4}
{"#474747"*4}#ABABAB{"#474747"*2}
{"#474747"*7}

Stone
#525252#5e5e5e#525252#5e5e5e#525252#383838#383838
#5e5e5e#525252#454545#525252#525252#5e5e5e#454545
#525252#5e5e5e#454545#5e5e5e#5e5e5e#525252#525252
#5e5e5e#383838#525252#525252#454545#525252#383838
#454545#525252#5e5e5e#454545#454545#525252#383838
#383838#454545#525252#383838#454545#454545#525252
#5e5e5e#5e5e5e#454545#5e5e5e#383838#383838#525252

Dirt
#2f5178#304c6e#304c6e#273e59#273e59#1e3045#273e59
#304c6e#2f5178#2f5178#273e59#2f5178#273e59#304c6e
#2f5178#273e59#273e59#2f5178#273e59#304c6e#273e59
#273e59#304c6e#304c6e#1e3045#1e3045#273e59#304c6e
#304c6e#273e59#273e59#2f5178#273e59#273e59#1e3045
#1e3045#273e59#2f5178#304c6e#2f5178#273e59#2f5178
#273e59#2f5178#273e59#273e59#273e59#2f5178#304c6e

Grass
#52b55a#58c261#52b55a#58c261#52b55a#4ba652#58c261
#58c261#4ba652#58c261#52b55a#58c261#52b55a#52b55a
#52b55a#52b55a#4ba652#4ba652#273e59#4ba652#4ba652
#4ba652#304c6e#4ba652#1e3045#1e3045#52b55a#4ba652
#304c6e#273e59#273e59#2f5178#273e59#273e59#58c261
#1e3045#273e59#2f5178#304c6e#2f5178#273e59#2f5178
#273e59#2f5178#273e59#273e59#273e59#2f5178#304c6e

Sand
{f"{"#FFED7C"*7}"*7}

Iron bar
{"#ABABAB"*5}#FFFFFF#ABABAB
#ABABAB#FFFFFF#ABABAB{"#FFFFFF"*4}
{"#ABABAB"*5}#FFFFFF#ABABAB
{"#ABABAB"*7}
{"#ABABAB"*5}#FFFFFF#ABABAB
{"#ABABAB"*7}
{"#ABABAB"*7}

Drt
#2f5178#304c6e#304c6e#273e59#273e59#1e3045#273e59#1e3045
#304c6e#2f5178#2f5178#273e59#2f5178#273e59#304c6e#273e59
#2f5178#273e59#273e59#2f5178#273e59#304c6e#273e59#1e3045
#273e59#304c6e#304c6e#1e3045#1e3045#273e59#304c6e#273e59
#304c6e#273e59#273e59#2f5178#273e59#273e59#1e3045#304c6e
#1e3045#273e59#2f5178#304c6e#2f5178#273e59#2f5178#273e59

Grs
#4ba652#58c261#58c261#4ba652#52b55a#52b55a#58c261#58c261
#52b55a#4ba652#4ba652#52b55a#52b55a#4ba652#52b55a#58c261
#4ba652#273e59#273e59#4ba652#58c261#4ba652#58c261#1e3045
#273e59#304c6e#304c6e#1e3045#1e3045#58c261#304c6e#273e59
#304c6e#273e59#273e59#2f5178#273e59#273e59#1e3045#304c6e
#1e3045#273e59#2f5178#304c6e#2f5178#273e59#2f5178#273e59

Stn
#525252#5e5e5e#525252#5e5e5e#525252#383838#383838#525252
#5e5e5e#525252#454545#525252#525252#5e5e5e#454545#454545
#525252#5e5e5e#454545#5e5e5e#5e5e5e#525252#525252#5e5e5e
#5e5e5e#383838#525252#525252#454545#525252#383838#383838
#454545#525252#5e5e5e#454545#454545#525252#383838#525252
#383838#454545#525252#383838#454545#454545#525252#525252
\"\"\".split("\n")

sprites = {}

# Function to convert hex to RGB
# thanks bing chat
# never even thought of doing it this way, kinda crazy
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

# this i wrote myself
# you can tell because it doesn't have weird python string manipulation int tuple thingmagicks

for line in all_sprites_text:
    current_sprite_name = ""
    current_sprite_contents: list[list[placeholder_dry]] = []
    reading_sprite = False
    
    if line == "":
        if reading_sprite:
            sprites[current_sprite_name] = current_sprite_contents
            reading_sprite = False
        continue
    
    elif "#" not in line:
        if not reading_sprite:
            current_sprite_name = line
            current_sprite_contents.append([])
            reading_sprite = True
        else:
            sprites[current_sprite_name] = current_sprite_contents
            
            current_sprite_name = ""
            current_sprite_contents = []
            reading_sprite = False
    
    elif reading_sprite:
        for hex_code in line.split("#"):
            if hex_code == "NONE":
                current_sprite_contents[-1].append(None)
            else:
                current_sprite_contents[-1].append(hex_to_rgb(f"#{hex_code}"))
            #elif current_sprite_name != "health_bar_full":
            #    current_sprite_contents[-1].append(hex_to_rgb(f"#{hex_code}"))
            #else:
            #    current_sprite_contents.append(f"#{hex_code}")
        current_sprite_contents.append([])


# Now to turn all those arrays into surfaces.
# there is a better way to do this but for readability i want surface creation and the hex interpreter
# to be at different parts of the file.
for key in sprites.keys():
    # i kinda need the health bar to be left as-is
    if current_sprite_name == "health_bar_full":
        continue
    
    # this just checks if it's an item, not a block
    if len(sprites[key]) > 6:
        width = 7
        height = 7
    else:
        width = 8
        height = 6

    new_sprite = Surface((width, height))

    for Y in range(len(sprites[key])):
        
        for X in range(sprites[key][Y]):
            
            new_sprite.set_at((X, Y), sprites[key][Y][X])
    
    sprites[key] = new_sprite
"""
    sprites.write(data)

increment()
increment()

# - Folder Checking finished -

# generateworld function

print("Importing all necessary ingame libraries..")

from gamedata.integri.utilityfolder.blocks import *
from gamedata.integri.utilityfolder.generateworldpackage import *
from gamedata.integri.utilityfolder.sprites import *

increment()

print("Brace for impact, this last 1% might be long!")

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
    if index >= 0 and index2 >= 0:
        try:
            return listt[index][index2]
        except(IndexError):
            return Bdr
    else:
        return Bdr

print("Making function Add If Reachable Placeholder (air_placeholder)")
def air_placeholder(
    space: list[list[api.block]],
    index_1: int,
    index_2 = int
) -> placeholder:
    if index_1 < 0 or index_2 < 0:
        return placeholder(
            "Bdr",
            "#000000",
            0,
            False
        )
    
    try:
        block = space[index_1][index_2]
        return placeholder(
            block.varname,
            block.image,
            0,
            block.passable
        )
    except IndexError:
        return placeholder(
            "Bdr",
            "#000000",
            0,
            False
        )


print("Loading quittime, frames, casting_world and originals..")
quittime = False
frames = 0
casting_world = []
originals = []


print("Loading function framecounter..")
def framecounter():
    global frames
    while not quittime:
        api.wait(1)
        print(f"fps: {frames}")
        frames = 0


print("Loading function applylightingsystem..")
def applylightingsystem(world):
    # Set the top of the world's light level to 15.
    for block in world[0]:
        block.light_level = 15
    
    for timesY in range(2):
        # timesY is approximately how many iterations I expect it to take
        # to apply the lighting system and leave without any lighting glitches.
        # O((n^2) * 2) lmfao
        
        for Y in range(1, len(world)):
            Ylevel = world[Y]
            # Since the light level of the top blocks is already 15, there is
            # no need to apply the lighting system to it.
            lightlevelsaroundblock = []

            for X in range(len(Ylevel)):
                above_block = world[Y - 1][X].light_level
                try:
                    left_block = Ylevel[X - 1].light_level
                except(IndexError):
                    left_block = 0

                try:
                    right_block = Ylevel[X + 1].light_level
                except(IndexError):
                    right_block = 0

                lightlevelsaroundblock.append(above_block)
                lightlevelsaroundblock.append(left_block)
                lightlevelsaroundblock.append(right_block)

                world[Y][X].light_level = api.average(lightlevelsaroundblock)
                world[Y][X].image = api.color_with_light(block.image, block.light_level, 15)

    return world


print("Loading function raycast..")
def raycast(target_X: int, target_Y: int) -> None:
    global casting_world
    global originals
    half_casting_world_size = len(casting_world) // 2
    half_casting_world_size_2 = (half_casting_world_size, half_casting_world_size)
    impassable_hits = 0
    impassable_limit = 5
    
    # readability? who needs that when i have an optimizemaxxing streak?
    for (X, Y) in api.bresenham(half_casting_world_size, half_casting_world_size, target_X, target_Y):
        # You will recieve no comment with this code. Fuck you, I'm tired and I want to get this
        # whole raycasting thing over with.
        original_block = originals[Y][X]
        
        if original_block.passable or (X, Y) == half_casting_world_size_2:
            casting_world[Y][X] = original_block
        
        elif not original_block.passable and not (X, Y) == half_casting_world_size_2 and not impassable_hits >= impassable_limit:
            casting_world[Y][X] = original_block
            impassable_hits += 1
        
        elif not original_block.passable and not (X, Y) == half_casting_world_size_2 and impassable_hits >= impassable_limit:
            casting_world[Y][X] = original_block
            break


#def raycast_4_rays(length_of_display, i):
#    raycast(i, 0)
#    
#    raycast(length_of_display - 1, i)
#    
#    raycast((length_of_display - 1) - i, length_of_display - 1)
#    
#    raycast(0, (length_of_display - 1) - i)


print("Loading function raycast_rays..")
def raycast_rays():
    global casting_world
    length_of_display = len(casting_world)
    
    for i in range(0, length_of_display - 1):
        #Thread(target=raycast_4_rays(length_of_display, i)).start()
        raycast(i, 0)
        
        raycast(length_of_display - 1, i)
        
        raycast((length_of_display - 1) - i, length_of_display - 1)
        
        raycast(0, (length_of_display - 1) - i)


print("Loading function calc_healh_pixel..")
def calc_health_pixel(
    health: int,
    required_health: int
):
    if health >= required_health:
        return True
    else:
        return False


#print("Loading function repeat_pixels..")
#def repeat_pixels(
#    pixels: list[placeholder_dry],
#    repetition_times: list[int]
#):
#    final_list = []
#    
#    for pixel_index in range(len(pixels)):
#        pixel = pixels[pixel_index]
#        for repeat in range(repetition_times[pixel_index]):
#            final_list.append(pixel)
#    
#    return final_list


print("Loading function calculate_health_bar..")
def calculate_health_bar(health: int) -> list[list[placeholder_dry]]:
    """Calculates and gives you a health bar.

    Args:
        health (int): The health of the player.

    Returns:
        list[list[placeholder_dry]]: The health bar.
    """
    black = placeholder_dry("#10121C")
    white = placeholder_dry("#FFFFFF")
    health_bar_full = sprites["health_bar_full"]
    
    health_bar_computed = []
    
    for Y in range(0, 7):
        health_bar_computed.append([])
        
        for X in range(1, 21):
            coords = (X, Y)
            
            color_in_health = health_bar_full.get_at(coords)
            
            if calc_health_pixel(health, abs(5 * (X - 20))):
                # like what the fuck is this formula above me scoob?
                health_bar_computed[-1].append(placeholder_dry(color_in_health))
            else:
                health_bar_computed[-1].append(placeholder_dry((255, 255, 255, 255)))
    
    return health_bar_computed


print("Loading function load_inventory..")
def load_inventory(
    display: list[list],
    inventory: api.inventory
):
    """Loads the 25x25 inventory of the player onto a display.

    Args:
        display (list[list]): The display to load the inventory onto.
        inventory (api.inventory): The inventory to load.

    Returns:
        list[list]: The display after having the inventory loaded on it.
    """
    output = display
    slotvalues = list(inventory.slots.values())
    slotvalues_iterable = range(len(slotvalues))
    
    output = stick_to_display(
        inventory_sprite,
        output,
        (29, 29)
    )
    
    #print(f"slotvalues: {slotvalues}")
    #print(f"len(slotvalues: {len(slotvalues)})")
    
    for slot_index in slotvalues_iterable:
        #print(f"inventory_sprite_slot_coords: {len(inventory_sprite_slot_coords)}")
        #print(f"slot_index: {slot_index}")
        sprite_coord = inventory_sprite_slot_coords[slot_index]
        slot = slotvalues[slot_index]
        
        if slot != None:
            output = stick_to_display(
                sprites[slot],
                output,
                (29 + sprite_coord[0], 29 + sprite_coord[1])
            )
    
    return output


print("Loading function stick_to_display..")
def stick_to_display(
    array: list[list[placeholder_dry]],
    display: list[list],
    starting_XY: tuple
) -> list[list]:
    """Puts an array into a display.

    Args:
        array (list[list[placeholder_dry]]): The array you want to put.
        display (list[list]): The display you want to put into.
        starting_XY (tuple): The X and Y coordinates of the top left pixel of the array.

    Returns:
        list[list]: The display after putting array into it.
    """
    X = starting_XY[0]
    Y = starting_XY[1]
    output = display
    
    for row_index in range(len(array)):
        row = array[row_index]
        for pix_index in range(len(row)):
            pix = row[pix_index]
            if pix != None:
                output[Y + row_index][X + pix_index] = pix
    
    return output


print("Loading function displaythread..")
def displaythread(screen):
    global casting_world
    global originals
    global quittime
    global frames
    global world
    global plr
    while not api.isquit():
        # LET HIM COOK :fire:
        displayoutput = []
        casting_world = []
        #blits_left = []

        #for n in range(worldtype[0]):
        #    cookingdisplayoutput.append([])
        #
        #    for m in range(100):
        #        cookingdisplayoutput[-1].append(air_placeholder(world, plr.position[1] - (n - worldtype[0]), plr.position[0] - (m - 50)))
        #print(f"len(cookingdisplayoutput[0]): {len(cookingdisplayoutput[0])}")
        #displayoutput = applylightingsystem(cookingdisplayoutput)

        # I came up with a math formula to line up player coordinates
        # between cookingdisplayoutput and displayoutput
        # coordinate of player in cookingdisplayoutput =
        # X - (X - (X_radius_around_player + 1))
        
        # Or just use m?? past me was a dumbass

        # this could actually be improved but i'm too lazy to do that
        for n in range(100):
            new_row = []

            for m in range(100):
                new_row.append(air(world, plr.position[1] - (n - 50), plr.position[0] - (m - 50)))
            
            displayoutput.append(new_row)
        
        displayoutput = list(reversed(displayoutput))

        for Y in range(len(displayoutput)):
            new_row = []
            for X in range(len(displayoutput)):
                new_row.append(Bdr)
            casting_world.append(new_row)
        
        originals = displayoutput
        raycast_rays()
        displayoutput = casting_world
        
        health_bar = calculate_health_bar(plr.health)
        displayoutput = stick_to_display(
            health_bar,
            displayoutput,
            (79, 0)
        )
        
        if api.ispressed_key("e"):
            displayoutput = load_inventory(
                displayoutput,
                plr.inventory
            )
        
        # FUCK YOU, I'LL USE MY OWN RENDERING ENGINE RAHHHHHHHH
        # WE RIDE AT DAWWWNNN BITCHEEEEESSSSSSS
        for Y in range(len(displayoutput)):
            Y_blocks = displayoutput[Y]
            
            for X in range(len(Y_blocks)):
                block: api.block = displayoutput[Y][X]
                blockimage = api.Color(block.image)
                
                if not api.reachableindex(sprites, block.varname):
                    api.draw_rectangle(
                        screen,
                        blockimage,
                        X * 8,
                        Y * 6,
                        8,
                        6
                    )
                else:
                    screen.blit(source=sprites[block.varname], dest=(X * 8, Y * 6))
        
        #for surface_data in blits_left:
        #    screen.blit(source=surface_data["surface"], dest=surface_data["coordinates"])
        
        api.update_screen()
        
        # haha fuck the framerate cap
        #api.display(screen, displayoutput, 8, 6)
        #api.wait(1/60) # "60 fps"
        frames += 1
        # How does this work again
        # lmao this shit ain't even CLOSE to 60 fps it runs at *~15*
        # how does this run at ~23 fps
        # the fact it runs at any fps past 10 is a miracle
        # HOW DOES IT KEEP GOING HIGHER EVERY UPDATE I'M NOT EVEN DOING ANYTHING
        # come to think of it this whole thing even working is a miracle



increment()

# - Loading Finished -

# Main Game Loop

while True:
    # Main Menu
    option = None # Currently selected option.
    meant_to_run = False
    saveselected = False
    displaytitle()
    # Present the options and how to select one of them.
    print(Fore.LIGHTBLACK_EX + "Press the number before the option to select it.")
    print(Fore.GREEN +         "                1. Singleplayer                 ")
    print(Fore.BLUE +          "  NOT AVAILABLE 2. Multiplayer                  ")
    print(Fore.YELLOW +        "  NOT AVAILABLE 3. Options                      ")
    print(Fore.RED +           "                4. Quit                         ")
    print()
    
    # Take keybaord input.
    option = api.wait_any()
    
    # Decide what to do with the keyboard input.
    if option == "4":
        break
    
    elif option == "1":
        displaytitle()
        
        # Initialize the save options
        availablesaveoptions = ["1", "2", "3", "4"]
        availabledeletesaveoptions = ["5", "6", "7", "8"]
        saveselected = False
        backtomenu = False

        while not saveselected:
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
            print(Fore.LIGHTBLACK_EX + "                0. Back to Menu." + Style.RESET_ALL)
            
            selectedsave = api.wait_any() # await a key press
            if selectedsave in availabledeletesaveoptions:
                match int(selectedsave):
                    case 5: api.delete("integri\\saves\\" + Saves[0] + ".py"); del Saves[0]
                    case 6: api.delete("integri\\saves\\" + Saves[1] + ".py"); del Saves[1]
                    case 7: api.delete("integri\\saves\\" + Saves[2] + ".py"); del Saves[2]
                    case 8: api.delete("integri\\saves\\" + Saves[3] + ".py"); del Saves[3]
                continue
            elif selectedsave == "0":
                meant_to_run = False
                break
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
                # python stop fucking compiling the save to efficient bytecode just RUN IT
                savename = str(Saves[int(selectedsave) - 1])
                save = import_module(integrisaves + savename)
                plr = save.plr
                if api.reachableindex(plr.inventory.slots, "slot26"):
                    del plr.inventory.slots["slot26"]
                print(plr.inventory.slots)
                world = save.world
                worldtype = save.worldtype
                del save
                print("Success. We will get to work now.")
            
            saveselected = True
            meant_to_run = True

        api.initiatewindow() # Initiate the window so that pygame doesn't go crazy.
        
        if meant_to_run:
            # Initialize a few variables
            screen = api.setres(800, 600)

            displayfunc = Thread(target=displaythread,args=[screen])
            displayfunc.start()
            framecounterfunc = Thread(target=framecounter)
            framecounterfunc.start()

            gravmltp = 0
            holdingW = False
            specialmode = False
            newdata = [world, plr.replace]
            
            # profiling
            #new_casting_world_time = 0
            #reverse_area_time = 0
            #health_bar_time = 0
            #init_vars_time = 0
            #area_grab_time = 0
            #raycast_time = 0
            #display_time = 0
            #hurt_time = True
        while meant_to_run and api.isquit() == False:

            # Player interaction

            # Keys
            wpressed = api.ispressed_key("w")
            apressed = api.ispressed_key("a")
            spressed = api.ispressed_key("s")
            dpressed = api.ispressed_key("d")
            breakmode = api.ispressed_key("shift")
            buildmode = api.ispressed_key("ctrl") # forget this building doesn't work
            
            if breakmode or buildmode:
                specialmode = True
            
            if breakmode and buildmode:
                specialmode = False # fuck you smartass

            # Actions
            
            # by god don't ask me why the controls are flipped for A and D
            # idk why but it must be there for a purpose
            
            # W moving
            if wpressed:
                if not specialmode:
                    newdata = plr.move("w", newdata[0], newdata[1])
                    holdingW = True
                elif breakmode:
                    newdata[0] = plr.breakblock("w", newdata[0], newdata[1], 2)
                elif buildmode:
                    newdata[0] = plr.placeblock("w", newdata[0], distance=2, item_to_block_dict=all_blocks_dict)
            
            # A moving
            if apressed:
                if not specialmode:
                    newdata = plr.move("d", newdata[0], newdata[1])
                    holdingW = True
                elif breakmode:
                    newdata[0] = plr.breakblock("d", newdata[0], newdata[1], 2)
                elif buildmode:
                    newdata[0] = plr.placeblock("d", newdata[0], distance=2, item_to_block_dict=all_blocks_dict)
            
            # S moving
            if spressed:
                if not specialmode:
                    newdata = plr.move("s", newdata[0], newdata[1])
                    holdingW = True
                elif breakmode:
                    newdata[0] = plr.breakblock("s", newdata[0], newdata[1], 2)
                elif buildmode:
                    newdata[0] = plr.placeblock("s", newdata[0], distance=2, item_to_block_dict=all_blocks_dict)
            
            # D moving
            if dpressed:
                if not specialmode:
                    newdata = plr.move("a", newdata[0], newdata[1])
                    holdingW = True
                elif breakmode:
                    newdata[0] = plr.breakblock("a", newdata[0], newdata[1], 2)
                elif buildmode:
                    newdata[0] = plr.placeblock("a", newdata[0], distance=2, item_to_block_dict=all_blocks_dict)

            # Apply Gravity

            if world[plr.position[1] + 1][plr.position[0]].passable:
                gravmltp += 0.05
                if not holdingW:
                    gravmltp += 0.3
            else:
                gravmltp = 0
            
            for i in range(floor(gravmltp)):
                newdata = plr.move("s", newdata[0], newdata[1], 1)

            # Other stuff

            world = newdata[0] # Update display
            plr.replace = newdata[1]
            specialmode = False
            breakmode = False
            holdingW = False # Tell the game the player has not moved up (this is used for gravity in the next tick/update).
            api.wait(1/15) # "15 tps/ups"
        quittime = True
        api.closewindow()

        if meant_to_run:
            print("Saving..")
            world = newdata[0] # Quickly update the world
            plr.replace = newdata[1] # Then update replace
            # May not be 100% accurate as in might be 1 frame behind but that is acceptable
            savegame(savename=savename,world=world,worldtype=worldtype,plr=plr,single=True)
            print("Saved.")
