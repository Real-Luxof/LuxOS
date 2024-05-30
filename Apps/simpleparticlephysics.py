print("Hold on, I'm getting shit ready for you.")

# Import the game engine.
import api

# Make path variables.
partphys = "gamedata\\partphys"

# Check if partphys exists inside gamedata. If it doesn't, the engine will make it.
api.checkandmake(partphys)

# Check if generator.py exists inside partphys. If it doesn't, make it.
if not api.checkpath(f"{partphys}\\generator.py"):
    with open(f"{partphys}\\generator.py", "w") as f:
        f.write("""from ..api import block
from random import choice
from random import randint

black_void = block(varname="black_void", image="#000000", passable=True)


def generate(colors: list,
             width: int,
             height: int,
             chance_of_void: float) -> list:
    \"\"\"Generates a big ass list filled with either black or a color/particle.

    Args:
        colors (list): A list of all the colors/particles.
        width (int): The width of the world.
        height (int): The height of the world.
        chance_of_void (float): What chance is there that there will be black void instead of a particle?
        
        Examples for chance_of_void:
            The probability is calculated like
            if randint(1, 100) < chance_of_void: world[-1].append(black_void)

    Returns:
        list: The entire world that was just generated.
    \"\"\"
    world = []

    for timesY in range(height):
        world.append([])
        for timesX in range(width):
            if randint(1, 100) < chance_of_void:
                world[-1].append(black_void)
            else:
                world[-1].append(choice(colors))

    return world""")

if not api.checkpath(f"{partphys}\\densitychecker.py"):
    with open(f"{partphys}\\densitychecker.py", "w") as f:
        f.write("""# I spent way too much time on this only to realize I don't need it
#def match_coordinates(X: int, Y: int) -> dict:
#    weight_x = 0
#    weight_y = 0
#
#    match Y:
#        case 0:
#            weight_y += 1
#            if X < 2:
#                weight_x += 1
#            elif X > 2:
#                weight_x -= 1
#        case 1:
#            match X:
#                case 0: weight_x += 1; weight_y += 1
#                case 1: weight_x += 2; weight_y += 2
#                case 2: weight_y += 2
#                case 3: weight_x -= 2; weight_y += 2
#                case 4: weight_x -= 1; weight_y += 1
#        case 2:
#            match X:
#                case 0: weight_x += 1
#                case 1: weight_x += 2
#                case 3: weight_x -= 2
#                case 4: weight_x -= 1
#        case 3:
#            match X:
#                case 0: weight_x += 1; weight_y -= 1
#                case 1: weight_x += 2; weight_y -= 2
#                case 2: weight_y -= 2
#                case 3: weight_x -= 2; weight_y -= 2
#                case 4: weight_x -= 1; weight_y -= 1
#        case 4:
#            weight_y -= 1
#            if X < 2:
#                weight_x += 1
#            elif X > 2:
#                weight_x -= 1
#
#    return {"Weight X": weight_x, "Weight Y": weight_y}

def check_density(particle, area: list[list]) -> dict:
    \"\"\"Checks density for you and gives directions to move the block accordingly.

    Args:
        area (list[list]): A 5x5 area around the particle. Must be centered on the particle.
        particle (api.block class): The particle you want directions for.

    Returns (list): Directions. It will be None if there is no movement in that direction.
    \"\"\"
    # Initialize variables.
    length_of_area = len(area)
    area_iterable = range(length_of_area)
    center_particle_coordinates = length_of_area // 2
    varname_of_target_particle = ""

    # Initialize weight.
    weight_X = 0
    weight_Y = 0

    # Initiate directions.
    direction_X = None
    direction_Y = None

    # Calculate weight.
    for particle_index_Y in area_iterable:
        for particle_index_X in area_iterable:
            varname_of_target_particle = area[particle_index_Y][particle_index_X].varname

            # Don't waste our time if it isn't an actual particle.
            if varname_of_target_particle != "black_void":
                continue
            # Don't waste our time if it's the middle of the array, either.
            elif particle_index_Y == 2 == particle_index_X:
                continue

            if varname_of_target_particle in particle.attracted:
                #weights = match_coordinates(particle_index_X, particle_index_Y)

                if particle_index_X < 2:
                    weight_X += 1
                elif particle_index_X > 2:
                    weight_X -= 1

                if particle_index_Y < 2:
                    weight_Y += 1
                elif particle_index_Y > 2:
                    weight_Y -= 1
                #weight_X += weights["Weight X"]
                #weight_Y += weights["Weight Y"]

    # Turn weight into actual directions.
    if weight_X < 0:
        direction_X = "a"
    elif weight_X > 0:
        direction_X = "d"

    if weight_Y < 0:
        direction_Y = "w"
    elif weight_Y > 0:
        direction_Y = "s"

    return {"Left or right": direction_X, "Up or down": direction_Y}
""")

# Separated the variables so as not to look like a clusterfuck.

# Since "attracted" usually isn't expected and thus not an attribute
# in the [block] class, we're gonna hack the game engine to set that
# attribute anyway.
red = api.block(varname="red", image="#AA0000", passable=False)
red.__setattr__("attracted", ["green", "yellow", "blue", "purple", "white"])

green = api.block(varname="green", image="#00AA00", passable=False)
green.__setattr__("attracted", ["yellow", "white", "cyan"])

yellow = api.block(varname="yellow", image="#AAAA00", passable=False)
yellow.__setattr__("attracted", ["purple", "red"])

blue = api.block(varname="blue", image="#0000AA", passable=False)
blue.__setattr__("attracted", ["white", "green"])

purple = api.block(varname="purple", image="#AA00AA", passable=False)
purple.__setattr__("attracted", ["blue", "green", "cyan"])

cyan = api.block(varname="cyan", image="#00AAAA", passable=False)
cyan.__setattr__("attracted", [])

white = api.block(varname="white", image="#AAAAAA", passable=False)
white.__setattr__("attracted", ["cyan", "yellow"])

black_void = api.block(varname="black_void", image="#000000", passable=True)

# Passed into the generator later.
particles = [red, green, yellow, blue, purple, cyan, white]

# Functions.
def findarea(X: int, Y: int, areaX: int, areaY: int, world: list[list]) -> list[list]:
    """Finds a [areaX]*[areaY] area from [world], centered around [center].
    [X] and [Y] are the coordinates of [center].
    If a coordinate is out of bounds, it simply replaces it with [black_void]."""
    area = []
    # [appendablevoid] is appended to [area] when [Ycoord] is out of bonds,
    # Removing the need to scroll through every X coordinate on [Ycoord].
    # black_void is brought into this scope to reduce function arguments.
    global black_void
    appendablevoid = []

    for Xcoord in range(X - areaX, X + areaX):
        appendablevoid.append()

    for Ycoord in range(Y - areaY, Y + areaY):
        if not api.reachableindex(world, Ycoord):
            area.append(appendablevoid)
            continue

        area.append([])
        for Xcoord in range(X - areaX, X + areaX):
            if api.reachableindex(world[Ycoord], Xcoord):
                area[-1].append(world[Ycoord][Xcoord])

# Unconventional, but import the generator now.
from gamedata.partphys import generator
from gamedata.partphys import densitychecker

api.clear()

# Make a screen.
api.initiatewindow()
screen = api.setres(800, 600)

# Generate the world.
world = generator.generate(colors=particles, width=400, height=300, chance_of_void=99.99)

# Main game loop
while not api.isquit():
    # Display the screen first. Yeah, we're doing updates and frames in the same thread.
    # Do I care? No.
    api.display(screen, world, 2, 2)

    # Calculate density and move accordingly.
    for Y in range(len(world)):
        for X in range(Y):
            area_of_block = findarea(X, Y, 5, 5, world)
            block = world[Y][X]
            directions = densitychecker.check_density(block, area_of_block)
            move_result = world

            if directions["Left or right"] != None:
                move_result = block.move(Y, X, directions["Left or right"], move_result, black_void)
            if directions["Up or down"] != None:
                move_result = block.move(Y, X, directions["Up or down"], move_result, black_void)
