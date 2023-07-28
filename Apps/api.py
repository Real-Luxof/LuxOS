<<<<<<< HEAD
# Loading

import time
import os
import random
from threading import Thread, Event
try: import simple_colors
except(ModuleNotFoundError): os.system("pip install simple_colors"); import simple_colors
try: import pyaudio
except(ModuleNotFoundError): os.system("pip install pyaudio"); import pyaudio
try: import wave
except(ModuleNotFoundError): os.system("pip install wave"); import wave

# - Misceallanous -

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

# Display with a height of 5 (maximum of 20) and with any width. But without spaces.
# LEGACY FEATURE

def don5ns(list1, list2, list3, list4, list5, list6 = None, list7 = None, list8 = None, list9 = None, list10 = None, list11 = None, list12 = None, list13 = None, list14 = None, list15 = None, list16 = None, list17 = None, list18 = None, list19 = None, list20 = None):
    alllists = []
    alluncompiledlists = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,list18,list19,list20]
    for i in alluncompiledlists:
        if i != None:
            alllists.append(i)
    for alist in alllists:
        for i in alist:
            print(i, end="")
        print("")

# - Inventory management -

# Inventory Find and Replace.

def inventoryFR(inventory, item):
    if type(inventory) == list:
        try:
            inventory[inventory.index(" ")] = item
            return inventory
        except(ValueError): return False

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

# Check if an index in a list or dictionary exists.

def reachableindex(liste, index):
    if type(liste) == list:
        if index < len(liste): return True
        else: return False
    else:
        try: liste[index]; return True
        except(KeyError): return False

# - Engine -

# Audio playing -
def playaudiothread(file, loop):
    if type(file) == str and type(loop) == bool:
        CHUNK = 1024
        try:
            with wave.open("Music/" + file, 'rb') as wf:
                # Instantiate PyAudio and initialize PortAudio system resources (1)
                p = pyaudio.PyAudio()

                # Open stream (2)
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                # Play samples from the wave file (3)
                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)

                # Close stream (4)
                stream.close()

                # Release PortAudio system resources (5)
                p.terminate()
        except(FileNotFoundError): return "AUDIO FNFE"
    elif type(file) == str and type(loop) != bool: return "AUDIO LUP " + str(type(loop)) + error("AUDIO LUP " + str(type(loop)))
    elif type(file) != str and type(loop) == bool: return "AUDIO FILE" + str(type(file)) + error('AUDIO FILE' + str(type(file)))
    else: return "AUDIO LUP " + str(type(loop)) + error("AUDIO LUP " + str(type(loop))) + "\nAUDIO FILE" + str(type(file)) + error('AUDIO FILE' + str(type(file)))

def playaudio(file, loop):
    global audiothread
    audiothread = Thread(target=playaudiothread, args=[file,loop])
    audiothread.start()

# Error finding -
def processvalue(value):
    match value:
        case "INT": return "INTEGER"
        case "FLT": return "FLOAT"
        case "STR": return "STRING"
        case "BUL": return "BOOLEAN"
        case "LST": return "LIST"
        case "TPL": return "TUPLE"
        case "DCT": return "DICTIONARY"
        case "ABV": return "above"
        case "EQ": return "equal to"
        case "BLO": return "below"
        case "<class 'str'>": return "STRING"
        case "<class 'float'>": return "FLOAT"
        case "<class 'int'>": return "INTEGER"
        case "<class 'bool'>": return "BOOLEAN"
        case "<case 'list'>": return "LIST"
        case "<case 'tuple'>": return "TUPLE"
        case "<case 'dict'>": return "DICTIONARY"

def error(errorcode):
    code = errorcode.split()
    if code[0] == "INV2":
        return ": Expected INTEGER, received " + processvalue(code[1]) + "."
    elif code[0] == "INV1":
        return ": Expected INTEGER above 0, received " + code[1] + "."
    elif code[0] == "AUDIO":
        if code[1] == "FILE": return ": Expected STRING, received " + code[2]
        elif code[1] == "LUP": return ": Expected BOOL, received " + code[2]
        elif code[1] == "FNFE": return ": Could not find file."

# Display -
    
# Display at ANY height and ANY width. But without spaces.
# Only takes 7 lines.

def display(todisplay): # The function takes a list of lists (let's call it X).
    buffer = "" # Makes the variable "buffer".
    for n in todisplay: # Checks every list in X.
        for i in n: # Checks every item in that list.
            buffer = buffer + i # Adds the currently selected item to the variable "buffer".
        buffer = buffer + "\n" # Adds a newline to the buffer.
    print(buffer) # Prints the variable "buffer".
        # Now it moves on to the next list in X.

# Object Defining -

# Inventory
class inventory:
    type = "player inventory"
    def __init__(self, slotnum=10, slotdata=None):
        if type(slotnum) == int:
            if slotnum > 0:
                slots = {}
                i = 0
                while i < slotnum:
                    if slotdata != None and ismore(slotdata, i):
                        slots["slot" + str(i + 1)] = slotdata[i]
                    else:
                        slots["slot" + str(i + 1)] = None
                    i += 1
                self.slots = slots
                self.selected = slots["slot1"]
            else: return "INV1 " + str(slotnum) + error("INV1" + str(slotnum))
        else:
            return "INV2"
    
    def __str__(self):
        return self.slots
    
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
    
    # Make the inventory bigger
    def enlargeinventory(self, slotnum, slotdata):
        lastkey = str(list(self.slots)[-1])
        lastkey = lastkey.split()
        current = int(lastkey[-1])
        for i in range(slotnum):
            self.slots["slot" + str(current + 1)] = slotdata[i]
            current += 1

# Player
class player:
    type = "player"
    def __init__(self, character=simple_colors.yellow("[ ]"), health=100, armor=0, attack=5, defense=5, speed=1, position=[2,2], inventory=inventory()):
        self.character = character
        self.health = health
        self.armor = armor
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = inventory
        self.X = position[0]
        self.Y = position[1]
        
    def __str__(self):
        return self.character

    # Move the player
    def move(self, direction, data, replace):
        
        # Load -
        
        X = self.X
        Y = self.Y
        Z = data[Y]

        direction = str.lower(direction)
        aboveplayer = None
        westplayer = None
        belowplayer = None
        eastplayer = None
        currentpos = Z[X]
        if reachableindex(data, Y - 1):
            aboveplayer = data[Y - 1]
        if reachableindex(Z, X - 1):
            westplayer = Z[X - 1]
        if reachableindex(data, Y + 1):
            belowplayer = data[Y + 1]
        if reachableindex(Z, X + 1):
            eastplayer = Z[X + 1]
        i = 0
        
        # Main -
        
        while i < self.speed:
            if direction == "w" and aboveplayer != None:
                if aboveplayer[X].passable:
                    self.Y -= 1
                    currentpos = replace
                    aboveplayer[X] = self.character
            elif direction == "a" and westplayer != None:
                if westplayer.passable:
                    self.X -= 1
                    currentpos = replace
                    westplayer = self.character
            elif direction == "s" and belowplayer[X] != None:
                if belowplayer[X].passable:
                    self.Y += 1
                    currentpos = replace
                    belowplayer[X] = self.character
            elif direction == "d" and eastplayer != None:
                if eastplayer.passable:
                    self.X += 1
                    currentpos = replace
                    eastplayer = self.character
            i += 1
        
            # Return -
            data[Y + 1] = belowplayer
            data[Y - 1] = aboveplayer
            Z[X + 1] = eastplayer
            Z[X - 1] = westplayer
            Z[X] = currentpos
            data[Y] = Z
        return data

    # Apply Gravity to the player
    def applygravity(self, direction, data, replace, blocks):
        # Load Variables
        
        i = 0
        
        # Main

# Block
class block:
    def __init__(self, image=simple_colors.black('Stn'), passable=False, breakablebytool=True, droptoolvalue=2, drop=simple_colors.black('Stone'), falling=False):
        self.image = image
        self.passable = passable
        self.breakablebytool = breakablebytool
        self.droptoolvalue = droptoolvalue
        self.drop = drop
    
    def __str__(self):
        return self.image

# World Generation -

def generate(width,height, config, Air, Stn, Bedrock, limit, oreconfig):
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
        for i in list(oreconfig.values()):
            
            spawnchance = random.randint(1, i[0])

            if spawnchance == 1 and reachableindex(space,"y" + str(n[0] + i[1])):
                area = random.randint(i[1], i[2])
                carea = n[0] + area
                if carea >= height:
                    while carea >= height: carea -= 1
                space["y" + str(carea)][n[1]] = list(oreconfig.values())[list(oreconfig.values()).index(i)][3]
                
    
    # FINALLY return the world.
    
    return list(space.values())

=======
# Loading

import time
import os
import random
from threading import Thread, Event
try: import colorama
except(ModuleNotFoundError): os.system("pip install colorama"); import colorama
try: import pyaudio
except(ModuleNotFoundError): os.system("pip install pyaudio"); import pyaudio
try: import wave
except(ModuleNotFoundError): os.system("pip install wave"); import wave

# - Misceallanous -

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

# Display with a height of 5 (maximum of 20) and with any width. But without spaces.
# LEGACY FEATURE

def don5ns(list1, list2, list3, list4, list5, list6 = None, list7 = None, list8 = None, list9 = None, list10 = None, list11 = None, list12 = None, list13 = None, list14 = None, list15 = None, list16 = None, list17 = None, list18 = None, list19 = None, list20 = None):
    alllists = []
    alluncompiledlists = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16,list17,list18,list19,list20]
    for i in alluncompiledlists:
        if i != None:
            alllists.append(i)
    for alist in alllists:
        for i in alist:
            print(i, end="")
        print("")

# - Inventory management -

# Inventory Find and Replace.

def inventoryFR(inventory, item):
    if type(inventory) == list:
        try:
            inventory[inventory.index(" ")] = item
            return inventory
        except(ValueError): return False

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

# Check if an index in a list or dictionary exists.

def reachableindex(liste, index):
    if type(liste) == list:
        if index < len(liste): return True
        else: return False
    else:
        try: liste[index]; return True
        except(KeyError): return False

# - Engine -

# Image Type -
# Kinda required if you wanna use colors with the Display() command
class createimage(string='Stn', foreorback = "Fore", color='LIGHTBLACK', internal='S'):
    def __init__(self, string, foreorback, color, internal):
        self.character = string
        self.color = color
        self.internal = internal
        if str.lower(foreorback) == "Fore":
            match str.lower(color):
                case "white": self.color = colorama.Fore.WHITE
                case "black": self.color = colorama.Fore.BLACK
                case "blue": self.color = colorama.Fore.BLUE
                case "cyan": self.color = colorama.Fore.CYAN
                case "green": self.color = colorama.Fore.GREEN
                case "lightblack": self.color = colorama.Fore.LIGHTBLACK_EX
                case "lightblue": self.color = colorama.Fore.LIGHTBLUE_EX
                case "lightcyan": self.color = colorama.Fore.LIGHTCYAN_EX
                case "lightgreen": self.color = colorama.Fore.LIGHTGREEN_EX
                case "lightmagenta": self.color = colorama.Fore.LIGHTMAGENTA_EX
                case "lightred": self.color = colorama.Fore.LIGHTRED_EX
                case "lightwhite": self.color = colorama.Fore.LIGHTWHITE_EX
                case "lightyellow": self.color = colorama.Fore.LIGHTYELLOW_EX
                case "red": self.color = colorama.Fore.RED
                case "magenta": self.color = colorama.Fore.MAGENTA
                case "yellow": self.color = colorama.Fore.YELLOW
        elif str.lower(foreorback) == "back":
            match str.lower(color):
                case "white": self.color = colorama.Back.WHITE
                case "black": self.color = colorama.Back.BLACK
                case "blue": self.color = colorama.Back.BLUE
                case "cyan": self.color = colorama.Back.CYAN
                case "green": self.color = colorama.Back.GREEN
                case "lightblack": self.color = colorama.Back.LIGHTBLACK_EX
                case "lightblue": self.color = colorama.Back.LIGHTBLUE_EX
                case "lightcyan": self.color = colorama.Back.LIGHTCYAN_EX
                case "lightgreen": self.color = colorama.Back.LIGHTGREEN_EX
                case "lightmagenta": self.color = colorama.Back.LIGHTMAGENTA_EX
                case "lightred": self.color = colorama.Back.LIGHTRED_EX
                case "lightwhite": self.color = colorama.Back.LIGHTWHITE_EX
                case "lightyellow": self.color = colorama.Back.LIGHTYELLOW_EX
                case "red": self.color = colorama.Back.RED
                case "magenta": self.color = colorama.Back.MAGENTA
                case "yellow": self.color = colorama.Back.YELLOW
    
    def __str__(self, internal):
        if internal == True: return self.internal
        else: return self.character


# Playing audio -
def playaudiothread(file, loop):
    if type(file) == str and type(loop) == bool:
        CHUNK = 1024
        try:
            with wave.open("Music/" + file, 'rb') as wf:
                # Instantiate PyAudio and initialize PortAudio system resources (1)
                p = pyaudio.PyAudio()

                # Open stream (2)
                stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                                channels=wf.getnchannels(),
                                rate=wf.getframerate(),
                                output=True)

                # Play samples from the wave file (3)
                while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
                    stream.write(data)

                # Close stream (4)
                stream.close()

                # Release PortAudio system resources (5)
                p.terminate()
        except(FileNotFoundError): return "AUDIO FNFE"
    elif type(file) == str and type(loop) != bool: return "AUDIO LUP " + str(type(loop)) + error("AUDIO LUP " + str(type(loop)))
    elif type(file) != str and type(loop) == bool: return "AUDIO FILE" + str(type(file)) + error('AUDIO FILE' + str(type(file)))
    else: return "AUDIO LUP " + str(type(loop)) + error("AUDIO LUP " + str(type(loop))) + "\nAUDIO FILE" + str(type(file)) + error('AUDIO FILE' + str(type(file)))

def playaudio(file, loop):
    global audiothread
    audiothread = Thread(target=playaudiothread, args=[file,loop])
    audiothread.start()

# Error finding -
def processvalue(value):
    match value:
        case "INT": return "INTEGER"
        case "FLT": return "FLOAT"
        case "STR": return "STRING"
        case "BUL": return "BOOLEAN"
        case "LST": return "LIST"
        case "TPL": return "TUPLE"
        case "DCT": return "DICTIONARY"
        case "ABV": return "above"
        case "EQ": return "equal to"
        case "BLO": return "below"
        case "<class 'str'>": return "STRING"
        case "<class 'float'>": return "FLOAT"
        case "<class 'int'>": return "INTEGER"
        case "<class 'bool'>": return "BOOLEAN"
        case "<case 'list'>": return "LIST"
        case "<case 'tuple'>": return "TUPLE"
        case "<case 'dict'>": return "DICTIONARY"

def error(errorcode):
    code = errorcode.split()
    if code[0] == "INV2":
        return ": Expected INTEGER, received " + processvalue(code[1]) + "."
    elif code[0] == "INV1":
        return ": Expected INTEGER above 0, received " + code[1] + "."
    elif code[0] == "AUDIO":
        if code[1] == "FILE": return ": Expected STRING, received " + code[2]
        elif code[1] == "LUP": return ": Expected BOOL, received " + code[2]
        elif code[1] == "FNFE": return ": Could not find file."

# Display -
    
# Display at ANY height and ANY width. But without spaces.
# Only takes 7 lines.

def display(todisplay): # The function takes a list of lists (let's call it X).
    buffer = "" # Makes the variable "buffer".
    for n in todisplay: # Checks every list in X.
        for i in n: # Checks every item in that list.
            buffer = buffer + i # Adds the currently selected item to the variable "buffer".
        buffer = buffer + "\n" # Adds a newline to the buffer.
    print(buffer) # Prints the variable "buffer".
        # Now it moves on to the next list in X.

# Object Defining -

# Inventory
class inventory:
    type = "player inventory"
    def __init__(self, slotnum=10, slotdata=None):
        if type(slotnum) == int:
            if slotnum > 0:
                slots = {}
                i = 0
                while i < slotnum:
                    if slotdata != None and ismore(slotdata, i):
                        slots["slot" + str(i + 1)] = slotdata[i]
                    else:
                        slots["slot" + str(i + 1)] = None
                    i += 1
                self.slots = slots
                self.selected = slots["slot1"]
            else: return "INV1 " + str(slotnum) + error("INV1" + str(slotnum))
        else:
            return "INV2"
    
    def __str__(self):
        return self.slots
    
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
    
    # Make the inventory bigger
    def enlargeinventory(self, slotnum, slotdata):
        lastkey = str(list(self.slots)[-1])
        lastkey = lastkey.split()
        current = int(lastkey[-1])
        for i in range(slotnum):
            self.slots["slot" + str(current + 1)] = slotdata[i]
            current += 1

# Player
class player:
    type = "player"
    def __init__(self, character=createimage('Player', 'Fore' 'YELLOW', 'Player'), health=100, armor=0, attack=5, defense=5, speed=1, position=[2,2], inventory=inventory()):
        self.character = character
        self.health = health
        self.armor = armor
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = inventory
        self.X = position[0]
        self.Y = position[1]
        
    def __str__(self):
        return self.character

    # Move the player
    def move(self, direction, data, replace):
        
        # Load -
        
        X = self.X
        Y = self.Y
        Z = data[Y]

        direction = str.lower(direction)
        aboveplayer = None
        westplayer = None
        belowplayer = None
        eastplayer = None
        currentpos = Z[X]
        if reachableindex(data, Y - 1):
            aboveplayer = data[Y - 1]
        if reachableindex(Z, X - 1):
            westplayer = Z[X - 1]
        if reachableindex(data, Y + 1):
            belowplayer = data[Y + 1]
        if reachableindex(Z, X + 1):
            eastplayer = Z[X + 1]
        i = 0
        
        # Main -
        
        while i < self.speed:
            if direction == "w" and aboveplayer != None:
                if aboveplayer[X].passable:
                    self.Y -= 1
                    currentpos = replace
                    aboveplayer[X] = self.character
            elif direction == "a" and westplayer != None:
                if westplayer.passable:
                    self.X -= 1
                    currentpos = replace
                    westplayer = self.character
            elif direction == "s" and belowplayer[X] != None:
                if belowplayer[X].passable:
                    self.Y += 1
                    currentpos = replace
                    belowplayer[X] = self.character
            elif direction == "d" and eastplayer != None:
                if eastplayer.passable:
                    self.X += 1
                    currentpos = replace
                    eastplayer = self.character
            i += 1
        
            # Return -
            data[Y + 1] = belowplayer
            data[Y - 1] = aboveplayer
            Z[X + 1] = eastplayer
            Z[X - 1] = westplayer
            Z[X] = currentpos
            data[Y] = Z
        return data

    # Apply Gravity to the player
    def applygravity(self, direction, data, replace, blocks):
        # Load Variables
        
        i = 0
        
        # Main

# Block
class block:
    def __init__(self, image=createimage(), passable=False, breakablebytool=True, droptoolvalue=2, drop=createimage('Stone'), falling=False):
        self.image = image
        self.passable = passable
        self.breakablebytool = breakablebytool
        self.droptoolvalue = droptoolvalue
        self.drop = drop
        self.falling = falling
    
    def __str__(self):
        return self.image

# World Generation -

def generate(width,height, config, Air, Stn, Bedrock, limit, oreconfig):
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
        for i in list(oreconfig.values()):
            
            spawnchance = random.randint(1, i[0])

            if spawnchance == 1 and reachableindex(space,"y" + str(n[0] + i[1])):
                area = random.randint(i[1], i[2])
                carea = n[0] + area
                if carea >= height:
                    while carea >= height: carea -= 1
                space["y" + str(carea)][n[1]] = list(oreconfig.values())[list(oreconfig.values()).index(i)][3]
                
    
    # FINALLY return the world.
    
    return list(space.values())

>>>>>>> 78e17e3 (Syncing VS Code with Git)
