# Loading

import time
import os
import random
import multiprocessing
from sys import exit as theactualsysexit
try: import stubs
except(ModuleNotFoundError): os.system("pip install stubs"); import stubs
try: from playsound import playsound
except(ModuleNotFoundError): os.system("pip install wheel"); os.system("pip install playsound"); from playsound import playsound
try: import keyboard
except(ModuleNotFoundError): os.system("pip install keyboard"); import keyboard
try: import pygame
except(ModuleNotFoundError): os.system("pip install pygame"); import pygame
from math import floor

# - Misceallanous -

# Strip important files
def stripimportant(downloaded: list[str], importantstuff: list[str]=["api.py","__pycache__","gamedata"]) -> list:
    """Strips stuff out of a list."""
    for i in importantstuff:
        while i in downloaded: downloaded.remove(i)
    return downloaded

# Scale a 2D Array
def scale_2dlist(data: list, extendby: int=2) -> list:
    """Lmao bing chat wrote 99.8% of this
    this function just turns up the resolution of a 2D array
    example:
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    if [extendby] is set to 2, that will become
    data = [
        [1, 1, 2, 2, 3, 3],
        [1, 1, 2, 2, 3, 3],
        [4, 4, 5, 5, 6, 6],
        [4, 4, 5, 5, 6, 6],
        [7, 7, 8, 8, 9, 9],
        [7, 7, 8, 8, 9, 9]
    ]

    Args:
        data (list): 2D Array.
        extendby (int, optional): . Defaults to 1.

    Returns:
        list: the resulting 2D Array. if [extendby] is set to 1, it somehow returns nothing.
    """
    result = []
    for row in data:
        for _ in range(extendby):
            new_row = [item for item in row for _ in range(extendby)]  # Duplicate each item in the row
            result.append(new_row)  # Duplicate each row
            # weird method of adding new lists cuz python stores it weird if i don't do this
    return result

# Internal Functions

# Add "api." if true
def addapiiftrue(addapi: bool) -> str:
    """DISCLAIMER: This is an internal function. It returns "api." if addapi is true, and returns "" if not.

    Args:
        addapi (bool): Should it return "api." or ""?

    Returns:
        str: Either "api." or "".
    """
    if addapi: return "api."
    else: return ""

# Get inventory with strings around slots
def putstringsaroundslots(inventory):
    """DISCLAIMER: This is an internal function. It returns inventory.slots but with double quotes around the slots.

    Args:
        inventory (inventory class): Used to pull slots from.

    Raises:
        ValueError: _description_
        TypeError: _description_

    Returns:
        str: A dict inside a string.
    """
    # Initialize variables.
    slots = inventory.slots
    returner = '{'
    returningkeys = slots.keys()
    returningvalues = slots.values()
    
    # Do the main processing part.
    for slotkeyindex in len(returningkeys) - 1:
        if returningvalues[slotkeyindex] == "":
            # Put empty double quotes if the value is also an empty string.
            # This is done so there isn't a key with no value.
            returner += f'"{returningkeys[slotkeyindex]}": "",'
        elif returningvalues[slotkeyindex].startswith("#"):
            # Put double quotes around the value if it starts with a hashtag.
            # This is done a line isn't commented out.
            returner += f'"{returningkeys[slotkeyindex]}": "{returningvalues(slotkeyindex)}",'
        else:
            # Just put the value there if it makes through none of the checks above.
            returner += f'"{returningkeys[slotkeyindex]}": {returningvalues(slotkeyindex)},'
    
    # Return an ouput.
    returner = returner.removesuffix(",")
    returner += '}'
    return returner

# Install a module

def install(module):
    os.system("pip install " + module)

# Delete a file

def delete(file):
    os.system("del gamedata\\" + file)

# Calculate when the operator is a string.

def calculate(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*" or op == "x":
        return num1 * num2
    elif op == "%":
        return num1 % num2
    elif op == "^":
        return num1 ^ num2
    elif op == "/":
        return num1 / num2

# Clear Screen.

def fullclear():
    os.system("cls")

def clear():
    os.system("cls")
    print("  _          _    _     _      _  ")
    print(" | |        | |  | |    \\ \\   / / ")
    print(" | |        | |  | |     \\ \\ / /  ")
    print(" | |        | |  | |      \\   /   ")
    print(" | |        | |  | |      /   \\   ")
    print(" | |___     | |__| |     / / \\ \\  ")
    print(" |_____|    |______|    /_/   \\_\\ ")
    print("    _______           ________    ")
    print("   |  ___  |         |   _____|   ")
    print("   | |   | |         |  |_____    ")
    print("   | |   | |         |_____   |   ")
    print("   | |___| |          _____|  |   ")
    print("   |_______|         |________|   ")
    print("                                  ")
    
# Wait.

def wait(secs):
    time.sleep(secs)

# - The Checkers -

# Check if one list has an element of the other.

def comparelist(list1, list2):
    for i in list1:
        if i in list2: return True
    return False

# Check for index in list.

def ismore(list, index):
    try: list[index]; return True
    except(IndexError): return False
    except(KeyError): return False

# Check if the string is a math operator.

def isoperator(string):
    operators = ["+", "-", "*", "x", "%", "/"]
    if string in operators: return True
    else: return False

# Check if the variable is a list.

def islist(var):
    if type(var) == list: return True
    else: return False

# Check if the variable is a string.

def isstring(var):
    if type(var) == str: return True
    else: return False

# Check if the string is an integer.

def isint(string):
    try: int(string); return True
    except(ValueError): return False
    except(TypeError): return False

# Check if an index in a list or dictionary exists.

def reachableindex(liste, index):
    if type(liste) == list:
        if isint(index):
            if index < len(liste): return True
            else: return False
        else:
            try: liste.index(index); return True
            except(ValueError): return False
    else:
        try: liste[index]; return True
        except(KeyError): return False

# - Engine -

# Playing audio -
def playaudio(relativepathtofile):
    path = f"{os.path.dirname(__file__)}\\{relativepathtofile}"
    p = multiprocessing.Process(target=playsound, args=[path])
    p.start()
    return p

def playaudioabs(absolutepathtofile):
    p = multiprocessing.Process(target=playsound, args=[absolutepathtofile])
    p.start()
    return p

# To stop the audio, use p.terminate()

# Display -

# Set Display Resolution among some other things.
def setres(width=800, height=600, flags=0, depth=0, display=0, vsync=0):
    # Width = width of the screen
    # Height = height of the screen
    # I honestly have no idea what flags, depth, and display do.
    # Vsync = Vertical Sync, prevents screen tearing but does take additional GPU resources.
    screen = pygame.display.set_mode((width, height), flags, depth, display, vsync)
    return screen

# The Main Function that puts shit on screen.
# Takes only 8 lines excluding empty lines or lines with only comment in them.

def display(screen, newscreen, widthofeachblock, heightofeachblock):
    # screen is obtained through api.setres
    # newscreen is a list of lists, with higher indexes more at the bottom of the map.
    # widthofeachblock and heightofeachblock are self-explanatory.
    Y = 0
    for Ycoord in newscreen: # Selects a list from newscreen.
        X = 0 # Set X to 0 for use in a new Y axis.
        for block in Ycoord: # Selects a block in said list,
            # Then it draws the block on screen with it's color being what comes from its __repr__ function.
            # the rest is self-explanatory.
            block = str(block) # Turn it into <type 'str'> instead of <class 'api.block'> or smth
            pygame.draw.rect(screen, pygame.Color(block), (X, Y, widthofeachblock, heightofeachblock))
            X += widthofeachblock # Add widthofeachblock to X. Why?
            # or else it would try to overlap all the colors on the same X coordinates.
        Y += heightofeachblock # Add heightofeachblock to Y. Why?
        # or else it would try to overlap all the colors on the same Y coordinates.
    pygame.display.flip() # Display the newly drawn screen on the window.

# Keyboard functions

# Any key -
# Pause thread until any key is pressed.
def wait_any(): return keyboard.read_key()

# Check if any key is currently being pressed.
def ispressed_any(): return keyboard.on_press()

# Check if any key has just been released.
def isreleased_any(): return keyboard.on_release()

# Specific key -
# Pause thread until key is pressed.
def wait_key(key): return keyboard.wait(key)

# Check if key is currently being pressed.
def ispressed_key(key): return keyboard.is_pressed(key)

# Check if key has just been released.
def isreleased_key(key): return keyboard.on_release_key(key)

# The X -
# Check if the user clicked the X on the top-right of the window.
def isquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: return True
    return False

# Close the window
def closewindow():
    pygame.quit()

# Close the entire program
def sysexit():
    theactualsysexit()

# Objects -

# Inventory
class inventory:
    def __init__(self, slotnum=10, slotdata=None, selectedindex=None):
        if type(slotnum) == int or isint(slotnum):
            slotnum = int(slotnum)
            if slotnum > 0:
                slots = {}
                if slotdata != None:
                    for i in slotdata:
                        slots["slot" + str(list(slotdata.keys()).index(i))] = slotdata[i]
                for i in range(slotnum):
                    if ismore(slots, "slot" + str(i + 1)) == False:
                        slots["slot" + str(i + 1)] = None
                self.slots = slots
                if selectedindex == None:
                    self.selected = slots["slot1"]
                    self.selectedindex = "slot1"
                else:
                    self.selected = slots[selectedindex]
                    self.selectedindex = selectedindex
                self.slotnum = slotnum
                self.type = "inventory"
            else: raise ValueError
        else: raise TypeError
    
    # Select a slot in the inventory for use
    def select(self, selectnum):
        self.selected = self.slots["slot" + str(selectnum)]
    
    # Clear the inventory of items
    def clearinventory(self):
        for i in self.slots:
            self.slots[i] = None
        self.selected = self.slots["slot1"]
    
    # Shrink the inventory starting from the end
    def shrinkinventory(self, slotnum):
        for i in range(slotnum):
            del list(self.slots)[-1]
            self.slotnum -= 1
    
    # Make the inventory bigger
    def enlargeinventory(self, slotnum, slotdata):
        lastkey = str(list(self.slots)[-1])
        lastkey = lastkey.split()
        current = int(lastkey[-1])
        for i in range(slotnum):
            self.slots["slot" + str(current + 1)] = slotdata[i]
            current += 1
            self.slotnum += 1

    def __str__(self):
        return self.slots

# Block
class block:
    def __init__(self, varname: str="Stn", image: str='#000000', passable: bool=False, breakablebytool: bool=True, droptoolvalue: int=2, drop='Stone', falling: bool=False):
        """Exactly what the name says. You can also call it a tile.

            varname: What variable is this block called? Used for turntoblock() and turnarraytoblocks().

            image: What the display() function will use. Is usually a hex code.

            passable: Can it be passed through by entities?

            breakablebytool: Can it be broken by an entity weilding a tool?

            droptoolvalue: What level does that tool have to be?

            drop: What does the entity gain in its inventory upon breaking the block?

            falling: Is the block not immune to gravity? Use this so you can just do this and it will move if this value is set to True:
                for block in world: block.move(arguments)
        """
        self.varname = varname
        self.image = image
        self.passable = passable
        self.breakablebytool = breakablebytool
        self.droptoolvalue = droptoolvalue
        self.drop = drop
        self.falling = falling
        self.type = "block"
    
    def __str__(self):
        return self.image
    
    def __repr__(self):
        return self.image
#        return f"api.block(image=\"{self.image}\",passable={str(self.passable)},breakablebytool={str(self.breakablebytool)},droptoolvalue={str(self.droptoolvalue)},drop={str(self.drop)},falling={str(self.falling)})"

# Entity
class entity:
    def __init__(self, varname="plr", character="#000000", maxhealth: int=100, health: int=100, armor: int=0, attack: int=5, defense: int=5, speed: int=1, position: list=[2,2], replace: block=block(), inventory: inventory=inventory(), dead: bool=False, deffactor: float=0.5, atkfactor: float=0.5, reach: int=1, handvalue: int=1):
        """Exactly what the name is. Can be used to make a player character.
        Methods:
            breakblock()
            move()
            hurt()
            heal()
        Hover over them after typing them out for a description of what they do and their inputs.
        """
        self.varname = varname
        self.character = character
        self.maxhealth = maxhealth
        self.health = health
        self.armor = armor
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = inventory
        self.position = position
        self.replace = replace
        self.dead = dead
        self.deffactor = deffactor
        self.atkfactor = atkfactor
        self.type = "entity"
        self.passable = False
        self.reach = reach
        self.handvalue = handvalue

    # Break a block
    def breakblock(self, direction: str, data:list, replace: block, distance: int=0) -> list:
        """Break a block a certain distance away from the entity. Will not break passable blocks, blocks which have "breakablebytool" set to False, or blocks when there is no free slot in the inventory.

        Args:
            direction (str): What direction the entity is attempting to break a block in. Can be "w", "a", "s", or "d". If you don't know what either of those options do, that's enough grass touching for you.
            data (list): The world around the entity.
            replace (block class): What will be left in the space the entity once was.
            distance (int, optional): How far away the block it is attempting to break is. Defaults to the reach of the entity.

        Returns:
            2D Array: The world after the entity has broken that block in front of it.
        """
        
        # Load -
        
        direction = str.lower(direction)
        dx, dy = 0, 0
        if distance != 0: usedistance = distance
        else: usedistance = self.reach
        match direction:
            case "w": dy -= usedistance
            case "a": dx -= usedistance
            case "s": dy += usedistance
            case "d": dx += usedistance
        
        # Main -
        
        print("main!")
        if data[self.position[1] + dy][self.position[0] + dx].passable == False:
            print("made it")
            if self.handvalue <= data[self.position[1] + dy][self.position[0] + dx].droptoolvalue:
                if self.inventory.selected == None:
                    self.inventory.slots[self.inventory.selectedindex] = data[self.position[1] + dy][self.position[0] + dx]
                    print("succ!")
                    data[self.position[1] + dy][self.position[0] + dx] = replace
                else:
                    for i in range(self.inventory.slotnum):
                        print("i in range")
                        if self.inventory.slots["slot" + str(i + 1)] == None:
                            self.inventory.slots["slot" + str(i + 1)] = data[self.position[1] + dy][self.position[0] + dx]
                            data[self.position[1] + dy][self.position[0] + dx] = replace
                            break

        # Return -
        
        return data

    # Move the entity
    def move(self, direction: str, data: list, replace: block, speed: int=0) -> list:
        """Move the entity. What did you think? Also great for gravity.

        Args:
            direction (str): Can be "w", "a", "s", or "d". If you don't know what either of those options do, stop living under the mariana trench.
            data (2D Array): The world around the entity.
            replace (block class): What will be left in the space the entity once was.
            speed (int, optional): How many blocks forward should the entity go? Defaults to the speed of the entity.

        Returns:
            list: [0] is the world after the entity has moved, and [1] is the block before the entity moved to it.
        """
        
        # Load -
        
        direction = str.lower(direction)
        final2 = replace # lol i don't know why, this is a pretty old line of code
        dy, dx = 0, 0 # difference Y, difference X
        if speed != 0: usespeed = speed
        else: usespeed = self.speed
        match direction:
            case "w": dy -= 1
            case "a": dx -= 1
            case "s": dy += 1
            case "d": dx += 1
        
        # Main -
        
        # [i] doesn't matter here, we're just tryna do stuff multiple times
        # oh, you wanna teleport? just do entity.position[newX, newY] or something ffs
        for i in range(usespeed):
            # Idk how I would even begin to comment this
            if reachableindex(data, self.position[1] + dy) and reachableindex(data[self.position[1]], self.position[0] + dx) and self.position[1] + dy > -1 and self.position[0] + dx > -1:
                if data[self.position[1] + dy][self.position[0] + dx].passable:
                    data[self.position[1]][self.position[0]] = replace
                    final2 = data[self.position[1] + dy][self.position[0] + dx]
                    data[self.position[1] + dy][self.position[0] + dx] = self
                    self.position[1] += dy
                    self.position[0] += dx
            
        # Return -
        
        return [data, final2]
    
    # Hurt the entity
    def hurt(self, amount: int) -> bool:
        """Subtract a specific amount of health from the entity. Takes defense and armor into account. Also declares the entity dead if health is 0. Returns a bool for if the entity is dead or not."""
        self.health -= (amount - (self.defense * self.deffactor) - self.armor)
        if self.health <= 0:
            self.death = True
            return self.death
        else: return self.death
    
    # Heal the entity
    def heal(self, amount: int) -> bool:
        """Add a specific amount of health to the entity. Also declares the entity not dead anymore if health is above 0. Returns a bool for if the entity is dead or not."""
        self.health += amount
        if self.health > self.maxhealth:
            while self.health > self.maxhealth:
                self.health -= 1
        if self.health > 0: self.dead = False
        return self.dead
    
    def __str__(self):
        return self.character
    
    def __repr__(self):
        return self.character

# World Generation -

def generate(width: int=400,height=100,biomes: list=[],Air: block=block(image='#FFFFFF',passable=True,breakablebytool=False,droptoolvalue=0,drop='Air',falling=False),Stn: block=block(image="#888888"),Bedrock: block=block(image="#111111"),limit: list=(2,98),oreconfig: dict={},originalYY: int=None,oreeverywhere: bool=False,mountainlikelihood: int=7,averagesteepness: int=40,averagelength: int=20,canyonlikelihood: int=4,averagesteepnessofcanyon: int=30,averagelengthofcanyon: int=20,logging: bool=True):
    """Here it is. The absolute MAX I can go to. THE EPITOME OF MY LABOUR!!
    
    this took hours of my life.
    i'm doing this for free.
    nobody will ever see this.
    i could've done other things with my time.
    
    Summary:

    Args:
        width (int, optional): The width of the world. Defaults to 400.
        height (int, optional): The height of the world. Defaults to 100.
        biomes (list, NOT optional): Biomes. Define minimum size and maximum size with the first and second indexes. Randomly chosen. Example: [[10, 30, Grs, Grs, Drt, Drt],[10, 30, Snd, Snd, Snd, Sndst]] Defaults to None.
        Air (block, optional): The thing that permeates open spaces. Defaults to "Air".
        Stn (block, optional): The thing that permeates everything below the ground. Defaults to "Stn".
        Bedrock (block, optional): Seperates all entities from the endless void below. Defaults to "Bdr".
        limit (tuple, optional): Prevents world generation indexes above the first index of this list and below the second index of this list. Keep in mind that Y levels are reversed, so being very high up = being at a very low Y level, and being deep underground = being at a high Y level. Defaults to None.
        oreconfig (list, optional): {"iron": 50, 10, 40, IronOre}: in this configuration, the block known as "IronOre" has a 1/50th (2%) chance of spawning between 10 and 40 blocks below the top solid block. If left alone it will default to None and the generator will pick a top solid block for you.
        originalYY (int, optional): Where is the original top solid block? Excellent for chunk building, allows for chunks connecting. Defaults to None.
        oreeverywhere (bool, optional): Should ore be placed regardless of the top solid block? Excellent for making Underground chunks. Defaults to False.
        mountainlikelihood (int, optional): How likely are mountains to spawn? calculates as "if random.randint(1, 100) <= mountainlikelihood" and if that results in True, turns on Mountain generation. Should NOT be over 100. Defaults to 7%.
        averagesteepness (int, optional): When mountain drive is on, how likely should it be that the next block is above the previous block? Defaults to 40%.
        averagelength (int, optional): How long should a mountain drive last? Defaults to 20.
        canyonlikelihood (int, optional): mountainlikelihood but for canyons. Defaults to 4%.
        averagesteepnessofcanyon (int, optional): averagesteepness but for canyons. Defaults to 30%.
        averagelengthofcanyon (int, optional): averagelength but for canyons. Defaults to 20.
        logging (bool, optional): Log whatever it's generating right now? gives the player something to look at while waiting for the world to load.

    Returns:
        A 2D Array. This is your 2D world.
    """
    # Air = literally the air, the thing that permeates open spaces.
    # Stn = the thing that permeates closed spaces underground.
    # Bedrock = the bottom layer of the world that separates all entities from the void.
    # biomes = biomes, the first index should be the minimum size of the biome and the second should be the maximum size of the biome. For example:
    # biomes = [
    #    [10, 30, Grs, Grs, Drt, Drt],
    #    [10, 30, Snd, Snd, Snd, Sndst]
    #]
    
    # - Variable Checking -
    
    if logging: print("Checkin' Variables.")
    
    # Select the first biome
    if biomes == []: print("HEY! YOU FORGOT TO GIVE ME ACTUAL BIOMES!!\n[BIOMES] IS LITERALLY JUST A BLANK LIST!"); ValueError()
    uncbiome = random.choice(biomes)
    if mountainlikelihood >= 100: print("HEY! MOUNTAINLIKELIHOOD SHOULD NOT BE OVER 100!!"); ValueError()
    
    # - Create the initial space -
    
    if logging: print("Initial Space time!")
    space = {} # Create the empty world
    for ylevel in range(height): # For every number in height,
        space["y" + str(ylevel + 1)] = [] # Add a new Ylevel in "space",
        if logging: print("Oooo, that's nice, a new Y level.")
        for xlevel in range(width): # And then for every number in width,
            if ylevel != range(height)[-1]: # If it's not at bedrock,
                space["y" + str(ylevel + 1)].append(Air) # Then put Air there.
            else: # If it is at bedrock level,
                space["y" + str(ylevel + 1)].append(Bedrock) # Put Bedrock there.
    if logging: print("Initial space time over.")

    # - Add blocks (finally use biomes) - 
    
    # Initalize some variables  
    
    if logging: print("Just initializing variables now!")
    
    # Check limit
    if limit == None:
        limit = [5, height + 1]

    if logging: print("Wow, limit check done.")
    
    # The top solid layer of the world
    if originalYY == None:
        if limit[0] == 0:
            originalY = random.randint(limit[0] + 1,limit[1])
        else:
            originalY = random.randint(limit[0],limit[1])
    else:
        originalY = originalYY
    
    if logging: print("Original Ys are done!")
    
    # [Y] is used for biomes, to generate things below the top layer.
    Y = originalY
    X = 0
    # Used later for structure and ore generation.
    # It means "Top layer", not "To player".
    toplayer = []
    toplayer.append([originalY, X])
    biome = []
    for i in uncbiome:
        biome.append(i)
    minim = biome[0]
    maxim = biome[1]
    del biome[0] # Delete the minimum biome size FROM [BIOME]
    del biome[0] # Delete the maximum biome size FROM [BIOME]
    biomelength = 1
    internalmaximum = random.randint(minim, maxim) # Set a random internal maximum biome size FOR THIS BIOME ONLY. Allows for varying biome sizes.
    heightlimit = 0
    # First initial layer
    space["y" + str(Y)][X] = biome[0]
    
    if logging: print("Lots of variable initalization is done!")
    
    mountaindrive = False
    canyondrive = False
    totallength = 0
    totallengthofcanyon = 0
    length = random.randint(averagelength - floor(averagelength / 2 / 2), averagelength + floor(averagelength / 2 / 2))
    lengthofcanyon = random.randint(averagelengthofcanyon - floor(averagelengthofcanyon / 2 / 2), averagelengthofcanyon + floor(averagelengthofcanyon / 2 / 2))

    if logging: print("Mountains and Canyons: Loaded!"); print("Now it's time for actual biome generation.")
    
    for i in range(width):

        for i in range(height):
            # This comment wall was just a discord message simplifying this code for some other guy, who then suggested I add it to the actual code.
            # I added so many checks for [Y], the [heightlimit], and the [Bedrock] level because it somehow kept being there which is weird ash.
            # Also, no, it's not for figuring out where [Bedrock] is depending on the [biome],
            # it's for generating layers depending on the [biome].
            # The [Bedrock] layer is always at the bottom of the [space].
            # [biomes] is a list that contains lists which are the actual biomes. [biome] is randomly picked and a random number is chosen between its max length and minimum length.
            # After that, let's say [biome] is ["Dirt", "Dirt", "Dirtier Dirt"].
            # This means that every generated [Y] level while that [biome] is active will look like [Dirt] on top, [Dirt] at the second layer, then [Dirtier Dirt] at the third.
            # After that, it's all [Stn] and maybe some ores until the [Bedrock] layer.
            if Y == heightlimit:
                Y += 1
            elif heightlimit > Y:
                Y = abs(Y)
                Y += 1
            elif Y >= height: Y = height - 1
            if (i - 1) >= 0 and space["y" + str(Y)][X] != Bedrock: # If Y is higher than or equal to 0 and the currently selected Block isn't Bedrock.
                if reachableindex(biome, i - 1):
                    space["y" + str(Y)][X] = biome[i - 1] # If [biome] hasn't ran out, apply the latest layer.
                elif reachableindex(biome, i - 1) == False:
                    space["y" + str(Y)][X] = Stn # Otherwise, make the block Stone.
                if Y < height: Y += 1 # If Y is not at the Bedrock layer, increase it.
        if logging: print("Y problems sorted.")
        # nextplace can be one of three values chosen randomly: 1, 2, and 3.
        # No matter what value nextplace is, X will always increase as long as it doesn't surpass width while doing so.
        # Also do  stuff with mountains and canyons.
        if logging: print("More variables! Yay!")
        above = 1
        below = 3
        if logging: print("Entering the territory of mountains and canyons..")
        if random.randint(1, 100) <= mountainlikelihood and canyondrive != True:
            mountaindrive = True
            if logging: print("MOUNTAIN.. DRIVE!!")
        if random.randint(1, 100) <= canyonlikelihood and mountaindrive != True:
            canyondrive = True
            if logging: print("CANYON.. DRIVE!!")
        if mountaindrive == True:
            if logging: print(f"Total length of the current mountain? oh, that's {totallength}")
            if random.randint(1, 100) <= averagesteepness: 
                if totallength < floor(length / 2): below -= 1
                else: above += 1
                if totallength >= length:
                    if logging: print("Mountain Drive.. Off!")
                    mountaindrive = False
            totallength += 1
        elif canyondrive == True:
            if logging: print(f"Yo, want the total length of the current canyon? No? screw you, it's {totallengthofcanyon}")
            if random.randint(1, 100) <= averagesteepnessofcanyon:
                if totallengthofcanyon < floor(lengthofcanyon / 2): above += 1
                else: below -= 1
                if totallengthofcanyon >= lengthofcanyon:
                    if logging: print("Canyon Drive.. Off!")
                    canyondrive = False
            totallengthofcanyon += 1
        if mountaindrive == False and totallength != 0: totallength = 0
        elif canyondrive == False and totallengthofcanyon != 0: totallengthofcanyon = 0
        if originalY + 1 < limit[0] or originalY + 1 < 1:
            if logging: print("Whoops, hit the height limit.")
            above += 1
        if originalY - 1 > limit[1] or originalY - 1 > (height - 1):
            if logging: print("Oh no, that's too low.")
            below -= 1
        
        try: nextplace = random.randint(above,below)
        except(ValueError): nextplace = 2
        
        if logging: print("Mountain'n'Canyon work done. Moving on to next place work.")
        if X < width - 1:
            if nextplace == 1: # If nextplace is equal to 1, the block placed in the next X coord's Y coord will be higher than the last X coord block's Y coord.
                originalY -= 1
                X += 1
            elif nextplace == 2: # If nextplace is equal to 2, the block placed in the next X coord's Y coord will be the same as the last X coord block's Y coord.
                X += 1
            elif nextplace == 3 : # If nextplace is equal to 3, the block placed in the next X coord's Y coord will be lower than the last X coord block's Y coord.
                originalY += 1
                X += 1
            Y = originalY # Set Y to the top solid block.
                # All of this is code jargon for "If nextplace = 1, go up a block.
                # If nextplace = 2, stay at the same height.
                # If nextplace = 3, go down a block.
                # Otherwise select a different value for nextplace.
                # Then start generating blocks from the top to the bottom."
        toplayer.append([originalY, X])
        if logging: print("Added to top layer.")
        biomelength += 1
        if logging: print("Added to biome length.")
        # Determine if it's time to switch up the biome
        if biomelength > internalmaximum:
            # If so, set some variables to some stuff and pick a new biome
            uncbiome = random.choice(biomes)
            biome = []
            for i in uncbiome:
                biome.append(i)
            minim = biome[0]
            maxim = biome[1]
            del biome[0]
            del biome[0]
            biomelength = 1
            internalmaximum = random.randint(minim, maxim)
            if logging: print("Did some weird shit with biome variables.")
    
    if logging: print("Wow, all that done. Now for Ores..")
    
    # Ore and Structure Generation

    # Ore -
    if oreconfig != {}:
        if logging: print("Looks like they gave us Ores.")
        if oreeverywhere == False:
            if logging: print("Below top block!")
            for topblock in toplayer:
                if logging: print("Next topblock!")
                for ore in list(oreconfig.values()):
                    if logging: print("Next ore, bruh.")
            
                    spawnchance = random.randint(1, ore[0])

                    if spawnchance == 1 and reachableindex(space,"y" + str(topblock[0] + ore[1])):
                        if ore[2] < height: area = random.randint(ore[1], ore[2])
                        elif ore[2] >= height:
                            if ore[1] < height: area = random.randint(ore[1], height - 1)
                            elif ore[1] >= height: pass
                        spawnlocation = topblock[0] + area
                        if spawnlocation >= height: spawnlocation = height - 1
                        if reachableindex(list(oreconfig.values()), ore):
                            space["y" + str(spawnlocation)][topblock[1]] = list(oreconfig.values())[list(oreconfig.values()).index(ore)][3]
                            if logging: print("Yay, we added an ore!")
                    else:
                        if logging: print("Oh no, no ore!")
        elif oreeverywhere == True:
            if logging: print("We don't care where top block is now, time for ores.")
            data = list(space.values())
            for ylevel in data:
                if logging: print("Next ylevel!")
                for xlevel in ylevel:
                    if logging: print("Next xlevel!")
                    for ore in list(oreconfig.values()):
                        if logging: print("Next ore!")
                        spawnchance = random.randint(1, ore[0])

                        if spawnchance == 1:
                            area = random.randint(ore[1], ore[2])
                            if reachableindex(space,"y" + str(area)):
                                if area >= height:
                                    while area >= height: spawnlocation -= 1
                                if reachableindex(ylevel, xlevel):
                                    space["y" + str(area)][ylevel.index(xlevel)] = list(oreconfig.values())[list(oreconfig.values()).index(ore)][3]
                                    if logging: print("Yay, ore added!")
                        else:
                            if logging: print("Oh no, no ore added!")
    
    # FINALLY return the world.
    if logging: print("Alright, time to give you this world. Enjoy.")
    return list(space.values())

# Saving -
def turntoblock(block: block=block(), addapi: bool=True) -> str:
    """Do you also hate that you can't just put "world = {world}" to save because it creates those pesky hashtags? here's a fix. It's useful for saving entities as they were in the world.

    Args:
        block (block, optional): Toss in a block. Defaults to block().
        addapi (bool, optional): Adds "api." before any function used in the api if true. Defaults to True.

    Returns:
        str: Out comes something like "api.block(image=)" or "api.entity(character=)".
    """
    if block.type == "block":
        return f'{addapiiftrue(addapi=addapi)}block(varname={block.varname},image={block.image},passable={block.passable},breakablebytool={block.breakablebytool},droptoolvalue={block.droptoolvalue},drop={block.drop},falling={block.falling})'
    elif block.type == "entity":
        return f'{addapiiftrue(addapi=addapi)}entity(varname={block.varname},character={block.character},maxhealth={block.maxhealth},health={block.health},armor={block.armor},attack={block.attack},defense={block.defense},speed={block.speed},position={block.position},replace={block.replace.varname},inventory={addapiiftrue(addapi=addapi)}inventory(slotnum={block.inventory.slotnum},slotdata={putstringsaroundslots(block.inventory.slots)},selectedindex="{block.inventory.selectedindex}"),dead={block.dead},deffactor={block.deffactor},atkfactor={block.atkfactor},reach={block.reach},handvalue={block.handvalue})'

def turnarraytoblocks(arrayofblocks: list=[[block()], [block()]]) -> list:
    """turntoblock() but applies to entire 2D Arrays.

    Args:
        listofblocks (list, optional): Toss in a 2D Array full of blocks. Defaults to [[block()], [block()]].

    Returns:
        list: Transforms every block in the list to its varname variable.
    """
    returning = []
    returner = []
    for YLevel in arrayofblocks:
        for block in YLevel: returner.append(block.varname)
        returning.append(returner)
        returner = []
    return returning

# Initiate an actual window to display stuff.
def initiatewindow():
    pygame.init()

multiprocessing.freeze_support()
