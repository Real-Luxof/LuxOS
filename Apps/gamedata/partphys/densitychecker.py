#  I spent way too much time on this only to realize I don't need it
# Nvm I do need it
def match_coordinates(X: int, Y: int, attraction_table, world) -> dict:
    weight_x = 0
    weight_y = 0

    match Y:
        case 0:
            weight_y += attraction_table[] 1
            if X < 2:
                weight_x += 1
            elif X > 2:
                weight_x -= 1
        case 1:
            match X:
                case 0: weight_x += 1; weight_y += 1
                case 1: weight_x += 2; weight_y += 2
                case 2: weight_y += 2
                case 3: weight_x -= 2; weight_y += 2
                case 4: weight_x -= 1; weight_y += 1
        case 2:
            match X:
                case 0: weight_x += 1
                case 1: weight_x += 2
                case 3: weight_x -= 2
                case 4: weight_x -= 1
        case 3:
            match X:
                case 0: weight_x += 1; weight_y -= 1
                case 1: weight_x += 2; weight_y -= 2
                case 2: weight_y -= 2
                case 3: weight_x -= 2; weight_y -= 2
                case 4: weight_x -= 1; weight_y -= 1
        case 4:
            weight_y -= 1
            if X < 2:
                weight_x += 1
            elif X > 2:
                weight_x -= 1

    return {"Weight X": weight_x, "Weight Y": weight_y}

def check_density(particle, area: list[list]) -> dict:
    """Checks density for you and gives directions to move the block accordingly.

    Args:
        area (list[list]): A 5x5 area around the particle. Must be centered on the particle.
        particle (api.block class): The particle you want directions for.

    Returns (list): Directions. It will be None if there is no movement in that direction.
    """
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
                weights = match_coordinates(particle_index_X, particle_index_Y)

                #if particle_index_X < 2:
                #    weight_X += 1
                #elif particle_index_X > 2:
                #    weight_X -= 1
                #
                #if particle_index_Y < 2:
                #    weight_Y += 1
                #elif particle_index_Y > 2:
                #    weight_Y -= 1
                weight_X += weights["Weight X"]
                weight_Y += weights["Weight Y"]

    # Turn weight into actual directions.
    if weight_X < 0:
        direction_X = "a"
    elif weight_X > 0:
        direction_X = "d"

    if weight_Y < 0:
        direction_Y = "w"
    elif weight_Y > 0:
        direction_Y = "s"

    return {"Left or right": direction_X, "Up or down": direction_Y, "Force_X": weight_X, "Force_Y": weight_Y}
