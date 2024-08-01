"""LuxOS Game Engine. *THE* GOAT.
It has a bunch of classes (with methods) that you can use for your game,
along with world generation functions and a VERY basic rendering engine.
Since the rendering engine is very basic, you are given the tools to
write your own rendering engine, namely "Surface", "draw_rectangle",
"update_screen", and "Color".

"powered by pygame and self-hatred, made with pain and suffering. :)"
    -Luxof
"""
# Loading

import time
import os
import random
import multiprocessing
from math import floor
from functools import wraps
from typing import Iterable
from typing import Collection
from typing import NamedTuple
from sys import exit as theactualsysexit

try:
    from playsound import playsound
except ModuleNotFoundError:
    os.system("pip install wheel")
    os.system("pip install playsound")
    from playsound import playsound

try:
    import keyboard
except ModuleNotFoundError:
    os.system("pip install keyboard")
    import keyboard

try:
    import pygame
except ModuleNotFoundError:
    os.system("pip install pygame")
    import pygame

try:
    from bresenham import bresenham
except ModuleNotFoundError:
    os.system("pip install bresenham")
    from bresenham import bresenham

try:
    from perlin_noise import PerlinNoise
except ModuleNotFoundError:
    os.system("pip install perlin-noise")
    from perlin_noise import PerlinNoise

# - Miscellaneous -


# Speed benchmark decorator
# totally did not copy and paste with some modifications
def benchmark(func):
    """This is a wrapper. Use it like @api.benchmark before a function declaration.
    It prints the amount of time that function's execution took every time it executes."""
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        
        time_duration = time_end - time_start
        print(f'Took {time_duration} seconds')
        return result
    
    return wrapper


# Apply chaos
def rand_num(seed: float) -> float:
    """Generates a random number with an overly complicated process where small differences in seed return big differences in output.

    Args:
        seed (float or int): The seed to work with. Same seed gives same output.

    Returns:
        float: A random number.
    """
    seed = (seed * 23082) / 293 + 29000 - 111
    random.seed(seed)
    nums = []
    for i in range(1, random.randint(10, 100)):
        start = random.randint(5908, 29084)
        random.seed(start)
        end = random.randint(start, 509123)
        random.seed(end)
        random.random
        nums.append(random.randint(start, end))
        random.seed(random.randint(start * (i // 2), end * i))
    seed = seed * random.randint(2, 58982)
    random.seed(random.randint(int(abs(seed)), int(abs(seed * 29 - (11 * random.randint(50, 2049))))))
    seed = seed / random.randint(5, 24) + (random.choice(nums) * random.randint(24, 999)) - 290
    return seed


# Strip important files
def stripimportant(strip_from: Iterable[str], strip: Collection[str]) -> list[str]:
    """Strips stuff out of a list."""
    return list(x for x in strip_from if x not in strip)


# Scale a 2D Array
def scale_2dlist(data: list, extendby_Y: int = 2, extendby_X: int = 2) -> list:
    """Lmao bing chat wrote 99.8% of this
    this function just turns up the resolution of a 2D array
    example:
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    if [extendby_Y] and [extendby_X] are set to 2, that will become
    data = [
        [1, 1, 2, 2, 3, 3],
        [1, 1, 2, 2, 3, 3],
        [4, 4, 5, 5, 6, 6],
        [4, 4, 5, 5, 6, 6],
        [7, 7, 8, 8, 9, 9],
        [7, 7, 8, 8, 9, 9]
    ]

    Args:
        data (list): 2D Array.
        extendby (int, optional): . Defaults to 1.

    Returns:
        list: the resulting 2D Array. if [extendby] is set to 1, it somehow returns nothing.
    """
    result = []
    for row in data:
        for _ in range(extendby_Y):
            new_row = [
                item for item in row for _ in range(extendby_X)
            ]  # Duplicate each item in the row
            result.append(new_row)  # Duplicate each row
            # weird method of adding new lists cuz python stores it weird if i don't do this
    return result


# Check if a file exists. If it doesn't, make it.
def checkandmake(pathtofile: str) -> bool:
    """Check if a path exists. If it doesn't, make it and return False."""
    if not os.path.exists(pathtofile):
        os.system(f"md {pathtofile}")
        return False
    else:
        return True

# Check if a file exists. If it doesn't, return False.
def checkpath(pathtofile: str) -> bool:
    """Check if a path exists. If it doesn't, return False."""
    if not os.path.exists(pathtofile):
        return False
    else:
        return True


# Internal Functions


# Add "api." if true
def addapiiftrue(addapi: bool) -> str:
    """DISCLAIMER: This is an internal function. It returns "api." if addapi is true, and returns "" if not.

    Args:
        addapi (bool): Should it return "api." or ""?

    Returns:
        str: Either "api." or "".
    """
    if addapi:
        return "api."
    else:
        return ""


# Get inventory with strings around slots
def putstringsaroundslots(inventory):
    """DISCLAIMER: This is an internal function. It returns inventory.slots but with double quotes around the slots.

    Args:
        inventory (inventory class): Used to pull slots from.

    Raises:
        ValueError: _description_
        TypeError: _description_

    Returns:
        str: A dict inside a string.
    """
    # Initialize variables.
    slots = inventory.slots
    returner = "{"
    returningkeys = list(slots.keys())
    returningvalues = list(slots.values())
    print(returningkeys)
    print(returningvalues)

    # Do the main processing part.
    for slotkeyindex in range(0, len(returningkeys) - 1):
        if type(returningvalues[slotkeyindex]) == block:
            # Put the block's varname if it's a block class.
            # This is done so that OTHER damned error doesn't pop up.
            returner += f'"{returningkeys[slotkeyindex]}": {returningvalues[slotkeyindex].varname},'
        elif returningvalues[slotkeyindex] == None:
            # Put None if the value is also None.
            # This is done so that that damned error doesn't pop up.
            returner += f'"{returningkeys[slotkeyindex]}": None,'
        elif returningvalues[slotkeyindex] == "":
            # Put empty double quotes if the value is also an empty string.
            # This is done so there isn't a key with no value.
            returner += f'"{returningkeys[slotkeyindex]}": "",'
        elif returningvalues[slotkeyindex].startswith("#"):
            # Put double quotes around the value if it starts with a hashtag.
            # This is done a line isn't commented out.
            returner += (
                f'"{returningkeys[slotkeyindex]}": "{returningvalues(slotkeyindex)}",'
            )
        else:
            # Just put the value there if it makes through none of the checks above.
            returner += (
                f'"{returningkeys[slotkeyindex]}": {str(returningvalues[slotkeyindex])},'
            )

    # Return an ouput.
    returner = returner.removesuffix(",")
    returner += "}"
    return returner


def reverse_if_true(some_list: list, boolean: bool):
    """DISCLAIMER: This is an internal function. It uses reversed() on some_list if boolean is True."""
    if boolean:
        return reversed(some_list)
    else:
        return some_list


# Install a module
def install(module):
    os.system("pip install " + module)


# Delete a file
def delete(file):
    os.system("del gamedata\\" + file)


# Math shit -
# Calculate when the operator is a string.
def calculate(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*" or op == "x":
        return num1 * num2
    elif op == "%":
        return num1 % num2
    elif op == "^":
        return num1 ^ num2
    elif op == "/":
        return num1 / num2


# Calculate average.
def average(iterable: list, return_float: bool=False) -> int:
    """Calculate the average of some numbers.

    Args:
        iterable (list): A list with the numbers.
        return_float (bool): Should it round down the answer or possibly return a float? Defaults to False.

    Returns:
        (int): The rounded down average of all the numbers in the list. Returned either if the average wasn't a float or
            if return_float was set to False.
        (float): The average of all the numbers in the list. Returned if the average was a float.
    """
    sigma_iterable = sum(iterable)
    number_of_elements = len(iterable)
    if return_float:
        return sigma_iterable / number_of_elements
    else:
        return floor(sigma_iterable / number_of_elements)


# Clear Screen.
def fullclear():
    """Like os.system('cls'), but with no catch."""
    os.system("cls")


def clear():
    """Like os.system('cls'), but adds the LuxOS logo."""
    os.system("cls")
    print("  _          _    _     _      _  ")
    print(" | |        | |  | |    \\ \\   / / ")
    print(" | |        | |  | |     \\ \\ / /  ")
    print(" | |        | |  | |      \\   /   ")
    print(" | |        | |  | |      /   \\   ")
    print(" | |___     | |__| |     / / \\ \\  ")
    print(" |_____|    |______|    /_/   \\_\\ ")
    print("    _______           ________    ")
    print("   |  ___  |         |   _____|   ")
    print("   | |   | |         |  |_____    ")
    print("   | |   | |         |_____   |   ")
    print("   | |___| |          _____|  |   ")
    print("   |_______|         |________|   ")
    print("                                  ")


# Wait.
def wait(secs):
    time.sleep(secs)

# Time.
def engine_time() -> float:
    """Like time.time()."""
    return time.time()

# - The Checkers -

# Check if one list has an element of the other.
def comparelist(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False


# Check if the string is a math operator.
def isoperator(
    string: str, operators: list[str] = ["+", "-", "*", "x", "%", "/", "//", "^"]
) -> bool:
    """Checks if {string} is one of {operators}.

    Args:
        string (str): Check the summary.
        operators (list[str]): Check the summary. Defaults to ["+", "-", "*", "x", "%", "/", "//", "^"].

    Returns: bool
    """
    if string in operators:
        return True
    else:
        return False


# Check if the variable is a list.
def islist(var):
    if type(var) == list:
        return True
    else:
        return False


# Check if the variable is a string.
def isstring(var):
    if type(var) == str:
        return True
    else:
        return False


# Check if the string is an integer.
def isint(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


# Check if the string is a hex code.
def ishex(string):
    try:
        pygame.Color(string)
        return True
    except ValueError:
        return False


# Check if an index in a list or dictionary exists.
# this variable name "liste" bothers me.
def reachableindex(liste, index: int) -> bool:
    """Check if index in liste exists.

    Args:
        liste (Any indexable type): The variable to index into.
        index (int): The index.

    Returns:
        bool: True if success, False if not.
    """
    
    if type(liste) == list:
        if isint(index):
            if index < len(liste):
                return True
            else:
                return False
        else:
            # wtf is this
            # this is questionable behaviour
            try:
                liste.index(index)
                return True
            except ValueError:
                return False
    else:
        try:
            liste[index]
            return True
        except KeyError:
            return False
        except TypeError:
            return False


# - Engine -


# Playing audio -
def playaudio(relativepathtofile: str):
    path = f"{os.path.dirname(__file__)}\\{relativepathtofile}"
    p = multiprocessing.Process(target=playsound, args=[path])
    p.start()
    return p


def playaudioabs(absolutepathtofile: str):
    p = multiprocessing.Process(target=playsound, args=[absolutepathtofile])
    p.start()
    return p


# To stop the audio, use p.terminate()

# Display -


# Set Display Resolution among some other things.
def setres(width=800, height=600, flags=0, depth=0, display=0, vsync=0) -> pygame.display:
    # Width = width of the screen
    # Height = height of the screen
    # I honestly have no idea what flags, depth, and display do.
    # Vsync = Vertical Sync, prevents screen tearing but does take additional GPU resources.
    # or at least i think that's what vsync means
    screen = pygame.display.set_mode((width, height), flags, depth, display, vsync)
    return screen


# Make a Surface.
def Surface(
    size: tuple[int, int],
    flags: int = None,
    depth: int = None,
    masks = None
) -> pygame.Surface:
    """Size is just tuple(width, height).\nDon't know what flags, depth, and masks are? I don't either."""
    return pygame.Surface(size)


# draw some shit
def draw_rectangle(
    surface: pygame.Surface,
    color: tuple[int, int, int], # type: ignore
    X: int,
    Y: int,
    width: int,
    height: int
):
    """Draws a {color}-colored rectangle {width} wide and {height} tall at {X, Y} on {surface}.
    Do you understand? No? It's just pygame.draw.rect."""
    pygame.draw.rect(surface, color, (X, Y, width, height))


# literally just pygame.Color
def Color(hex_code):
    """Takes a hex code (like #0000FF) and turns it into an RGB tuple."""
    return pygame.Color(hex_code)


# update the screen
def update_screen():
    """Updates the screen."""
    pygame.display.flip()


# Set a block's saturation according to its light level.
def color_with_light(hex_color: str, light_level: int, max_light_level: int) -> str:
    """A nearly fully modular function to define the saturation of a block depending on its light level.

    Args:
        hex_color (str): The hex color.
        light_level (int): The light level you want the block to have.
        max_light_level (int): The maximum light level that a block can have.

    Returns:
        (str): Always returns a hexadecimal which is the block's color after lighting.
    """
    # Remove the # from hex_color.
    hex_color = hex_color.removeprefix("#")
    # int(hex_color, 16) turns a hexadecimal to decimal.
    R = int(f"0x{hex_color[0]}{hex_color[1]}", 16)
    G = int(f"0x{hex_color[2]}{hex_color[3]}", 16)
    B = int(f"0x{hex_color[4]}{hex_color[5]}", 16)
    # MATH.
    R = floor((R / max_light_level) * light_level)
    G = floor((R / max_light_level) * light_level)
    B = floor((R / max_light_level) * light_level)
    # Back to hex.
    R_hex = str(hex(R).removeprefix("0x"))
    G_hex = str(hex(G).removeprefix("0x"))
    B_hex = str(hex(B).removeprefix("0x"))
    # If lengths are too low, add zeroes.
    if len(R_hex) < 2: R_hex += "0"
    if len(G_hex) < 2: G_hex += "0"
    if len(B_hex) < 2: B_hex += "0"
    # Add it up and re-add the #.
    return f"#{R_hex}{G_hex}{B_hex}"


# The maion function that puts shit on screen.
def display(
    screen, newscreen: list[list], widthofeachblock: int, heightofeachblock: int
):
    """screen is obtained through api.setres
    newscreen is a list of lists, with higher indexes more at the bottom of the map.
    widthofeachblock and heightofeachblock are self-explanatory.
    
    This is a very basic rendering engine. You are advised to make your own."""
    Y = 0
    for Ycoord in newscreen:  # Selects a list from newscreen.
        width_is_due = False
        duewidthofeachblock = widthofeachblock
        X = 0 
        for Xcoord in range(len(Ycoord)):  # Selects a block in said list,
            block = Ycoord[Xcoord]
            try:
                next_block = Ycoord[Xcoord + 1]
            except IndexError:
                next_block = None
            
            #if ishex(str(block)):
            # then it draws the block on screen with it's color
            # being what comes from its __repr__/__str__ function.
            # the rest is self-explanatory.
            block = str(block)  # Turn it into <type 'str'> instead of <class 'api.block'> or smth
            next_block = str(next_block) # Same to next_block
            
            if block != next_block:
                pygame.draw.rect(
                    screen,
                    pygame.Color(block),
                    (X, Y, duewidthofeachblock, heightofeachblock),
                )
                width_is_due = True
            
            if width_is_due:
                X += duewidthofeachblock
                duewidthofeachblock = 0
                width_is_due = False
            
            duewidthofeachblock += widthofeachblock
        Y += heightofeachblock
    
    pygame.display.flip() # Update the display
    # the lack of triple quotes telling me what these functions do irritates me


# Keyboard functions


# Any key -
# Pause thread until any key is pressed.
def wait_any():
    return keyboard.read_key()


# Specific key -
# Pause thread until key is pressed.
def wait_key(key):
    return keyboard.wait(key)


# Check if key is currently being pressed.
def ispressed_key(key):
    return keyboard.is_pressed(key)


# Check if key has just been released.
def isreleased_key(key):
    return keyboard.on_release_key(key)


# The X -
# Check if the user clicked the X on the top-right of the window.
def isquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


# Close the window
def closewindow():
    pygame.quit()


# Close the entire program
def sysexit():
    theactualsysexit()


# Objects -


# Inventory
class inventory:
    """Literally the name. slotdata should be like {"slot1": "jacuzzzzzzzi"}, and selectedindex should be like "slot1".
    
    Has 4 (with a hidden 5th) attributes.
    self.slots: The slots. It is a dict accessed like "inventory_instance.slots["slot1"]".
    self.slotnum: The number of slots in the inventory_instance.
    self.selected: Corresponds to "inventory_instance.slots[inventory_instance.selectedindex]" but is a clone not a pointer 'cause of python bullshit.
    self.selectedindex: The currently selected item's index as in "slot1".
    
    self.type: the type of the object, present in all classes. E.g. "inventory_instance.type" would be "inventory" and "entity_instance.type" would be "entity".
    """
    def __init__(self, slotnum=10, slotdata=None, selectedindex=None):
        if not isint(slotnum):
            raise TypeError("NUMBER of slots must be an integer!")
        
        if slotnum <= 0:
            raise ValueError("Number of slots must be over 0!")
    
        slotnum = int(slotnum)
        slots = {}
        
        for slot_index in range(slotnum):
            if reachableindex(slotdata, f"slot{slot_index}"):
                slots[f"slot{slot_index}"] = slotdata[f"slot{slot_index}"]
            else:
                slots[f"slot{slot_index}"] = None
        
        self.slots = slots
        
        
        if selectedindex == None:
            self.selected = slots["slot1"]
            self.selectedindex = "slot1"
        else:
            self.selected = slots[selectedindex]
            self.selectedindex = selectedindex
        
        self.slotnum = slotnum
        self.type = "inventory"

    # Select a slot in the inventory for use
    def select(self, selectnum: int):
        """Select a slot in the inventory for use."""
        self.selectedindex = "slot" + str(selectnum)
        self.selected = self.slots[self.selectedindex]

    # Clear the inventory of items
    def clearinventory(self):
        """Clear the inventory of items and select slot1."""
        for slot in self.slots:
            self.slots[slot] = None
        
        self.selectedindex = "slot1"
        self.selected = self.slots["slot1"]

    # Shrink the inventory starting from the end
    def shrink(self, slotnum: int):
        """Shrink the inventory starting from the end."""
        for i in range(slotnum):
            
            del self.slots[f"slot{abs(i - self.slotnum)}"]
            self.slotnum -= 1

    # Make the inventory bigger
    def enlarge(self, slotnum: int, slotdata):
        """Make the inventory bigger."""
        for slot_index in range(self.slotnum, slotnum + self.slotnum):
            
            if reachableindex(slotdata, slot_index - self.slotnum):
                self.slots[f"slot{slot_index}"] = slotdata[slot_index]
            
            else:
                self.slots[f"slot{slot_index}"] = None
        
        self.slotnum += slotnum
    
    def add(self, items: list) -> list:
        """Adds an item to the inventory and returns whatever couldn't be put in the inventory.

        Args:
            items (list): A list of items to put in the inventory. Can also be a list with just one element.

        Returns:
            list: The remaining items which could not be put in the inventory.
        """
        remaining_items = []
        
        for item in items:
            item_put = False
            
            for slot in self.slots.keys():
                if not self.slots[slot] == None:
                    continue
                
                self.slots[slot] = item
                item_put = True
                break
            
            if item_put:
                continue
            
            remaining_items.append(item)
        
        return remaining_items
    
    def pop(self, index: int=-1, not_None: bool=True):
        """Like some_list.pop(index) but for the inventory.
        If not_None is True, it will attempt to not return None unless there is no other option."""
        value = None # the value to return should be None at the start in case it never gets assigned
        if index < 0 and not not_None:
            index = self.slotnum + index
        
        if not_None:
            not_none_index_count = 0
            for slot_index in reverse_if_true(range(self.slotnum), index < 0):
                
                if self.slots[f"slot{slot_index}"] != None:
                    not_none_index_count -= 1
                
                if not_none_index_count <= index:
                    
                    value = self.slots[f"slot{slot_index}"] # get val
                    self.slots[f"slot{slot_index}"] = None # remove val
                    break
        
        else:
            value = self.slots[f"slot{index}"] # get val
            self.slots[f"slot{index}"] = None # remove val
        
        return value

    def __str__(self):
        return str(self.slots)
    
    def __repr__(self):
        return str(self.slots)


# Block
class block:
    """Exactly what the name says. You can also call it a tile.

    varname: What variable is this block called? Used for turntoblock() and turnarraytoblocks().

    image: What the display() function will use. Is usually a hex code.

    passable: Can it be passed through by entities?

    breakablebytool: Can it be broken by an entity weilding a tool?

    droptoolvalue: What level does that tool have to be?

    drop: What does the entity gain in its inventory upon breaking the block?
        An item class doesn't exist, just put an empty string for now.

    falling: Is the block not immune to gravity? Use this so you can just do this and it will move if this value is set to True:
    for block in world: block.move(arguments)
    """
    def __init__(
        self,
        varname: str = "Stn",
        image: str = "#000000",
        passable: bool = False,
        breakablebytool: bool = True,
        droptoolvalue: int = 2,
        drop="Stone",
        falling: bool = False,
    ):
        self.varname = varname
        self.image = image
        self.passable = passable
        self.breakablebytool = breakablebytool
        self.droptoolvalue = droptoolvalue
        self.drop = drop
        self.falling = falling
        self.type = "block"

    def move(self, Y: int, X: int, direction: str, data: list, replace: str = "block class", speed: int = 1) -> list:
        """Move the entity. What did you think? Also great for gravity.

        Args:
            Y (int): The Y coordinate of the block.
            X (int): The X coordinate of the block.
            direction (str): Can be "w", "a", "s", or "d". If you don't know what either of those options do, stop living under the mariana trench.
            data (2D Array): The world around the block.
            replace (block class): What will be left in the space the block once was.
            speed (int, optional): How many blocks forward should the block go?

        Returns:
            list: [0] is the world after the block has moved, and [1] is the block before the other block moved to it. [2] is the post-moving X coordinate of the block, and [3] is the post-moving Y coordinate of the block.
        """

        # Load -

        direction = str.lower(direction)
        final2 = replace  # lol i don't know why, this is a pretty old line of code
        dy, dx = 0, 0  # difference Y, difference X
        match direction:
            case "w":
                dy -= 1
            case "a":
                dx -= 1
            case "s":
                dy += 1
            case "d":
                dx += 1

        # Main -

        # [i] doesn't matter here, we're just tryna do stuff multiple times
        # oh, you wanna teleport? just do block.position[newX, newY] or something ffs
        for i in range(speed):
            # Credit to guy on discord for writing this.
            if (
                reachableindex(data, Y + dy)
                and reachableindex(data[Y], X + dx)
                and Y + dy > -1
                and X + dx > -1
            ):
                if data[Y + dy][X + dx].passable:
                    data[Y][X] = replace
                    final2 = data[Y + dy][X + dx]
                    data[Y + dy][X + dx] = self
                    Y += dy
                    X += dx

        # Return -

        return [data, final2, X, Y]

    def __str__(self):
        return self.image

    def __repr__(self):
        return self.image


#        return f"api.block(image=\"{self.image}\",passable={str(self.passable)},breakablebytool={str(self.breakablebytool)},droptoolvalue={str(self.droptoolvalue)},drop={str(self.drop)},falling={str(self.falling)})"


# Entity
class entity:
    """Exactly what the name is. Can be used to make a player character.
    Methods:
        breakblock()
        move()
        hurt()
        heal()
    Hover over them after typing them out for a description of what they do and their inputs.
    """
    def __init__(
        self,
        replace: block,
        varname="plr",
        image="#000000",
        maxhealth: int = 100,
        health: int = 100,
        armor: int = 0,
        attack: int = 5,
        defense: int = 5,
        speed: int = 1,
        position: list = [2, 2],
        inventory: inventory = inventory(),
        dead: bool = False,
        deffactor: float = 0.5,
        atkfactor: float = 0.5,
        reach: int = 1,
        handvalue: int = 1,
    ):
        self.varname = varname
        self.image = image
        self.maxhealth = maxhealth
        self.health = health
        self.armor = armor
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = inventory
        self.position = position
        self.replace = replace
        self.dead = dead
        self.deffactor = deffactor
        self.atkfactor = atkfactor
        self.type = "entity"
        self.passable = False
        self.reach = reach
        self.handvalue = handvalue

    # Break a block
    def breakblock(
        self,
        direction: str,
        data: list,
        replace: block,
        distance: int = 0,
        bypass_inventory: bool = True,
        still_add: bool = True
    ) -> list[list[block]]:
        """Break blocks up to a certain distance away from the entity.
        Will not break passable blocks, blocks which have "breakablebytool" set to False,
        or blocks when there is no free slot in the inventory unless bypass_inventory is True.
        Will not add the block to the inventory when bypass_inventory is True unless still_add is True.
        If distance or entity.reach is over 1, will place on all passable blocks in the way similar to entity.move.
        
        Args:
            direction (str): Simple: wasd. If you don't get it, stop touching grass.
            data (list[list[block]]): The world around the entity.
            distance (int, optional): The name. Defaults to the entity's reach attribute if it's 0.
            bypass_inventory (bool, optional): It will not add items to the inventory automatically when this value is True. Defaults to True.
            still_add (bool, optional): It will add items to the inventory and keep breaking blocks regardless of inventory fullness if this value is True. Defaults to True.

        Returns:
            2D Array: The world after the entity has broken that block in front of it.
        """

        # Load -

        direction = str.lower(direction)
        dx, dy = 0, 0
        if distance != 0:
            usedistance = distance
        else:
            usedistance = self.reach
        
        for i in range(usedistance):
            
            # god damn i don't drink but sometimes i write like i do
            match direction:
                case "w":
                    dy -= 1
                case "a":
                    dx -= 1
                case "s":
                    dy += 1
                case "d":
                    dx += 1
            
            X = self.position[0] + dx
            Y = self.position[1] + dy
            # i mean the logic makes sense but it could've been done better

            # Main -

            # De-nestified a fair bit :D
            if data[Y][X].passable:
                continue
            elif self.handvalue < data[Y][X].droptoolvalue:
                break
            
            if not bypass_inventory:
                if not self.inventory.add([data[Y][X].drop]):
                    data[Y][X] = replace
            elif still_add:
                self.inventory.add([data[Y][X].drop])
                data[Y][X] = replace
            else:
                data[Y][X] = replace

        # Return -

        return data

    # Break a block
    def placeblock(
        self,
        direction: str,
        data: list[list[block]],
        replace: block = None,
        distance: int = 0,
        ignore_passable: bool = False,
        ignore_inventory: bool = False,
        item_to_block_dict: dict = {}
    ) -> list[list[block]]:
        """Place blocks up to a certain distance away from the entity.
        Will also stop placing blocks after the inventory is empty.
        This function pulls from the end of the inventory to the start.
        If distance or entity.reach is over 1, will place on all passable blocks in the way similar to entity.move.
        
        Args:
            direction (str): Simple: wasd. If you don't get it, stop touching grass.
            data (list[list[block]]): The world around the entity.
            replace (block, optional): If ignore_inventory is True, it will only place this argument.
            distance (int, optional): The name. Defaults to the entity's reach attribute if it's 0.
            ignore_passable (bool, optional): Will not stop placing blocks after encountering an impassable block.
            ignore_inventory (bool, optional): Read the description of the replace argument.
            item_to_block_dict (dict): if ignore_inventory is False, this dict will be used to transform items into blocks.

        Returns:
            2D Array: The world after the entity has placed that block.
        """

        # Load -

        direction = str.lower(direction)
        dx, dy = 0, 0
        if distance != 0:
            usedistance = distance
        else:
            usedistance = self.reach
        
        # Main -
        
        for i in range(usedistance):
            
            # ah it's only being used 1 or 2 times anyway
            match direction:
                case "w":
                    dy -= 1
                case "a":
                    dx -= 1
                case "s":
                    dy += 1
                case "d":
                    dx += 1
            
            X = self.position[0] + dx
            Y = self.position[1] + dy
            
            if not data[Y][X].passable and not ignore_passable:
                break
            
            if ignore_inventory:
                data[Y][X] = replace
                continue
            
            popped_item = self.inventory.pop()
            
            if popped_item == None:
                break
            
            data[Y][X] = item_to_block_dict[popped_item]
            
            X += dx
            Y += dy

        # Return -

        return data

    # Move the entity
    def move(self, direction: str, data: list, replace: block, speed: int = 0) -> list:
        """Move the entity. What did you think? Also great for gravity.

        Args:
            direction (str): Can be "w", "a", "s", or "d". If you don't know what either of those options do, stop living under the mariana trench.
            data (2D Array): The world around the entity.
            replace (block class): What will be left in the space the entity once was.
            speed (int, optional): How many blocks forward should the entity go? Defaults to the speed of the entity.

        Returns:
            list: [0] is the world after the entity has moved, and [1] is the block before the entity moved to it.
        """

        # Load -

        direction = str.lower(direction)
        final2 = replace  # lol i don't know why, this is a pretty old line of code
        dy, dx = 0, 0  # difference Y, difference X
        if speed != 0:
            usespeed = speed
        else:
            usespeed = self.speed
        match direction:
            case "w":
                dy -= 1
            case "a":
                dx -= 1
            case "s":
                dy += 1
            case "d":
                dx += 1
        
        X = self.position[0] + dx
        Y = self.position[1] + dy

        # Main -

        # [i] doesn't matter here, we're just tryna do stuff multiple times
        # oh, you wanna teleport? just do entity.position[newX, newY] or something ffs
        for i in range(usespeed):
            # Idk how I would even begin to comment this
            if (
                reachableindex(data, Y)
                and reachableindex(data[self.position[1]], X)
                and Y > -1
                and X > -1
            ):
                if data[Y][X].passable:
                    data[self.position[1]][self.position[0]] = replace
                    final2 = data[Y][X]
                    data[Y][X] = self
                    self.position[1] += dy
                    self.position[0] += dx
                    Y += dy
                    X += dx

        # Return -

        return [data, final2]

    # Hurt the entity
    def hurt(self, amount: int) -> bool:
        """Subtract a specific amount of health from the entity. Takes defense and armor into account. Also declares the entity dead if health is 0. Returns a bool for if the entity is dead or not."""
        self.health -= amount - (self.defense * self.deffactor) - self.armor
        if self.health <= 0:
            self.death = True
            return self.death
        else:
            return self.death

    # Heal the entity
    def heal(self, amount: int) -> bool:
        """Add a specific amount of health to the entity. Also declares the entity not dead anymore if health is above 0. Returns a bool for if the entity is dead or not."""
        self.health += amount
        if self.health > self.maxhealth:
            while self.health > self.maxhealth:
                self.health -= 1
        if self.health > 0:
            self.dead = False
        return self.dead

    def __str__(self):
        return self.image

    def __repr__(self):
        return self.image


# World Generation -

# Limit
class Limit(NamedTuple):
    upper_limit: int
    lower_limit: int


# Biome
class Biome(NamedTuple):
    name: str
    chance_of_spawning: int
    minimum_length: int
    maximum_length: int
    layers: list

# Ore configuration
class OreConfiguration(NamedTuple):
    chance_of_spawning: int
    spawn_limit: int
    upper_limit: int
    lower_limit: int
    block: block

# Terrain
class Terrain:
    """A Terrain type. Used for the new, OPTIMIZED and FASTER optimized_generate!

Args:
    name (str): The name. Used to tell a programmer what this terrain type is.
    
    spawn_chance (int): Whether or not this type will spawn is decided by
    random.randint(1, 100) <= spawn_chance
    Imagine this as a percent chance of the terrain type spawning on any block except for those that already have a terrain type.
    
    length_range (list[int, int]): The range of length. On the first index is the minimum length and on the last is the maximum length.
    
    transform_function (function): Alright, this is gonna require a good explanation.
Basically, optimized_generate takes a list of all terrain types you want to add.
Since I wanted the game to be able to define easily what kind of terrain it wants,
I let you make a custom function for it! How merciful is that? More than the fact
you're actually coding in this engine.

When optimized_generate calls transform_function, it will give you two arguments:
The current length of the terrain type that has been generated,
and the maximum length picked by random.randint(length_range[0], length_range[1]).

After that, you MUST return a list[list[int, int], int].
The first index specifies a range of how many blocks above or below the previous
block the next block should be,
and the second index tells the function what chance there is of that happening.

And by the way, the result of this transform_function bypasses [next_block_limit]
but not [limit].
"""
    def __init__(self, name: str, spawn_chance: int, length_range: list[int, int], transform_function="literally a function"):
        self.name = name
        self.spawn_chance = spawn_chance
        self.length_range = length_range
        self.transform_function = transform_function

def mountain_transform(current_length: int, max_length: int) -> list[list[int, int], int]:
    """Hiya there, this a pre-built transform_function for the Terrain class used in a pre-built variable for it known simply as mountain_terrain_type.
    This tends to generate mountains.

    Args:
        current_length (int): The first argument optimized_generate gives it.
        max_length (int): The second argument optimized_generate gives it.

    Returns:
        list[list[int, int], int]: For an explanation, read the Terrain class' description.
    """
    if current_length <= max_length // 2:
        return [[0, 1], 40]
    else:
        return [[-1, 0], 40]

def inverse_mountain_transform(current_length: int, max_length: int) -> list[list[int, int], int]:
    """Hiya there, this a pre-built transform_function for the Terrain class used in a pre-built variable for it known simply as inverse_mountain_terrain_type.
    This tends to generate inverted mountains. That actually used to be called "canyons".

    Args:
        current_length (int): The first argument optimized_generate gives it.
        max_length (int): The second argument optimized_generate gives it.

    Returns:
        list[list[int, int], int]: For an explanation, read the Terrain class' description.
    """
    if current_length >= max_length // 2:
        return [[0, 1], 70]
    else:
        return [[-1, 0], 70]

def plateau_transform(current_length: int, max_length: int) -> list[list[int, int], int]:
    """Hiya there, this a pre-built transform_function for the Terrain class used in a pre-built variable for it known simply as plateau_terrain_type.
    This tends to generate plateau-like terrain.

    Args:
        current_length (int): The first argument optimized_generate gives it.
        max_length (int): The second argument optimized_generate gives it.

    Returns:
        list[list[int, int], int]: For an explanation, read the Terrain class' description.
    """
    if current_length <= max_length // 0.25:
        return [[-1, 0], 70]
    elif current_length <= max_length // 0.75:
        return [[0, 0], 70]
    else:
        return [[0, 1], 70]

def crater_transform(current_length: int, max_length: int) -> list[list[int, int], int]:
    """Hiya there, this a pre-built transform_function for the Terrain class used in a pre-built variable for it known simply as crater_terrain_type.
    This tends to generate crater-like terrain, also known as inverse plateaus.

    Args:
        current_length (int): The first argument optimized_generate gives it.
        max_length (int): The second argument optimized_generate gives it.

    Returns:
        list[list[int, int], int]: For an explanation, read the Terrain class' description.
    """
    if current_length <= max_length // 0.25:
        return [[0, 1], 70]
    elif current_length <= max_length // 0.75:
        return [[0, 0], 70]
    else:
        return [[-1, 0], 70]

mountain_terrain_type = Terrain(
    name="mountain",
    spawn_chance=3,
    length_range=[50, 200],
    transform_function=mountain_transform
)

inverse_mountain_terrain_type = Terrain(
    name="inverted mountain",
    spawn_chance=3,
    length_range=[50, 200],
    transform_function=inverse_mountain_transform
)

plateau_terrain_type = Terrain(
    name="plateau",
    spawn_chance=3,
    length_range=[50, 200],
    transform_function=plateau_transform
)

crater_terrain_type = Terrain(
    name="crater",
    spawn_chance=3,
    length_range=[50, 200],
    transform_function=crater_transform
)


# Actually generate a world (LEGACY)
def generate(
    width: int = 400,
    height=100,
    biomes: list = [],
    Air: block = block(
        image="#FFFFFF",
        passable=True,
        breakablebytool=False,
        droptoolvalue=0,
        drop="Air",
        falling=False,
    ),
    Stn: block = block(image="#888888"),
    Bedrock: block = block(image="#111111"),
    limit: list = (2, 98),
    oreconfig: dict = {},
    originalYY: int = None,
    oreeverywhere: bool = False,
    mountainlikelihood: int = 7,
    averagesteepness: int = 40,
    averagelength: int = 20,
    canyonlikelihood: int = 4,
    averagesteepnessofcanyon: int = 30,
    averagelengthofcanyon: int = 20
):
    """LEGACY version! Use optimized_generate instead.
    Here it is. The absolute MAX I can go to. THE EPITOME OF MY LABOUR!!

    this took hours of my life.
    i'm doing this for free.
    nobody will ever see this.
    i could've done other things with my time.

    Summary:

    Args:
        width (int, optional): The width of the world. Defaults to 400.
        height (int, optional): The height of the world. Defaults to 100.
        biomes (list, NOT optional): Biomes. Define minimum size and maximum size with the first and second indexes. Randomly chosen. Example: [[10, 30, Grs, Grs, Drt, Drt],[10, 30, Snd, Snd, Snd, Sndst]] Defaults to None.
        Air (block, optional): The thing that permeates open spaces. Defaults to "Air".
        Stn (block, optional): The thing that permeates everything below the ground. Defaults to "Stn".
        Bedrock (block, optional): Seperates all entities from the endless void below. Defaults to "Bdr".
        limit (tuple, optional): Prevents world generation indexes above the first index of this list and below the second index of this list. Keep in mind that Y levels are reversed, so being very high up = being at a very low Y level, and being deep underground = being at a high Y level. Defaults to None.
        oreconfig (list, optional): {"iron": 50, 10, 40, IronOre}: in this configuration, the block known as "IronOre" has a 1/50th (2%) chance of spawning between 10 and 40 blocks below the top solid block. If left alone it will default to None and the generator will pick a top solid block for you.
        originalYY (int, optional): Where is the original top solid block? Excellent for chunk building, allows for chunks connecting. Defaults to None.
        oreeverywhere (bool, optional): Should ore be placed regardless of the top solid block? Excellent for making Underground chunks. Defaults to False.
        mountainlikelihood (int, optional): How likely are mountains to spawn? calculates as "if random.randint(1, 100) <= mountainlikelihood" and if that results in True, turns on Mountain generation. Should NOT be over 100. Defaults to 7%.
        averagesteepness (int, optional): When mountain drive is on, how likely should it be that the next block is above the previous block? Defaults to 40%.
        averagelength (int, optional): How long should a mountain drive last? Defaults to 20.
        canyonlikelihood (int, optional): mountainlikelihood but for canyons. Defaults to 4%.
        averagesteepnessofcanyon (int, optional): averagesteepness but for canyons. Defaults to 30%.
        averagelengthofcanyon (int, optional): averagelength but for canyons. Defaults to 20.
        logging (bool, optional): Log whatever it's generating right now? gives the player something to look at while waiting for the world to load.

    Returns:
        A 2D Array. This is your 2D world.
    """
    # Air = literally the air, the thing that permeates open spaces.
    # Stn = the thing that permeates closed spaces underground.
    # Bedrock = the bottom layer of the world that separates all entities from the void.
    # biomes = biomes, the first index should be the minimum size of the biome and the second should be the maximum size of the biome. For example:
    # biomes = [
    #    [10, 30, Grs, Grs, Drt, Drt],
    #    [10, 30, Snd, Snd, Snd, Sndst]
    # ]

    # - Variable Checking -

    # Select the first biome
    if biomes == []:
        print(
            "HEY! YOU FORGOT TO GIVE ME ACTUAL BIOMES!!\n[BIOMES] IS LITERALLY JUST A BLANK LIST!"
        )
        ValueError()
    uncbiome = random.choice(biomes)
    if mountainlikelihood >= 100:
        print("HEY! MOUNTAINLIKELIHOOD SHOULD NOT BE OVER 100!!")
        ValueError()

    # - Create the initial space -

    space = {}  # Create the empty world
    for ylevel in range(height):  # For every number in height,
        space["y" + str(ylevel + 1)] = []  # Add a new Ylevel in "space"
        for xlevel in range(width):  # And then for every number in width,
            if ylevel != range(height)[-1]:  # If it's not at bedrock,
                space["y" + str(ylevel + 1)].append(Air)  # Then put Air there.
            else:  # If it is at bedrock level,
                space["y" + str(ylevel + 1)].append(Bedrock)  # Put Bedrock there.

    # - Add blocks (finally use biomes) -

    # Initalize some variables

    # Check limit
    if limit == None:
        limit = [5, height + 1]

    # The top solid layer of the world
    if originalYY == None:
        if limit[0] == 0:
            originalY = random.randint(limit[0] + 1, limit[1])
        else:
            originalY = random.randint(limit[0], limit[1])
    else:
        originalY = originalYY

    # [Y] is used for biomes, to generate things below the top layer.
    Y = originalY
    X = 0
    # Used later for structure and ore generation.
    # It means "Top layer", not "To player".
    toplayer = []
    toplayer.append([originalY, X])
    biome = []
    for i in uncbiome:
        biome.append(i)
    minim = biome[0]
    maxim = biome[1]
    del biome[0]  # Delete the minimum biome size FROM [BIOME]
    del biome[0]  # Delete the maximum biome size FROM [BIOME]
    biomelength = 1
    internalmaximum = random.randint(
        minim, maxim
    )  # Set a random internal maximum biome size FOR THIS BIOME ONLY. Allows for varying biome sizes.
    heightlimit = 0
    # First initial layer
    space["y" + str(Y)][X] = biome[0]

    mountaindrive = False
    canyondrive = False
    totallength = 0
    totallengthofcanyon = 0
    length = random.randint(
        averagelength - floor(averagelength / 2 / 2),
        averagelength + floor(averagelength / 2 / 2),
    )
    lengthofcanyon = random.randint(
        averagelengthofcanyon - floor(averagelengthofcanyon / 2 / 2),
        averagelengthofcanyon + floor(averagelengthofcanyon / 2 / 2),
    )

    for i in range(width):
        for i in range(height):
            # This comment wall was just a discord message simplifying this code for some other guy, who then suggested I add it to the actual code.
            # I added so many checks for [Y], the [heightlimit], and the [Bedrock] level because it somehow kept being there which is weird ash.
            # Also, no, it's not for figuring out where [Bedrock] is depending on the [biome],
            # it's for generating layers depending on the [biome].
            # The [Bedrock] layer is always at the bottom of the [space].
            # [biomes] is a list that contains lists which are the actual biomes. [biome] is randomly picked and a random number is chosen between its max length and minimum length.
            # After that, let's say [biome] is ["Dirt", "Dirt", "Dirtier Dirt"].
            # This means that every generated [Y] level while that [biome] is active will look like [Dirt] on top, [Dirt] at the second layer, then [Dirtier Dirt] at the third.
            # After that, it's all [Stn] and maybe some ores until the [Bedrock] layer.
            if Y == heightlimit:
                Y += 1
            elif heightlimit > Y:
                Y = abs(Y)
                Y += 1
            elif Y >= height:
                Y = height - 1
            if (
                (i - 1) >= 0 and space["y" + str(Y)][X] != Bedrock
            ):  # If Y is higher than or equal to 0 and the currently selected Block isn't Bedrock.
                if reachableindex(biome, i - 1):
                    space["y" + str(Y)][X] = biome[
                        i - 1
                    ]  # If [biome] hasn't ran out, apply the latest layer.
                elif reachableindex(biome, i - 1) == False:
                    space["y" + str(Y)][X] = Stn  # Otherwise, make the block Stone.
                if Y < height:
                    Y += 1  # If Y is not at the Bedrock layer, increase it.

        # nextplace can be one of three values chosen randomly: 1, 2, and 3.
        # No matter what value nextplace is, X will always increase as long as it doesn't surpass width while doing so.
        # Also do  stuff with mountains and canyons.
        above = 1
        below = 3

        if random.randint(1, 100) <= mountainlikelihood and canyondrive != True:
            mountaindrive = True

        if random.randint(1, 100) <= canyonlikelihood and mountaindrive != True:
            canyondrive = True

        if mountaindrive == True:
            if random.randint(1, 100) <= averagesteepness:
                if totallength < floor(length / 2):
                    below -= 1
                else:
                    above += 1
                if totallength >= length:
                    mountaindrive = False
            totallength += 1
        elif canyondrive == True:
            if random.randint(1, 100) <= averagesteepnessofcanyon:
                if totallengthofcanyon < floor(lengthofcanyon / 2):
                    above += 1
                else:
                    below -= 1
                if totallengthofcanyon >= lengthofcanyon:
                    canyondrive = False
            totallengthofcanyon += 1

        if mountaindrive == False and totallength != 0:
            totallength = 0
        elif canyondrive == False and totallengthofcanyon != 0:
            totallengthofcanyon = 0

        if originalY + 1 < limit[0] or originalY + 1 < 1:
            above += 1

        if originalY - 1 > limit[1] or originalY - 1 > (height - 1):
            below -= 1

        try:
            nextplace = random.randint(above, below)
        except ValueError:
            nextplace = 2

        if X < width - 1:
            if (
                nextplace == 1
            ):  # If nextplace is equal to 1, the block placed in the next X coord's Y coord will be higher than the last X coord block's Y coord.
                originalY -= 1
                X += 1
            elif (
                nextplace == 2
            ):  # If nextplace is equal to 2, the block placed in the next X coord's Y coord will be the same as the last X coord block's Y coord.
                X += 1
            elif (
                nextplace == 3
            ):  # If nextplace is equal to 3, the block placed in the next X coord's Y coord will be lower than the last X coord block's Y coord.
                originalY += 1
                X += 1
            Y = originalY  # Set Y to the top solid block.
            # All of this is code jargon for "If nextplace = 1, go up a block.
            # If nextplace = 2, stay at the same height.
            # If nextplace = 3, go down a block.
            # Otherwise select a different value for nextplace.
            # Then start generating blocks from the top to the bottom."
        toplayer.append([originalY, X])
        biomelength += 1
        # Determine if it's time to switch up the biome
        if biomelength > internalmaximum:
            # If so, set some variables to some stuff and pick a new biome
            uncbiome = random.choice(biomes)
            biome = []
            for i in uncbiome:
                biome.append(i)
            minim = biome[0]
            maxim = biome[1]
            del biome[0]
            del biome[0]
            biomelength = 1
            internalmaximum = random.randint(minim, maxim)

    # Ore and Structure Generation

    # Ore -
    if oreconfig != {}:
        if oreeverywhere == False:
            for topblock in toplayer:
                # no im not gonna touch this shit
                for ore in list(oreconfig.values()):

                    spawnchance = random.randint(1, ore[0])

                    if spawnchance == 1 and reachableindex(
                        space, "y" + str(topblock[0] + ore[1])
                    ):
                        if ore[2] < height:
                            area = random.randint(ore[1], ore[2])
                        elif ore[2] >= height:
                            if ore[1] < height:
                                area = random.randint(ore[1], height - 1)
                            elif ore[1] >= height:
                                pass
                        spawnlocation = topblock[0] + area
                        if spawnlocation >= height:
                            spawnlocation = height - 1
                        if reachableindex(list(oreconfig.values()), ore):
                            space["y" + str(spawnlocation)][topblock[1]] = list(
                                oreconfig.values()
                            )[list(oreconfig.values()).index(ore)][3]

        elif oreeverywhere == True:
            # god i love the fact i'm never gonna have to touch this again
            # holy shit this looks like some programmer puked all over their keyboard 
            data = list(space.values())
            for ylevel in data:
                for xlevel in ylevel:
                    for ore in list(oreconfig.values()):
                        spawnchance = random.randint(1, ore[0])

                        if spawnchance == 1:
                            area = random.randint(ore[1], ore[2])
                            if reachableindex(space, "y" + str(area)):
                                if area >= height: spawnlocation = height - 1
                                if reachableindex(ylevel, xlevel):
                                    space["y" + str(area)][ylevel.index(xlevel)] = list(
                                        oreconfig.values()
                                    )[list(oreconfig.values()).index(ore)][3]

    # FINALLY return the world.
    return list(space.values())


# Actually generate a world (but faster)
def optimized_generate(
    seed: str,
    width: int,
    height: int,
    
    air: block,
    
    stone: block,
    
    limit: Limit = Limit(100, 700),
    
    biomes: list[Biome] = [
            Biome(
                "plains",
                50,
                10,
                50,
                ["Grs", "Grs", "Drt", "Drt", "Drt", "Drt"]
            ),
            
            Biome(
                "desert",
                50,
                10,
                50,
                ["Snd", "Snd", "Snd"]
            )
        ],
        
    ore_config: list[OreConfiguration] = [
            OreConfiguration(
                5,
                1,
                10,
                20,
                "IronOre"
            ),
            
            OreConfiguration(
                30,
                3,
                20,
                40,
                "CoalOre"
            ),
            
            OreConfiguration(
                30,
                3,
                30,
                100,
                "IronOre"
            ),
            
            OreConfiguration(
                30,
                10,
                50,
                250,
                "CoalOre"
            )
        ],
    
    next_block_limits: Limit = Limit(-1, 1),
        
    starting_y: int = None, # my reasoning for this is that starting_Y will be randomly chosen if None.
    terrain_types: list = [mountain_terrain_type, inverse_mountain_terrain_type, plateau_terrain_type]
):
    """Time to toss the so-called "epitome of my labor" in the trash and make a better one.

    Summary: it generates a world, but 3x-2.3x faster.

    Args:
        seed (str): The seed for the world. Leave as None for the engine to pick one for you.
        width (int): The width of the world.
        height (int): The height of the world.
        
        air (block): The thing that permeates open spaces.
        stone (block): The thing that permeates closed spaces.
        
        limit (Limit): Prevents world generation indexes above upper_limit and below lower_limit.

        biomes (list[Biome]): Biomes. Just look at the default to figure out its structure.

        ore_config (list[OreConfiguration]): Look at the default. spawn_limit limits how many of that ore can spawn at a single Y coordinate.
        
        next_block_limits (Limit): Look at the default. This controls how far up or down a block can be from another block.
        
        starting_y (int): Where to start from? Excellent for chunk building as it allows for chunks connecting. If left as None, the engine will randomly pick one for you.
        terrain_types (list): What terrain types do you want to be able to be generated? Defaults to the default ones from the Engine.

    Returns:
        list: A 2D Array. This is your 2D world.
    """
    # - Variable Checking -
    
    # Select the first biome.
    if biomes == []:
        print("HEY! YOU FORGOT TO GIVE ME ACTUAL BIOMES!!\n[biomes] IS LITERALLY JUST A BLANK LIST!")
        ValueError()
    
    # None is pretty falsy, so I'll just use if not [variable].
    if not seed:
        seed = rand_num(random.randint(0, 1000000000000))
    
    if not starting_y:
        starting_y = random.randint(limit.upper_limit, limit.lower_limit)
    
    # set seed again cause i'm not sure if random.randint can change random.seed
    random.seed(seed)
    # Y is used to generate blocks below the top solid layer.
    Y = starting_y
    X = 0
    # generating_terrain blocks other terrain types from generating while one is on.
    generating_terrain = False
    # current_terrain_type is the currently generating terain type.
    current_terrain_type = None
    
    # - Create the initial space -

    # Pretty self-explanatory if you're not a silly lil dum dum.
    #space = []
    #for i in range(height):
    #    space.append([])
    #    for j in range(width):
    #        space[-1].append(air)
    #space = [[air] * width] * height
    #space = [[air] * width for y in range(height)]
    space = []
    for i in range(height):
        new_row = []
        for j in range(width):
            new_row.append(air)
        space.append(new_row)

    # - Add blocks (finally use biomes) -

    # Initalize some variables

    # [Y] is used for biomes, to generate things below the top layer.
    # Used later for structure and ore generation.
    top_layers = []
    top_layers.append([starting_y, X])
    
    biome = None
    while not biome:
        for biome_candidate in biomes:
            if random.randint(1, 100) <= biome_candidate.chance_of_spawning:
                biome = biome_candidate
    
    current_biome_length = 0
    current_biome_layers = biome.layers
    current_biome_max_length = random.randint(
        biome.minimum_length,
        biome.maximum_length
    )
    
    current_terrain_type_length = 0
    current_terrain_type_max_length = 0

    for times_X in range(width):
        # biome_Y is used for biomes, so the original Y is not contaminated.
        biome_Y = Y
        
        for times_Y in range(height):
            
            # Actually do the biome work.
            if not reachableindex(space, biome_Y):
                break
            
            # If you don't know why times_Y is being used for this,
            # don't worry. I'm not explaining.
            if reachableindex(current_biome_layers, times_Y):
                space[biome_Y][X] = current_biome_layers[times_Y]
            else:
                space[biome_Y][X] = stone
            
            biome_Y += 1
        
        # Out of times_Y, into times_X.
        
        # next_place is added to Y to decide how many blocks above or below the previous block the next
        # block should be.
        next_place = random.randint(
            next_block_limits.upper_limit,
            next_block_limits.lower_limit
        )
        
        # Terrain generation time.
        if not generating_terrain:
            for type in terrain_types:
                if random.randint(1, 100) <= type.spawn_chance:
                    
                    generating_terrain = True
                    current_terrain_type = type
                    current_terrain_type_length = 0
                    
                    current_terrain_type_max_length = random.randint(
                        type.length_range[0],
                        type.length_range[1]
                    )
                
        
        if generating_terrain:
            if current_terrain_type_length <= current_terrain_type_max_length:
        
                transform_result = current_terrain_type.transform_function(
                    current_terrain_type_length,
                    current_terrain_type_max_length
                )
        
                if random.randint(1, 100) <= transform_result[1]:
        
                    next_place = random.choice(
                        transform_result[0]
                    )
        
            else:
                generating_terrain = False
        
        # Now to clean up next_place.
        while Y + next_place < limit.upper_limit:
            #print("next place must go down")
            #print(f"next_place going down: {next_place}")
            next_place += 1
        
        while Y + next_place > limit.lower_limit:
            #print("next place must go up")
            #print(f"next_place going up: {next_place}")
            #print(f"limit['lower_limit']: {limit['lower_limit']}")
            #print(f"Y at next_place: {Y}")
            #print(f"Y + next_place: {Y + next_place}")
            #print(f"Y + next_place > limit['lower_limit']: {Y + next_place > limit['lower_limit']}")
            next_place -= 1
        
        # The show must go on!
        top_layers.append([Y, X])
        if X < width:
            #print(f"next_place: {next_place}")
            Y += next_place
            X += 1
        current_terrain_type_length += 1
        #print(f"X: {X}")
        #print(f"Y: {Y}")
        
        # length checking
        current_biome_length += 1
        
        # If the biome's length is finished, select a different one.
        if current_biome_length > current_biome_max_length:
            biome = None
            while not biome:
                for biome_candidate in biomes:
                    if random.randint(1, 100) <= biome_candidate.chance_of_spawning:
                        biome = biome_candidate
                        break

            current_biome_length = 0
            current_biome_layers = biome.layers
            current_biome_max_length = random.randint(
                biome.minimum_length,
                biome.maximum_length
            )
        
        if current_terrain_type_length > current_terrain_type_max_length:
            generating_terrain = False

    # Ore and structure generation

    # Ore -
    for top_block in top_layers:
        for ore in ore_config:
            
            for times in range(random.randint(1, ore.spawn_limit)):
                # Part of the great de-nesting.
                if not random.randint(1, 100) <= ore.chance_of_spawning or not reachableindex(
                    space,
                    top_block[0] + ore.upper_limit
                ):
                    continue
                
                # Self-explanatory for the most part.
                spawn_area = random.randint(
                    ore.upper_limit,
                    ore.lower_limit
                ) + top_block[0]
                
                # If spawn_area's too far away, just reel it back in.
                # Yeah this might cause some ores to cluster up at the bottom of the world, so what?
                if spawn_area >= height:
                    continue
                
                space[spawn_area][top_block[1]] = ore.block

    # FINALLY return the world.
    return space


# Saving -
def turntoblock(block: block = block(), addapi: bool = True) -> str:
    """Do you also hate that you can't just put "world = {world}" to save because it creates those pesky hashtags? here's a fix. It's useful for saving entities as they were in the world.

    Args:
        block (block, optional): Toss in a block. Defaults to block().
        addapi (bool, optional): Adds "api." before any function used in the api if true. Defaults to True.

    Returns:
        str: Out comes something like "api.block(image=)" or "api.entity(image=)".
    """
    if block.type == "block":
        return f"{addapiiftrue(addapi=addapi)}block(varname=\"{block.varname}\",image={block.image},passable={block.passable},breakablebytool={block.breakablebytool},droptoolvalue={block.droptoolvalue},drop={block.drop},falling={block.falling})"
    elif block.type == "entity":
        return f'{addapiiftrue(addapi=addapi)}entity(varname=\"{block.varname}\",image="{block.image}",maxhealth={block.maxhealth},health={block.health},armor={block.armor},attack={block.attack},defense={block.defense},speed={block.speed},position={block.position},replace={block.replace.varname},inventory={addapiiftrue(addapi=addapi)}inventory(slotnum={block.inventory.slotnum},slotdata={putstringsaroundslots(block.inventory)},selectedindex="{block.inventory.selectedindex}"),dead={block.dead},deffactor={block.deffactor},atkfactor={block.atkfactor},reach={block.reach},handvalue={block.handvalue})'


def turnarraytoblocks(arrayofblocks: list = [[block], [block]]) -> list:
    """turntoblock() but applies to entire 2D Arrays.

    Args:
        listofblocks (list, optional): Toss in a 2D Array full of blocks. Defaults to [[block()], [block()]].

    Returns:
        list: Transforms every block in the list to its varname variable.
    """
    returning = []
    returner = []
    for YLevel in arrayofblocks:
        for block in YLevel:
            returner.append(block.varname)
        returning.append(returner)
        returner = []
    return returning


# - Window Stuff -


# Initiate an actual window to display stuff.
def initiatewindow():
    """Initalizes everything necessary to make windows.

    Returns: Nothing.
    """
    pygame.init()


# Close the window.
def closewindow():
    """Closes all windows.

    Returns: Nothing. It just closes all windows.
    """
    pygame.quit()


multiprocessing.freeze_support()
