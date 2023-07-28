<<<<<<< HEAD
import os
import api
import simple_colors
from threading import Thread

os.system("pip install simple_colors")

print("This is an advanced version of Iliketomoveit.")
print("Same rules, but you can't move into non-air blocks.")
print("You can't fly either.")
input("Press Enter to start Game.")

# Loading Colors

Drt = simple_colors.green("Drt")
Stn = simple_colors.black("Stn", "bright")
Air = "Air"
Plr = simple_colors.yellow("Plr")

A = [Air, Air, Air, Air, Air, Air, Air]
B = [Air, Air, Air, Air, Air, Air, Air]
C = [Drt, Drt, Drt, Plr, Air, Air, Air]
D = [Drt, Drt, Drt, Drt, Drt, Stn, Stn]
E = [Stn, Stn, Stn, Stn, Stn, Stn, Stn]

# The Variables

allsets = [A, B, C, D, E]
X = 3
Y = C
Y[X] = Plr
airtime = 0
playerpos = allsets.index(Y, 0, 4)
belowplayerpos = allsets[playerpos + 1]
aboveplayerpos = allsets[playerpos - 1]


def makescreen():
	while True:
		api.wait(1)
		api.clear()
		api.don5ns(A, B, C, D, E)


displayer = Thread(target=makescreen)
# displayer.start()

while True:

	api.clear()
	api.don5ns(A, B, C, D, E)

	Pinput = input("> ")

	if Pinput == "quit":
		break
	# Left and Right Movement
	try:
		if Pinput.startswith(
		    "l") and X != 0 and Y[X - 1] != Drt and Y[X - 1] != Stn:
			Y[X - 1] = Plr
			Y[X] = Air
			X -= 1
			if belowplayerpos[X] == Air:
				Y[X] = Air
				belowplayerpos[X] = Plr
				Y = belowplayerpos
			playerpos = allsets.index(Y, 0, 4)
	except (IndexError):
		input("Invalid move!")
	try:
		if Pinput.startswith(
		    "r") and X != 6 and Y[X + 1] != Drt and Y[X + 1] != Stn:
			Y[X + 1] = Plr
			Y[X] = Air
			X += 1
			playerpos = allsets.index(Y, 0, 4)
			if belowplayerpos[X] == Air:
				Y[X] = Air
				belowplayerpos[X] = Plr
				Y = belowplayerpos
	except (IndexError):
		input("Invalid move!")
	# Up and Down Movement
	if Pinput.startswith("u") and playerpos != 0 and aboveplayerpos[
	    X] != Drt and aboveplayerpos[X] != Stn:
		if belowplayerpos[X] != Air:
			Y[X] = Air
			aboveplayerpos[X] = Plr
			Y = aboveplayerpos
		else:
			input("No Flying!")
			Y[X] = Air
			belowplayerpos[X] = Plr
			Y = belowplayerpos
		playerpos = allsets.index(Y, 0, 4)
	elif Pinput.startswith("d") and playerpos != 4 and belowplayerpos[
	    X] != Drt and belowplayerpos[X] != Stn:
		Y[X] = Air
		belowplayerpos[X] = Plr
		Y = belowplayerpos
		playerpos = allsets.index(Y, 0, 4)

	# Update Playerpos
	playerpos = allsets.index(Y, 0, 4)
	if playerpos != E:
		belowplayerpos = allsets[playerpos + 1]
	else:
		belowplayerpos = None
	if playerpos != A:
		aboveplayerpos = allsets[playerpos - 1]
	else:
		aboveplayerpos = None

# displayer.join()

input("Game ended, hope you liked it. >")
=======
import os
import api
import simple_colors
from threading import Thread

os.system("pip install simple_colors")

print("This is an advanced version of Iliketomoveit.")
print("Same rules, but you can't move into non-air blocks.")
print("You can't fly either.")
input("Press Enter to start Game.")

# Loading Colors

Drt = simple_colors.green("Drt")
Stn = simple_colors.black("Stn", "bright")
Air = "Air"
Plr = simple_colors.yellow("Plr")

A = [Air, Air, Air, Air, Air, Air, Air]
B = [Air, Air, Air, Air, Air, Air, Air]
C = [Drt, Drt, Drt, Plr, Air, Air, Air]
D = [Drt, Drt, Drt, Drt, Drt, Stn, Stn]
E = [Stn, Stn, Stn, Stn, Stn, Stn, Stn]

# The Variables

allsets = [A, B, C, D, E]
X = 3
Y = C
Y[X] = Plr
airtime = 0
playerpos = allsets.index(Y, 0, 4)
belowplayerpos = allsets[playerpos + 1]
aboveplayerpos = allsets[playerpos - 1]


def makescreen():
	while True:
		api.wait(1)
		api.clear()
		api.don5ns(A, B, C, D, E)


displayer = Thread(target=makescreen)
# displayer.start()

while True:

	api.clear()
	api.don5ns(A, B, C, D, E)

	Pinput = input("> ")

	if Pinput == "quit":
		break
	# Left and Right Movement
	try:
		if Pinput.startswith(
		    "l") and X != 0 and Y[X - 1] != Drt and Y[X - 1] != Stn:
			Y[X - 1] = Plr
			Y[X] = Air
			X -= 1
			if belowplayerpos[X] == Air:
				Y[X] = Air
				belowplayerpos[X] = Plr
				Y = belowplayerpos
			playerpos = allsets.index(Y, 0, 4)
	except (IndexError):
		input("Invalid move!")
	try:
		if Pinput.startswith(
		    "r") and X != 6 and Y[X + 1] != Drt and Y[X + 1] != Stn:
			Y[X + 1] = Plr
			Y[X] = Air
			X += 1
			playerpos = allsets.index(Y, 0, 4)
			if belowplayerpos[X] == Air:
				Y[X] = Air
				belowplayerpos[X] = Plr
				Y = belowplayerpos
	except (IndexError):
		input("Invalid move!")
	# Up and Down Movement
	if Pinput.startswith("u") and playerpos != 0 and aboveplayerpos[
	    X] != Drt and aboveplayerpos[X] != Stn:
		if belowplayerpos[X] != Air:
			Y[X] = Air
			aboveplayerpos[X] = Plr
			Y = aboveplayerpos
		else:
			input("No Flying!")
			Y[X] = Air
			belowplayerpos[X] = Plr
			Y = belowplayerpos
		playerpos = allsets.index(Y, 0, 4)
	elif Pinput.startswith("d") and playerpos != 4 and belowplayerpos[
	    X] != Drt and belowplayerpos[X] != Stn:
		Y[X] = Air
		belowplayerpos[X] = Plr
		Y = belowplayerpos
		playerpos = allsets.index(Y, 0, 4)

	# Update Playerpos
	playerpos = allsets.index(Y, 0, 4)
	if playerpos != E:
		belowplayerpos = allsets[playerpos + 1]
	else:
		belowplayerpos = None
	if playerpos != A:
		aboveplayerpos = allsets[playerpos - 1]
	else:
		aboveplayerpos = None

# displayer.join()

input("Game ended, hope you liked it. >")
>>>>>>> 78e17e3 (Syncing VS Code with Git)
