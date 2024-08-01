from urllib.request import urlretrieve
from keyboard import read_key
from os import mkdir

print("Update process initiated. Please know that the latest commit may be unstable, get fucked if it is.")
print("If you do not have access to the internet your files may be fucked as I have not tested this.")
print("No files outside of the ones being downloaded will be overwritten.")
print("Are you sure you wish to update?")
print("Press any key to continue..")
read_key()
print("Install process intiated.")

def install(file: str, destination: str):
    print(f"Downloading: {file}")
    urlretrieve(f"https://raw.githubusercontent.com/Real-Luxof/LuxOS/main/{file}", file)

install("main.py", "main.py")
install("interface.py", "interface.py")
mkdir("Apps")
mkdir("Apps\\gamedata")
install("Apps/api.py", "Apps\\api.py")

print("Installation complete.")
print("Press any key to exit..")
read_key()
