def terminal():

    from os import listdir, remove, system, chdir
    import urllib.request
    from Apps import api
    from json import loads
    try: import requests
    except(ModuleNotFoundError): system("pip install requests")

    from Apps import api
    chdir("Apps")
    
    def title():
        api.clear()
    
    commands = [
        "help", "search", "quit", "find", "download", "run", "delete"
    ]
    command_help_messages = {
        "help": "Displays the list of commands.\nSyntax: help\n",
        "search": "Searches for a list of downloadable applications online.\nSyntax: search\n",
        "quit": "Quits this program.\nSyntax: quit\n",
        "find": "Lists all downloaded applications.\nSyntax: find\n",
        "download": "Downloads an app from the internet.\nSyntax: download [app_name]\n",
        "run": "Runs an app on your machine.\nSyntax: run [app_name]\n",
        "delete": "Deletes an app from your machine.\nSyntax: delete [app_name]\n"
    }
    
    # Main App
    
    print("Remember: type \"help\" for a list of commands.")
    api.wait_key("Enter")
    
    while True:
        title()
        rawinput = input("> ")
        
        cinput = rawinput.split()
        
        if cinput == []:
            continue
        elif cinput[0] not in commands:
            continue
        
        cinput[0] = str.lower(cinput[0])
        
        if cinput[0] == "quit":
            return 0
        
        
        elif cinput[0] == "help":
            for command in commands:
                print(f"{command}: {command_help_messages[command]}")
            api.wait_key("Enter")
            continue
        
        
        elif cinput[0] == "search":
            try:
                r = requests.get("https://raw.githubusercontent.com/Real-Luxof/LuxOS/main/list.txt")
            except Exception as err:
                # bro tip: prefix all your errors with "User error".
                print(f"User error: {err}")
                api.wait_key("Enter")
                continue
            
            if not r.status_code:
                print(f"Server returned {r.status_code}")
                api.wait_key("Enter")
                continue
            
            print("Here's a list of apps you can download:")
            for line in r.text.split("\n"):
                if line.startswith("#"):
                    continue
                print(line)
            api.wait_key("Enter")
            continue
        
        
        elif cinput[0] == "find":
            files = listdir()
            files = api.stripimportant(files, ["api.py", "__pycache__", "gamedata"])
            print("Here's a list of apps you have:")
            
            for file in files:
                print(file)
            
            api.wait_key("Enter")
            continue
        
        
        elif cinput[0] == "download":
            latest_trace = "reachableindex"
            
            if not api.reachableindex(cinput, 1):
                print(f"Syntax: download [app_name]")
                api.wait_key("Enter")
                continue
            
            try:
                latest_trace = "list.txt"
                
                req = requests.get("https://raw.githubusercontent.com/Real-Luxof/LuxOS/main/list.txt").text
                if cinput[1] not in req:
                    raise NameError("You cannot download that.")
                
                latest_trace = "retrieving app"
                urllib.request.urlretrieve(f"https://raw.githubusercontent.com/Real-Luxof/LuxOS/main/Apps/{cinput[1]}", f"{cinput[1]}")
                
                latest_trace = "dependencies getting"
                req: dict = loads(requests.get("https://raw.githubusercontent.com/Real-Luxof/LuxOS/main/dependencies.json").text)
                
                if cinput[1] not in req.keys():
                    print("App downloaded.")
                    api.wait_key("Enter")
                    continue
                
                latest_trace = "keyerror maybe?"
                dependency_list = req[cinput[1]]
                
                for dependency in dependency_list:
                    if dependency[0] == "folder":
                        latest_trace = "folder " + dependency[1]
                        
                        api.checkandmake(dependency[1])
                    
                    elif dependency[0] == "file":
                        latest_trace = f"file {dependency[1]} {dependency[2]}"
                        
                        urllib.request.urlretrieve(
                            f"https://raw.githubusercontent.com/Real-Luxof/LuxOS/main/Apps/{dependency[1]}",
                            dependency[2]
                        )
                
                print("App downloaded.")
                
            except Exception as err:
                print(f"The following error occured: {err}\ntrace: {latest_trace}")
            
            api.wait_key("Enter")
            continue
        
        
        elif cinput[0] == "run":
            if not api.reachableindex(cinput, 1):
                print(f"Syntax: run [app_name]")
                api.wait_key("Enter")
                continue
            
            files = listdir()
            files = api.stripimportant(files, ["api.py", "__pycache__", "gamedata"])
            
            if cinput[1] not in files:
                print("No such app found. Did you make a typo?")
                api.wait_key("Enter")
                continue
            
            system(f"py {cinput[1]}")
            print("App executed.")
            api.wait_key("Enter")
            continue
                
        
        elif cinput[0] == "delete":
            if not api.reachableindex(cinput, 1):
                print(f"Syntax: delete [app_name]")
                api.wait_key("Enter")
                continue
            
            files = listdir()
            files = api.stripimportant(files, ["api.py", "__pycache__", "gamedata"])
            
            if cinput[1] not in files:
                print("No such app found. Did you make a typo?")
                api.wait_key("Enter")
                continue
            
            remove(f"{cinput[1]}")
            print("App deleted.")
            api.wait_key("Enter")
            continue
