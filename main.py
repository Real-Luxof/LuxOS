def bootloader():

    # Boot

    from os import system
    from time import sleep as wait
    import sys
    
    system("title [ LuxOS Bootloader ]")
    def typewriter(string):
        for char in string:
            print(char, end="")
            sys.stdout.flush()
            wait(1/120)
        print()
    typewriter("Welcome.")
    input()
    system("cls")

    typewriter("  _          _    _     _      _  ")
    typewriter(" | |        | |  | |    \\ \\   / / ")
    typewriter(" | |        | |  | |     \\ \\ / /  ")
    typewriter(" | |        | |  | |      \\   /   ")
    typewriter(" | |        | |  | |      /   \\   ")
    typewriter(" | |___     | |__| |     / / \\ \\  ")
    typewriter(" |_____|    |______|    /_/   \\_\\ ")
    typewriter("    _______           ________    ")
    typewriter("   |  ___  |         |   _____|   ")
    typewriter("   | |   | |         |  |_____    ")
    typewriter("   | |   | |         |_____   |   ")
    typewriter("   | |___| |          _____|  |   ")
    typewriter("   |_______|         |________|   ")
    typewriter("                                  ")
    typewriter("           Loading...")
    import interface

    system("title [ LuxOS ]")
    interface.terminal()

if __name__ == "__main__":
    bootloader()
