import api
from gamedata.integri.utilityfolder.blocks import *
from threading import Thread

casting_world = []
displayoutput = api.optimized_generate(
    seed=None,
    width=500,
    height=500,
    air=Air,
    stone=Stn,
    limit=api.Limit(252, 298),
    biomes=biomes,
    ore_config=oreconfig,
)
quittime = False


def air(listt, index, index2): # "air" stands for "Add If Reachable"
    global Bdr
    if index >= 0 and index2 >= 0:
        try:
            return listt[index][index2]
        except(IndexError):
            return Bdr
    else:
        return Bdr


def raycast(target_X: int, target_Y: int) -> None:
    global casting_world
    half_casting_world_size = len(casting_world) // 2
    
    line = list(api.bresenham(half_casting_world_size, half_casting_world_size, target_X, target_Y))

    for coordinates in line:
        Y = coordinates[1]
        X = coordinates[0]

        if casting_world[Y][X].passable:
            casting_world[Y][X].temp_image = casting_world[Y][X].image
        else:
            try:
                casting_world[Y][X].temp_image = casting_world[Y][X].image
                break
            except AttributeError:
                casting_world[Y][X].temp_image = casting_world[Y][X].character


def raycast_4_rays(length_of_display, i):
    raycast(i, 0)
    
    raycast(length_of_display - 1, i)
    
    raycast((length_of_display - 1) - i, length_of_display - 1)
    
    raycast(0, (length_of_display - 1) - i)


def raycast_rays():
    global casting_world
    length_of_display = len(casting_world)
    
    for i in range(0, length_of_display - 1):
        #Thread(target=raycast_4_rays(length_of_display, i)).start()
        raycast(i, 0)
        
        raycast(length_of_display - 1, i)
        
        raycast((length_of_display - 1) - i, length_of_display - 1)
        
        raycast(0, (length_of_display - 1) - i)


def displaythread(screen):
    global casting_world
    global quittime
    global frames
    global displayoutput
    while not api.isquit():
        uncdisplayoutput = []
        half_len = len(displayoutput) // 2
        for n in range(100):
            uncdisplayoutput.append([])

            for m in range(100):
                uncdisplayoutput[-1].append(air(displayoutput, half_len - (n - 50), half_len - (m - 50)))
        
        for y_level in uncdisplayoutput:
            for block in y_level:
                block.temp_image = "#000000"
        
        casting_world = uncdisplayoutput
        raycast_rays()
        uncdisplayoutput = casting_world

        for y_level in uncdisplayoutput:
            for block in y_level:
                block.image = block.temp_image
        
        api.display(screen, reversed(uncdisplayoutput), 8, 6)
        #frames += 1
        api.wait(1/60) # "60 fps"
        # How does this work again
        # lmao this shit ain't even CLOSE to 60 fps it runs at *~15*
        # how does this run at ~23 fps

screen = api.setres(800, 600)
displaythread(screen)
