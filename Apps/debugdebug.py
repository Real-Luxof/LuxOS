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

height = 300
width = 300

array = []
for i in range(height):
    array.append([])
    for j in range(width):
        #array[-1].append(minus)
        if j != 70:
            array[-1].append(minus)
        elif 150 < i < 200:
            array[-1].append(dollar)
        else:
            array[-1].append(minus)

stoptime = False

def display():
    global array
    global stoptime
    screen = api.setres(600, 600)

    while not stoptime:
        
        
        api.display(screen, array, 2, 2)
        if api.isquit():
            break

def raycast(target_X: int, target_Y: int) -> None:
    global array
    half_array_size = len(array) // 2
    
    line = list(bresenham(half_array_size, half_array_size, target_X, target_Y))

    for coordinates in line:
        #print(coordinates)
        if array[coordinates[1]][coordinates[0]].passable:
            array[coordinates[1]][coordinates[0]] = hash
        else:
            break
    sleep(0.0001)

#def raycast_thread(target_X: int, target_Y: int) -> None:
#    raycast(target_X, target_Y)

def raycast_rays() -> None:
    global array
    length_of_display = len(array)
    
    for i in range(0, length_of_display - 1):
        #Thread(target=raycast_thread, args=[i, 0], daemon=True).start()
        raycast(i, 0)
        
        #Thread(target=raycast_thread, args=[length_of_display - 1, i], daemon=True).start()
        raycast(length_of_display - 1, i)
        
        #Thread(target=raycast_thread, args=[(length_of_display - 1) - i, length_of_display - 1], daemon=True).start()
        raycast((length_of_display - 1) - i, length_of_display - 1)
        
        #Thread(target=raycast_thread, args=[0, (length_of_display - 1) - i], daemon=True).start()
        raycast(0, (length_of_display - 1) - i)

displaythread = Thread(target=display)
displaythread.start()

try:
    raycast_rays()
except KeyboardInterrupt:
    stoptime = True

displaythread.join()
