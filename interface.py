def terminal():
    # Loading
    
    from Apps import api
    def title():
        api.clear()
    listofcommands = ["help","search","quit","find", "music"]
    listofmodularcommands = ["download", "run", "delete"]
    downloadargs = 1

    # Display List of Commands
    
    def displayLOC(LOC, modularlist):
        for i in LOC:
            print(i)
        for i in modularlist:
            print(i)
    
    # Display Downloadable Content
    
    def displaydownloads(list):
        clist = list.text
        clist.replace("__pycache__", "")
        clist.replace("api.py", "")
        clist.replace(".py", "")
        print(clist)

    # No command exception
    
    global nocommandexception
    nocommandexception = False

    # Imports

    import os
    try: import requests
    except(ModuleNotFoundError): os.system("pip install requests")
    from Apps import api
    import urllib

    # Music command
    
    if os.path.exists("music") == False:
        os.system("md music")
    global p
    p = None
    
    # Game Data Folder
    
    if os.path.exists("Apps\\gamedata") == False:
        os.system("md Apps\\gamedata")
    
    # Loading Ended
    
    # Main App
    
    while True:
        title()
        rawinput = input("> ")
        
        cinput = rawinput.split()
        
        # Processing Input
        
        if cinput != []:
            if cinput[0] in listofcommands:
            # Help Command
            
                if cinput[0] == listofcommands[0]:
                    displayLOC(listofcommands, listofmodularcommands)
                    input("Press Enter to go back to title screen...")
                    os.system("cls")
            
            # Find Downloadable Content Command
            
                elif cinput[0] == listofcommands[1]:
                    try:
                        r = requests.get('https://programhub.survivalist260.repl.co/static/list.txt')
                        if r.status_code:
                            displaydownloads(r)
                            input("When you download one of these Apps, check the spelling Because it is case-sensitive.\n(I made it that way to piss you off, my pleasure. <3)")
                    except(ConnectionError or ConnectionAbortedError or ConnectionRefusedError or ConnectionResetError):
                        input("Yo yo yo, would love to find you something you can download,\nbut I can't connect to the internet!")
            
            # Quit Command
            
                elif cinput[0] == listofcommands[2]:
                    os.system("cls")
                    break
            
            # List Downloaded Content Command
            
                elif cinput[0] == listofcommands[3]:
                    downloaded = os.listdir("Apps/")
                    for i in downloaded:
                        if i != "api.py" and i != "__pycache__" and i != "gamedata":
                            print(i.replace(".py", ""))
                    input("\nThat's all the apps you have.")
                    os.system("cls")
            
            # Music Command
                
                elif cinput[0] == listofcommands[4]:
                    musicorno = input("Do you want to play music? (Y/N) > ")
                    if str.lower(musicorno).startswith("y") and p == None:
                        music = os.listdir("music")
                        n = 1
                        for i in music:
                            print(str(n) + ". " + i)
                        selection = input("Select your music of choice (with the file extension) > ")
                        p = api.playaudio(os.path.dirname(__file__) + "\\" + selection)
                    elif str.lower(musicorno).startswith("n") and p == None:
                        p.terminate()
                        p = None
                    elif str.lower(musicorno).startswith("y") and p != None:
                        input("Cannot play more than one track at a time.")
                    elif str.lower(musicorno).startswith("n") and p == None:
                        input("Cannot stop the music when none is playing.")
            elif cinput[0] in listofmodularcommands:
            # Download Command
            
                if cinput[0] == listofmodularcommands[0]:
                    if api.ismore(cinput, downloadargs):
                        try:
                            r = requests.get('https://programhub.survivalist260.repl.co/static/list.txt')
                            if r.status_code and cinput[1] in r.text:
                                r = requests.get('https://programhub.survivalist260.repl.co/static/' + cinput[1] + '.txt')
                                cr = r.text
                                with open("Apps/" + cinput[1] + ".py", "w") as file:
                                    file.write(cr)
                                    print("File Downloaded Successfully!\nIf you already had the file, it was overwritten.")
                                    input("That's a good way to update.")
                                    os.system("cls")
                            else:
                                input("Pfft, are you SUURE that's something on the list of things you can download? I knew you were an idiot.")
                        except(ConnectionError):
                            input("Unable to connect to the server.")
                    else:
                        print("YOU'RE DOING IT WRO-\nWAIT.. WHAT THE FUCK ARE YOU DOING?")
                        input("What the shit.")
                        input("Tell me what to download, idiot.")
                    os.system("cls")

            # Run Command
            
                elif cinput[0] == listofmodularcommands[1]:
                    downloaded = os.listdir("Apps/")
                    cinput[1] = cinput[1] + ".py"
                    if cinput[1] in downloaded:
                        title()
                        os.system("py Apps/" + cinput[1])
                        input("\nThe App was executed. That's the result. Now go away by pressing Enter.")
                    else:
                        input("Is that a file though?")
                    os.system("cls")
            
            # Delete Command
            
                elif cinput[0] == listofmodularcommands[2]:
                    downloaded = os.listdir("Apps/")
                    cinput[1] = cinput[1] + ".py"
                    if cinput[1] in downloaded:
                        if cinput[1] == "api.py" or cinput[1] == "__pycache__": input("Seems like you made a mistake in the file name. Try putting the exact name in.")
                        else:
                            os.remove("Apps/" + cinput[1])
                            input("\nApp slashed out of existence. Press Enter to go back to Title..\n(I have to remember every time that it's one of you lot I'm talking to and do have to include that message)")
                    else: input("Seems like you made a mistake in the file name. Try putting the exact name in.")
                    os.system("cls")
                
            
            # What if it's gibberish?
            
            else:
                input("I don't think that's a command.")
                os.system("cls")
    
    return 0
