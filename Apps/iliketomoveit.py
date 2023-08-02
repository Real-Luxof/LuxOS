from os import system as sys
import api

print("You must type left, right, up, or down\nthen press enter to move your player character.")
print("A = Air")
print("P = Player")
input("Start Game?")
api.clear()

A = ["A", "A", "A", "A", "A"]
B = ["A", "A", "A", "A", "A"]
C = ["A", "A", "P", "A", "A"]
D = ["A", "A", "A", "A", "A"]
E = ["A", "A", "A", "A", "A"]

Y = C
X = 2
playerposition = Y[X]

while True:
    api.clear()
    display = api.don5(A,B,C,D,E)

    for i in display:
        print(i)

    playerinput = input("> ")

    if playerinput.startswith("l"):
        if X != 0:
            Y[X] = "A"
            X -= 1
            playerposition = Y[X]
            Y[X] = "P"
        else: input("Illegal move.")
    elif playerinput.startswith("r"):
        if X != 4:
            Y[X] = "A"
            X += 1
            playerposition = Y[X]
            Y[X] = "P"
        else: input("Illegal move.")
    elif playerinput.startswith("u"):
        if Y != A:
            if Y == B:
                Y[X] = "A"
                Y = A
                playerposition = Y[X]
                A[X] = "P"
            elif Y == C:
                Y[X] = "A"
                Y = B
                playerposition = Y[X]
                B[X] = "P"
            elif Y == D:
                Y[X] = "A"
                Y = C
                playerposition = Y[X]
                C[X] = "P"
            elif Y == E:
                Y[X] = "A"
                Y = D
                playerposition = Y[X]
                D[X] = "P"
        else: input("Illegal move.")
    elif playerinput.startswith("d"):
        if Y != E:
            if Y == A:
                Y[X] = "A"
                Y = B
                playerposition = Y[X]
                B[X] = "P"
            elif Y == B:
                Y[X] = "A"
                Y = C
                playerposition = Y[X]
                C[X] = "P"
            elif Y == C:
                Y[X] = "A"
                Y = D
                playerposition = Y[X]
                D[X] = "P"
            elif Y == D:
                Y[X] = "A"
                Y = E
                playerposition = Y[X]
                E[X] = "P"
        else: input("Illegal move.")
    elif playerinput.startswith("q"):
        break
