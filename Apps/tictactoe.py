from api import install, wait, wait_any, isint, clear
from threading import Thread

try:
    from colorama import just_fix_windows_console
except ModuleNotFoundError:
    install("colorama")
    from colorama import just_fix_windows_console

just_fix_windows_console()
clear()

global game
global quit_time
game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
quit_time = False

def print_game(game):
    # not as good as it could be but it's functional
    # and i don't care
    for Y_index in range(len(game)):
        if Y_index > 0:
            print("-----------")
        for X_index in range(len(game[Y_index])):
            square = game[Y_index][X_index]
            
            if X_index == 1:
                print(end=" | ")
            elif X_index == 0:
                print(end=" ")
            
            print(end=square)
            
            if X_index == 1:
                print(end=" | ")
            elif X_index == 2:
                print()

def display_thread():
    global game
    global quit_time
    while not quit_time:
        print_game(game)
        print(end="\x1b[5A\r")

def game_hotseat():
    global game
    global quit_time
    
    active_player = "X"
    
    print("1-9 to select a square.")
    print("ESC to leave.")
    Thread(target=display_thread).start()
    
    while True:
        key = ""
        
        while not isint(key) and key != "esc":
            key = wait_any()
        
        if key == "esc":
            quit_time = True
            break
        
        key = int(key) + 1
        
        Y = key + 1 // 3
        X = key % 3
        
        game[Y][X] = active_player
        
        wait(0.1)
        
        match active_player:
            case "X": active_player = "O"
            case "O": active_player = "X"
    
    #display_thread()

if __name__ == '__main__':
    game_hotseat()
