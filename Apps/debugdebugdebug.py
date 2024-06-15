import api
from gamedata.integri.utilityfolder.blocks import *
from threading import Thread

casting_world = []
originals = []
world = api.optimized_generate(
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
    global originals
    half_casting_world_size = len(casting_world) // 2
    impassable_hits = 0
    impassable_limit = 3
    
    line = list(api.bresenham(half_casting_world_size, half_casting_world_size, target_X, target_Y))

    for coordinates in line:
        # You will recieve no comment with this code. Fuck you, I'm tired and I want to get this
        # whole raycasting thing over with.
        Y = coordinates[1]
        X = coordinates[0]

        #if originals[Y][X].passable or originals[Y][X].type == "entity" and impassable_hits > 0:
        #    casting_world[Y][X] = originals[Y][X]
        #    impassable_hits += 1
        
        if originals[Y][X].passable or originals[Y][X].type == "entity":
            casting_world[Y][X] = originals[Y][X]
        
        elif not originals[Y][X].passable and not originals[Y][X].type == "entity" and not impassable_hits >= impassable_limit:
            casting_world[Y][X] = originals[Y][X]
            impassable_hits += 1
        
        elif not originals[Y][X].passable and not originals[Y][X].type == "entity" and impassable_hits >= impassable_limit:
            casting_world[Y][X] = originals[Y][X]
            break
        #if not casting_world[Y][X].passable and not casting_world[Y][X].type == "entity":
        #    casting_world[Y][X] = Bdr
        #    break
        #if casting_world[Y][X].passable:
        #    casting_world[Y][X].temp_image = casting_world[Y][X].image
        #else:
        #    try:
        #        casting_world[Y][X].temp_image = casting_world[Y][X].image
        #        break
        #    except AttributeError:
        #        casting_world[Y][X].temp_image = casting_world[Y][X].character


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
    global originals
    global quittime
    global frames
    global world
    plr.position[1] = len(world) // 2
    plr.position[0] = len(world[0]) // 2
    while not api.isquit():
        # LET HIM COOK :fire:
#                   cookingdisplayoutput = []
        displayoutput = []
        casting_world = []

#                    for n in range(worldtype[0]):
#                        cookingdisplayoutput.append([])
#
        #    for m in range(100):
        #        cookingdisplayoutput[n].append(air(world, plr.position[1] - (n - worldtype[0]), plr.position[0] - (m - 50)))

#                    cookingdisplayoutput = applylightingsystem(cookingdisplayoutput)

        # I came up with a math formula to line up player coordinates
        # between cookingdisplayoutput and displayoutput
        # coordinate of player in cookingdisplayoutput =
        # X - (X - (X_radius_around_player + 1))

        for n in range(100):
            displayoutput.append([])

            for m in range(100):
                displayoutput[-1].append(air(world, plr.position[1] - (n - 50), plr.position[0] - (m - 50)))

        displayoutput = list(reversed(displayoutput))
        
        for Y in range(len(displayoutput)):
            new_row = []
            for X in range(len(displayoutput)):
                new_row.append(Bdr)
            casting_world.append(new_row)
        
        originals = displayoutput
        raycast_rays()
        displayoutput = casting_world

        #for y_level in displayoutput:
        #    for block in y_level:
        #        block.image = block.temp_image
        
        api.display(screen, displayoutput, 8, 6)
        #frames += 1
        api.wait(1/60) # "60 fps"
        # How does this work again
        # lmao this shit ain't even CLOSE to 60 fps it runs at *~15*
        # how does this run at ~23 fps

screen = api.setres(800, 600)
displaythread(screen)
