from ..api import block
from random import choice
from random import randint

black_void = block(varname="black_void", image="#000000", passable=True)


def generate(colors: list,
             width: int,
             height: int,
             chance_of_void: float) -> list:
    """Generates a big ass list filled with either black or a color/particle.

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
    """
    world = []

    for timesY in range(height):
        world.append([])
        for timesX in range(width):
            if randint(1, 100) < chance_of_void:
                world[-1].append(black_void)
            else:
                world[-1].append(choice(colors))

    return world
