import api
try: import requests
except(ModuleNotFoundError): api.install("requests"); import requests
try: from flask import *
except(ModuleNotFoundError): api.install("Flask"); from flask import *
from threading import Thread

game = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
activeplayer = 'X'

def host(port):
    global game
    app = Flask(__name__)
    
    @app.route('/',methods=['GET'])
    def checkstate():
        global game
        return game
    
    @app.route('/turn',methods=['POST'])
    def doaturn():
        # Get that shit
        global game
        global activeplayer
        player = request.form['player']
        gamestate = list(request.form['gamestate']) # put list() around it cuz better safe than sorry
        
        # Pass it through the grand filter of if it's not the active player do fuck all
        if player != activeplayer: return game
        
        # If it is the active player actually take it and switch the active player to the next player
        game = gamestate
        
        match activeplayer:
            case "X": activeplayer = "O"
            case "O": activeplayer = "X"
        
    
    app.run(host='127.0.0.1',port=int(port))

while True:
    
    # Ask if Host or connect.
    api.clear()
    userinput = str.lower(input("Host or connect? (H/C) > "))
    
    # If hosting:
    if userinput.startswith("h"):
        
        # Host the server
        server = Thread(target=host,args=[5000])
        server.run()
        
        while True:
            # Get the current game state.
            req = requests.get("http://127.0.0.1:5000/")
            req = list(req.text)
            
            # Print the active player and game's state.
            print(f"- Active Player: {activeplayer} -")
            print("- To refresh the board type anything in -") # Too lazy to refresh automatically
            for boxlayer in req:
                print("|",end="")
                for box in boxlayer:
                    print(box,end="|")
            
            # Take a choice, then tell the server what player you are.
            # By default the host goes first and is X.
            choice = input("Number (1-9) >")
            
            # Use the power of MATH and LOGIC to dynamically drop drops on the correct box if it's empty.
            proposedgame = game
            choice -= 1
            if choice >= 0 or choice <= 8:
                if proposedgame[choice // 3][choice % 3] == ' ':
                    proposedgame[choice // 3][choice % 3] = "X"
            params = {'player':'X', 'gamestate':proposedgame}
            
            # Ask the server to take our version of the game, and it decides whether it wants to or not.
            # LMAO dis has no security if u active player then u do anything u want to the board
            game = requests.post("http://127.0.0.1:5000/turn", params=params).text

    elif userinput.startswith("c"):
        
        ipinput = str(input("insert server IP with port > "))
        
        while True:
            # Get the current game state.
            req = requests.get("http://" + ipinput + "/")
            req = list(req.text)
            
            # Print the active player and game's state.
            print(f"- Active Player: {activeplayer} -")
            print("- To refresh the board type any number in -") # Too lazy to refresh automatically
            for boxlayer in req:
                print("|",end="")
                for box in boxlayer:
                    print(box,end="|")
            
            # Take a choice, then tell the server what player you are.
            # By default the host goes first and is X.
            choice = input("Number (1-9) >")
            
            # Use the power of MATH and LOGIC to dynamically drop drops on the correct box if it's empty.
            proposedgame = game
            choice -= 1
            if choice >= 0 or choice <= 8:
                if proposedgame[choice // 3][choice % 3] == ' ':
                    proposedgame[choice // 3][choice % 3] = "O"
            params = {'player':'O', 'gamestate':proposedgame}
            
            # Ask the server to take our version of the game, and it decides whether it wants to or not.
            # LMAO dis has no security if u active player then u do anything u want to the board
            game = requests.post("http://" + ipinput + "/turn", params=params).text
