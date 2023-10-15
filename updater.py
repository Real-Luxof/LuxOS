# Imports
import os # Import the OS library, mainly used to execute commands like "cls" or "del".
import urllib.request # Import urllib.request, used to download files.

# Announcing that the program has started.
input("Yooo! wassup my man?\nHeard you wanted the newest version of LUX OS, and I've got it right here!\nTake it.\n- This program may accidentally make things worse if you don't have an Internet Connection. -")

# Deleting files to make space for new ones.
os.system("del main.py") # Delete main.py aka the bootloader.
os.system("del interface.py") # Delete interface.py aka the kernel.
os.system("del Apps\\api.py") # Delete api.py aka the Engine.
os.system("del Apps\\gamedata\\api.py") # Delete the Engine inside gamedata.
os.system("del APIDocs.txt") # Delete APIDocs.txt aka the Engine Manual.

# Grabbing the site.
site = "https://programhub.survivalist260.repl.co/static/"

# Downloading stuff.
urllib.request.urlretrieve(site + "LUXOS_MAIN.txt", "main.py") # Download the latest version of main.py aka the bootloader.
urllib.request.urlretrieve(site + "LUXOS_INTERFACE.txt", "interface.py") # Download the latest version of interface.py aka the kernel.
urllib.request.urlretrieve(site + "LUXOS_APIDOCS.txt", "APIDocs.txt") # Download the latest version of APIDocs.txt aka the Engine Manual.
os.system("mkdir Apps") # Make the directory "Apps"
os.system("md Apps/gamedata") # Make the directory "gamedata" inside "Apps"
urllib.request.urlretrieve(site + "LUXOS_API.txt", "Apps/api.py") # Download the latest version of API.py aka the Engine to Apps.
urllib.request.urlretrieve(site + "LUXOS_API.txt", "Apps/gamedata/api.py") # Download API.py to Apps/gamedata.

# Announcing that the program has ended.
print("Aight bro, peace!")
