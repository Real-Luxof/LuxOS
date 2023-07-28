import time
from os import system as sys
import os
sys("pip install requests")
sys("cls")
time.sleep(5)
import requests
userinput = input("Yooo! wassup my man?\nHeard you wanted a lil' update.\nWell, I'm gonna check for some. Your system should be great after this.\n- This program may accidentally make things worse if you don't have an Internet Connection. -")
try:
    stateofmain = "FINE"
    stateofinterface = "FINE"
    stateofapi = "FINE"
    stateofapidocs = "FINE"
    with open("main.py", "r") as f:
        main = f.read()
    with open("interface.py", "r") as f:
        interface = f.read()
    with open("Apps/api.py", "r") as f:
        api = f.read()
    with open("APIDocs.txt", "r") as f:
        apidocs = f.read()
    r = requests.get('https://programhub.survivalist260.repl.co/static/LUXOS_MAIN.txt')
    if main != r.text:
        stateofmain = "NOT FINE"
        with open("main.py", "w") as f:
            f.write(r.text)
    r = requests.get("https://programhub.survivalist260.repl.co/static/LUXOS_INTERFACE.txt")
    if interface != r.text:
        stateofinterface = "NOT FINE"
        with open("interface.py", "w") as f:
            f.write(r.text)
    r = requests.get("https://programhub.survivalist260.repl.co/static/LUXOS_API.txt")
    if api != r.text:
        stateofapi = "NOT FINE"
        with open("Apps/api.py", "w") as f:
            f.write(r.text)
    r = requests.get('https://programhub.survivalist260.repl.co/static/LUXOS_APIDOCS.txt')
    if apidocs != r.text:
        stateofapidocs = "NOT FINE"
        with open("APIDocs.txt", "w") as f:
            f.write(r.text)
    
    input(stateofmain + "\n" + stateofinterface + "\n" + stateofapi + "\n" + stateofapidocs)
    if stateofmain and stateofinterface and stateofapi and stateofapidocs == "FINE":
        input("No need for me! your system is already clean, which is a good thing!")
    else:
        input("Your system should be working faster than C++ now! (an exaggeration, of course. Or is it?)")
except(FileNotFoundError):
    input("Woah! Seems like your system is pretty f'd up.\nLemme just fix that for you in a sec.")
    r = requests.get('https://programhub.survivalist260.repl.co/static/LUXOS_MAIN.txt')
    with open("main.py", "w") as f:
        f.write(r.text)
    r = requests.get('https://programhub.survivalist260.repl.co/static/LUXOS_INTERFACE.txt')
    with open("interface.py", "w") as f:
        f.write(r.text)
    r = requests.get('https://programhub.survivalist260.repl.co/static/LUXOS_APIDOCS.txt')
    with open("APIDocs.txt", "w") as f:
        f.write(r.text)
    r = requests.get('https://programhub.survivalist260.repl.co/static/LUXOS_API.txt')
    if os.path.isdir("Apps"):
        if os.path.isfile("Apps/api.py") == False:
            with open("Apps/api.py", "w") as f:
                f.write(r.text)
    else:
        sys("mkdir Apps")
        with open("Apps/api.py", "w") as f:
            f.write(r.text)
    input("All fixed. Your system should work now.")
quit()
