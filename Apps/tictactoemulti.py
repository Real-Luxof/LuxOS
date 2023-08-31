import api
try: import requests
except(ModuleNotFoundError): api.install("requests"); import requests
try: from flask import *
except(ModuleNotFoundError): api.install("Flask"); from flask import *
from threading import Thread

global game
game = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def calculatechoice(choice, drop, gamen):
    if choice < 10 and choice > 0:
        if choice == 1 and gamen[0][0] == ' ':
            gamen[0][0] = drop
            return gamen
        elif choice == 2 and gamen[0][1] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 3 and gamen[0][2] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 4 and gamen[1][0] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 5 and gamen[1][1] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 6 and gamen[1][2] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 7 and gamen[2][0] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 8 and gamen[2][1] == ' ':
            gamen[0][1] = drop
            return gamen
        elif choice == 9 and gamen[2][2] == ' ':
            gamen[0][1] = drop
            return gamen
        else:
            return False
    else:
        return False

def host(port):
    global game
    app = Flask(__name__)
    
    @app.route('/',methods=['GET'])
    def establishconnection():
        args = request.args
        args = args.to_dict()
        dataadd = args["dataadd"]
        if dataadd != False:
            game = dataadd
        return game
    
    app.run(host='127.0.0.1',port=int(port))

while True:
    api.clear()
    userinput = str.lower(input("Host or connect? (H/C) > "))
    if userinput.startswith("h"):
        server = Thread(target=host,args=[5000])
        server.run()
        params = {"dataadd": False}
        r = requests.get("http://127.0.0.1", params=params)
        r = r.text
        previousgame = None
        while True:
            for i in r:
                print("|",end="")
                for n in i:
                    print(n,end="|")
                print()
            if r != previousgame:
                choice = input("1-9: you choose > ")
                game = calculatechoice(choice,"X",game)
    elif userinput.startswith("c"):
        ipinput = str(input("insert server IP > "))
        params = {"dataadd": False}
        r = requests.get("http://" + ipinput, params=params)
        r = r.text
        previousgame = None
        while True:
            api.clear()
            for i in r:
                print("|",end="")
                for n in i:
                    print(n,end="|")
                print()
            if r != [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] and r != previousgame:
                choice = input("1-9: you choose > ")
                game = calculatechoice(choice,"O",game)
