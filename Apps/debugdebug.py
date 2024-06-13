from bresenham import bresenham
from time import sleep
from os import system
from threading import Thread
import api

class MinusSign:
    passable = True
    image = "#000000"

    def __repr__(self):
        return self.image

class Hash:
    passable = True
    image = "#FFFFFF"

    def __repr__(self):
        return self.image

class DollarSign:
    passable = False
    image = "#FF0000"

    def __repr__(self):
        return self.image

minus = MinusSign()
hash = Hash()
dollar = DollarSign()

height = 200
width = 200

array = []
for i in range(height):
    array.append([])
    for j in range(width):
        array[-1].append(minus)

stoptime = False

def display():
    global array
    global stoptime
    screen = api.setres(800, 600)

    while not stoptime:
        api.display(screen, array, 4, 3)
        if api.isquit():
            break

def raycast(target_X: int, target_Y: int) -> None:
    global array
    half_array_size = len(array) // 2
    
    line = list(bresenham(half_array_size, half_array_size, target_X, target_Y))

    for coordinates in line:
        if array[coordinates[1]][coordinates[0]].passable:
            array[coordinates[1]][coordinates[0]] = hash
        else:
            break

def raycast_rays():
    global array
    length_of_display = len(array)
    
    for i in range(0, length_of_display - 1):
        raycast(i, 0)
        
        raycast(length_of_display - 1, i)
        
        raycast((length_of_display - 1) - i, length_of_display - 1)
        
        raycast(0, (length_of_display - 1) - i)

displaythread = Thread(target=display)
displaythread.start()

try:
    raycast_rays()
except KeyboardInterrupt:
    stoptime = True

displaythread.join()
