import os
try:
	import api
except(ModuleNotFoundError):
    input("Fatal Error: API Not Found.\nPossible Solutions:\n1. Run updater.py outside of the \"Apps\" folder.\n2. Return the App to the \"Apps\" folder\n\nIf you cannot apply these solutions, you may need to contact someone who can.")
try:
    import simple_colors
except(ModuleNotFoundError):
	input("Module Not Found Error. Assuming first boot..")
	os.system("pip install simple_colors")
	import simple_colors

api.clear()

input("This is an even more advanced version of iliketomoveit.\nSame rules, but you can't move into non-air blocks.\nYou can't fly either.\nPress Enter to start Game.")

# Loading Colors

Drt = simple_colors.green("Drt")
Stn = simple_colors.black("Stn", "bright")
Air = simple_colors.cyan("Air")
Plr = simple_colors.yellow("[ ]")
bedrock = simple_colors.black("Bdr", "bright")
oreconfig = {}
Log = ("Log")

# The Variables

# Width and Height
width = 50
height = 30

# Help command

quitorhelp = ["- Normal Commands -\n", "quit - Exits the game", "help - Shows all the commands"]
inventorycoms = ["\n- Inventory Commands -\n", "inventory - Displays your inventory", "inventory set [item] - Sets your currently equipped item. Replace \"[item]\" with item number.", "inventory use [direction] - Uses that item. Replace \"[direction]\" with the direction you want to use it in."]
movementcoms = ["\n- Movement Commands -\n", "left - Moves left", "right - Moves right", "up - Jumps.", "down - Goes down."]

# All sets (used for playerposition)

allsets = api.generate(width, height, config=[Drt,Drt], Air=Air, Stn=Stn, Bedrock=bedrock, limit=[10, 20], oreconfig=oreconfig)

# X and Y (used to set some things)

X = 3
maxleft = 0
maxrightneeded = allsets[0]
maxright = maxrightneeded.index(maxrightneeded[-1])

Y = allsets[2]
Y[X] = Plr

# Player position (used to check some things or set some things)

playerpos = allsets.index(Y, 0, allsets.index(allsets[-1]))
belowplayerpos = allsets[playerpos + 1]
aboveplayerpos = allsets[playerpos - 1]

# Inventory

inventory = ["Axe", "Stone Stick", " "]
equippeditem = inventory[0]

# Impassable Objects

impassableobj = [Drt, Stn, Log]

# Debug Mode

debugmode = False
allvariables = ["quitorhelp:", quitorhelp, "inventorycoms:", inventorycoms, "movementcoms:", movementcoms, "allsets:", allsets, "X:", X, "maxleft:", maxleft, "maxright:", maxright, "Y:", Y, "Y[X]:", Y[X], "playerpos:", playerpos, "inventory:", inventory, "equippeditem:", equippeditem]

# Functions

def makescreen():
	while True:
		api.wait(1)
		api.clear()
		api.don5ns(A, B, C, D, E)

def ismore(list, index):
    try:
        list[index]
        return True
    except(IndexError):
        return False

def isint(string):
    try:
        int(string)
        return True
    except(ValueError):
        return False

# Main Game

while True:

	api.clear()
	api.display(allsets)

	Pinput = input("> ")

	if Pinput == "quit":
		break
	elif Pinput == "help":
		for i in quitorhelp:
			print(i)
		for i in inventorycoms:
			print(i)
		for i in movementcoms:
			print(i)
		input("That's all the commands.")

	# Left and Right Movement
	try:
		if Pinput.startswith("l") and X != maxleft and Y[X - 1] not in impassableobj:
			Y[X - 1] = Plr
			Y[X] = Air
			X -= 1
			if belowplayerpos[X] == Air:
				Y[X] = Air
				belowplayerpos[X] = Plr
				Y = belowplayerpos
			playerpos = allsets.index(Y, 0, allsets.index(allsets[-1]))
	except (IndexError):
		input("Invalid move!")
	try:
		if Pinput.startswith("r") and X != maxright and Y[X + 1] not in impassableobj:
			Y[X + 1] = Plr
			Y[X] = Air
			X += 1
			if belowplayerpos[X] == Air:
				Y[X] = Air
				belowplayerpos[X] = Plr
				Y = belowplayerpos
	except (IndexError):
		input("Invalid move!")

	# Up and Down Movement
	if Pinput.startswith("u") and playerpos != 0 and aboveplayerpos[
	    X] :
		if belowplayerpos[X] != Air:
			Y[X] = Air
			aboveplayerpos[X] = Plr
			Y = aboveplayerpos
		else:
			Y[X] = Air
			belowplayerpos[X] = Plr
			Y = belowplayerpos
	elif Pinput.startswith("d") and playerpos != allsets.index(allsets.index(allsets[-1])) and belowplayerpos[
	    X] not in impassableobj != Stn:
		Y[X] = Air
		belowplayerpos[X] = Plr
		Y = belowplayerpos

	# Inventory interactions

	# Inventory
 
	elif Pinput.startswith("inventory"):
		cinput = Pinput.split()
		if ismore(cinput, 1):
	# Inventory - Set
			if cinput[1] == "set":
				if ismore(cinput, 2) and isint(cinput[2]):
					equippeditem = inventory[int(cinput[2]) - 1]
				else: input("Incorrect number of arguments or third argument was not a number.")
	# Inventory - Use
			elif cinput[1] == "use":
				if ismore(cinput, 2):
	# Left Direction
					if cinput[2].startswith("l") and Y[X - 1] == Drt or Y[X - 1] == Stn:
						if equippeditem == "Pickaxe":
							Y[X - 1] = Air
						else: input("Pickaxe is not equipped.")
					elif cinput[2].startswith("l") and Y[X - 1] == Log:
						if equippeditem == "Axe":
							Y[X - 1] = Air
							checking = api.inventoryFR(inventory, "Log")
							if checking != False: inventory = checking
							else: input("Not enough Space in Inventory.");Y[X - 1] = Log
						else: input("Axe is not equipped.")
	# Right Direction
					elif cinput[2].startswith("r") and Y[X + 1] == Drt or Y[X + 1] == Stn:
						if equippeditem == "Pickaxe":
							Y[X + 1] = Air
						else: input("Pickaxe is not equipped.")
					elif cinput[2].startswith("r") and Y[X + 1] == Log:
						if equippeditem == "Axe":
							Y[X + 1] = Air
							checking = api.inventoryFR(inventory, "Log")
							if checking != False: inventory = checking
							else: input("Not enough Space in Inventory.");Y[X + 1] = Log
						else: input("Axe is not equipped.")
    # Up Direction
					elif cinput[2].startswith("u") and aboveplayerpos[X] == Drt or aboveplayerpos[X] == Stn:
						if equippeditem == "Pickaxe":
							aboveplayerpos[X] = Air
						else: input("Pickaxe is not equipped.")
					elif cinput[2].startswith("d") and aboveplayerpos[X] == Log:
						if equippeditem == "Axe":
							aboveplayerpos[X] = Air
							checking = api.inventoryFR(inventory, "Log")
							if checking != False: inventory = checking
							else: input("Not enough Space in Inventory.");aboveplayerpos[X] = Log
						else: input("Axe is not equipped.")
    # Down Direction
					elif cinput[2].startswith("d") and belowplayerpos[X] == Drt or belowplayerpos[X] == Stn:
						if equippeditem == "Pickaxe":
							belowplayerpos[X] = Air
						else: input("Pickaxe is not equipped.")
					elif cinput[2].startswith("d") and belowplayerpos[X] == Log:
						if equippeditem == "Axe":
							belowplayerpos[X] = Air
							checking = api.inventoryFR(inventory, "Log")
							if checking != False: inventory = checking
							else: input("Not enough Space in Inventory.");belowplayerpos[X] = Log
						else: input("Axe is not equipped.")
	# Error handling
					else: input("Are you trying to use an item on Air?")
				else: input("Incorrect number of arguments")
	# Inventory - Craft
#			elif cinput[1] == "craft":
#				
			else: input("That's not a command.")
	# Inventory - Open
		else:
			print("This is what you have.")
			for i in inventory:
				input(i)
	# Apply Gravity
		if belowplayerpos[X] == Air:
			Y[X] = Air
			belowplayerpos[X] = Plr
			Y = belowplayerpos
	# Update Playerpos
	playerpos = allsets.index(Y, 0, allsets.index(allsets[-1]))
	if playerpos != J:
		belowplayerpos = allsets[playerpos + 1]
	else:
		belowplayerpos = None
	if playerpos != A:
		aboveplayerpos = allsets[playerpos - 1]
	else:
		aboveplayerpos = None


input("Game ended, hope you liked it. >")
