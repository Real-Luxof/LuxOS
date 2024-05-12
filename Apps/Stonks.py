# - Loading Started -

# Import os. It is needed to check for and create folders, as well as to install modules.
import os

# Loading thingy
bar1 = "   \n| |\n___"

print(l + "\n" + bar) # Display the loading bar
def increment(num=1):
    """Make the loading bar progress ahead."""
    global l
    global bar
    api.clear() # Clear the screen and put the LuxOS logo there
    for times in range(num):
        match bar2:
            case "| ": bar2 = "  "; bar1 = "_ "
    print(l + "\n" + bar)

# Initialize the Game Engine
print("Initializing Game Engine..")
try: import api # Try to import it.
except(ModuleNotFoundError): input("Couldn't find the engine, I'm gonna quit now! LUL."); quit
# If the program can't for whatever reason, quit.

# Import the import_module function from the importlib module
print("Importing function: import_module from module: importlib")
from importlib import import_module

increment()

# Folder variables used for loading

print("Loading path variables..")
files = "gamedata\\stonks" # Variable for main game files
save = "gamedata\\stonks\\save.py" # Variable for the save.
                                   # Yeah, I'm too lazy to do save management. So what?
st = "gamedata\\stonks\\soundtrack" # Variable for the soundtrack folder.

increment()

# Real file shit

print("Checking file stuff..")
if os.path.exists(files) == False:
    print("Installing..")
    os.system("md " + files)

if os.path.exists(save) == False:
    print("Installing save..")
    os.system("md " + save)
