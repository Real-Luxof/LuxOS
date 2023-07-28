from api import *

while True:
    clear()

    pinput = input("Calc > ")
    cinput = pinput.split()

    if cinput[0] == "quit":
        break
    if ismore(cinput,0) and ismore(cinput,1) and ismore(cinput,2):
        if isint(cinput[0]) and isoperator(cinput[1]) and isint(cinput[2]):
            calculationproduct = calculate(int(cinput[0]), cinput[1], int(cinput[2]))
            if ismore(cinput,3) and ismore(cinput,4):
                if isoperator(cinput[3]) and isint(cinput[4]):
                    calculationproduct = calculate(calculationproduct, cinput[3], cinput[4])
                    if ismore(cinput,5) and ismore(cinput,6):
                        if isoperator(cinput[5]) and isint(cinput[6]):
                            calculationproduct = calculate(calculationproduct, cinput[5], cinput[6])
                        else: input("Problem found in 6th, and/or 7th argument(s).")
                else: input("Problem found in 4th, and/or 5th argument(s).")
        else: input("Problem found in 1st, 2nd, and/or 3rd argument(s).")
        input(calculationproduct)
    else: input("Insufficient arguments for at least one mathematical operation.")
