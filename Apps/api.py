# Loading

import time
import os
import random
import multiprocessing
try: from playsound import playsound
except(ModuleNotFoundError): os.system("pip install playsound"); from playsound import playsound
try: import keyboard
except(ModuleNotFoundError): os.system("pip install keyboard"); import keyboard
try: import pygame
except(ModuleNotFoundError): os.system("pip install pygame"); import pygame

# - Misceallanous -

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
    print(" | |        | |  | |    \ \   / / ")
    print(" | |        | |  | |     \ \ / /  ")
    print(" | |        | |  | |      \   /   ")
    print(" | |        | |  | |      /   \   ")
    print(" | |___     | |__| |     / / \ \  ")
    print(" |_____|    |______|    /_/   \_\ ")
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
    path = f"{os.path.dirname(__file__)}{relativepathtofile}"
    p = multiprocessing.Process(target=playsound, args=[path])
    p.start()
    return p
# To stop it, use p.terminate()

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
        for Xcoord in Ycoord: # Selects a block in said list.
            # Draws the block on screen,
            # with it's color being what comes from its __repr__ function,
            # the rest is self-explanatory.
            Xcoord = str(Xcoord) # Turn it into <type 'str'> instead of <class 'api.block'> or smth
            pygame.draw.rect(screen, pygame.Color(Xcoord), (X, Y, widthofeachblock, heightofeachblock))
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
                        slots["slot" + str(list(slotdata.values()).index(i))] = slotdata[i]
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

# Player
class player:
    def __init__(self, character='Plr', maxhealth=100, health=100, armor=0, attack=5, defense=5, speed=1, position=[2,2], inventory=inventory(), dead=False, deffactor=0.5, atkfactor=0.5):
        self.character = character
        self.maxhealth = maxhealth
        self.health = health
        self.armor = armor
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = inventory
        self.position = position
        self.dead = dead
        self.deffactor = deffactor
        self.atkfactor = atkfactor
        self.type = "player"
        self.passable = False

    # Move the player
    def move(self, direction, data, replace, speed=None):
        
        # Load -
        
        X = self.position[0]
        Y = self.position[1]
        Z = data[self.position[1]]
        final2 = replace
        direction = str.lower(direction)
        aboveplayer = None
        westplayer = None
        belowplayer = None
        eastplayer = None
        currentpos = Z[X]
        if reachableindex(data, self.position[1] - 1):
            aboveplayer = data[self.position[1] - 1]
        if reachableindex(Z, self.position[0] + 1):
            westplayer = Z[self.position[0] + 1]
        if reachableindex(data, self.position[1] + 1):
            belowplayer = data[self.position[1] + 1]
        if reachableindex(Z, self.position[0] - 1):
            eastplayer = Z[self.position[0] - 1]
        if speed != None:
            usespeed = speed
        else:
            usespeed = self.speed
        
        # Main -
        
        for i in range(usespeed):
            if direction == "w" and aboveplayer != None:
                if aboveplayer[self.position[0]].passable:
                    self.position[1] -= 1
                    currentpos = replace
                    final2 = aboveplayer[self.position[0]]
                    aboveplayer[self.position[0]] = self
            elif direction == "a" and westplayer != None:
                if westplayer.passable:
                    self.position[0] -= 1
                    currentpos = replace
                    final2 = westplayer
                    westplayer = self
            elif direction == "s" and belowplayer[self.position[0]] != None:
                if belowplayer[self.position[0]].passable:
                    self.position[1] += 1
                    currentpos = replace
                    final2 = belowplayer[self.position[0]]
                    belowplayer[self.position[0]] = self
            elif direction == "d" and eastplayer != None:
                if eastplayer.passable:
                    self.position[0] += 1
                    currentpos = replace
                    final2 = eastplayer
                    eastplayer = self
            
        # Return -
            
            data[self.position[1]] = Z
            data[self.position[1] + 1] = belowplayer
            data[self.position[1] - 1] = aboveplayer
            Z[self.position[0] - 1] = eastplayer
            Z[self.position[0] + 1] = westplayer
            Z[self.position[0]] = currentpos
        
        return [data, final2]
    
    # Hurt the player
    def hurt(self, amount):
        self.health -= (amount - (self.defense / self.deffactor) - (self.armor / self.armfactor))
        if self.health <= 0:
            self.death = True
            return self.death
        else: return self.death
    
    # Heal the player
    def heal(self, amount):
        self.health += amount
        if self.health > self.maxhealth:
            while self.health > self.maxhealth:
                self.health -= 1
    
    def __str__(self):
        return self.character
    
    def __repr__(self):
        return self.character

# Block
class block:
    def __init__(self, image='  ', passable=False, breakablebytool=True, droptoolvalue=2, drop='Stone', falling=False):
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

# World Generation -

def generate(width=30,height=20,config=None,Air="Air",Stn="Stn",Bedrock="Bdr",limit=None,oreconfig=None,originalYY=None,oreeverywhere=False):
    # Air = literally the air, the thing that permeates open spaces.
    # Stn = the thing that permeates closed spaces underground.
    # Bedrock = the bottom layer of the world that separates the player from the void.
    # config = Layers, e.g. if there should be two layers of dirt at the top then one layer of Crs, then
    # config should be [Drt,Drt,Crs] provided Drt and Crs are variables.
    
    # - Create the initial space -
    
    space = {} # Create the empty world
    for ylevel in range(height): # For every number in height,
        space["y" + str(ylevel + 1)] = [] # Add a new Ylevel in "space",
        for xlevel in range(width): # And then for every number in width,
            if ylevel != range(height)[-1]: # If it's not at bedrock,
                space["y" + str(ylevel + 1)].append(Air) # Then put Air there.
            else: # If it is at bedrock level,
                space["y" + str(ylevel + 1)].append(Bedrock) # Put Bedrock there.

    # - Add blocks (finally use config) -
    
    # Check limit
    if limit == None:
        limit = [5, height + 1]
    
    # The top solid layer of the world
    if originalYY == None:
        if limit[0] == 0:
            originalY = random.randint(limit[0] + 1,limit[1])
        else:
            originalY = random.randint(limit[0],limit[1])
    else:
        originalY = originalYY
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
    
    # Ore and Structure Generation

    # Ore -
    if oreconfig != None:
        if oreeverywhere == False:
            for n in toplayer:
                for i in list(oreconfig.values()):
            
                    spawnchance = random.randint(1, i[0])

                    if spawnchance == 1 and reachableindex(space,"y" + str(n[0] + i[1])):
                        area = random.randint(i[1], i[2])
                        carea = n[0] + area
                        if carea >= height:
                            while carea >= height: carea -= 1
                        if reachableindex(list(oreconfig.values()), i):
                            space["y" + str(carea)][n[1]] = list(oreconfig.values())[list(oreconfig.values()).index(i)][3]
        elif oreeverywhere == True:
            spacevalues = list(space.values())
            for x in spacevalues:
                for n in x:
                    for i in list(oreconfig.values()):
                        spawnchance = random.randint(1, i[0])

                        if spawnchance == 1:
                            area = random.randint(i[1], i[2])
                            if reachableindex(space,"y" + str(area)):
                                area
                                if area >= height:
                                    while area >= height: carea -= 1
                                if reachableindex(x, n):
                                    space["y" + str(area)][x.index(n)] = list(oreconfig.values())[list(oreconfig.values()).index(i)][3]
    
    # FINALLY return the world.
    
    return list(space.values())

# Initiate an actual window to display stuff.
def initiatewindow():
    pygame.init()

multiprocessing.freeze_support()
