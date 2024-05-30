# Import the game engine
import api

# Define variables
api.checkandmake("gamedata\\Nori\\levels") # Make the levels folder if it doesn't exist.
level1exists = api.checkpath("gamedata\\Nori\\level1.txt")
level1default = """35
26
W W W W W W W W W W W W W W W W W W W W W W
W . . W W . . . . . . . . . . . . . . . . W
W W . . . . W W . W W W W . . . . . . . . W
W . . W . . W W . W W W W . . . . . . . . W
W . . . . . . . . . . . . . . . . . . . . W
W . W W W W W . W W W W . W . W W W W W W W
W . W W W W W . W W W W W W . W W W W W W W
W . . . . . . . . . . E . . . . . . . . . W
W . W W W W W W W W W W . . W W W . W W . W
W . W W W W . W W W W W . . W . W W W W . W
W . . . . . . . . . . W . . . . . . . W . W
W . . . W W W W W W . W . . W W W W W W . W
W . W W . . . . . . . W . . W W W W W W . W
W . . . W W W W W W W W . . W W W W W W . W
W . . . . . . . W W . . . . W W W W W W . W
W . W W W W W . W . . . . . W W W W W W . W
W . W W W . . . . . . . . . . . . . . . . W
W . . . W . W . W W W W W W W W W W W W W W
W . W W W . . . W . . . . . . . . . . . . W
W . W W W . W W W W W W W W W W W W W W . W
W P . . . . . . . . . . . . . . . . . . . W
W W W W W W W W W W W W W W W W W W W W W W"""

wall = api.block(image="#c0af97", passable=False)
dirt = api.block(image="#613e1c", passable=True)
end = api.block(image="#9884ad", passable=True)
player = api.entity(character="", replace=dirt)
# Replace is what was at somewhere before the player walked into it.
# Like dirt.

# If level1 does not exist, make it.
if level1exists == False:
    level1 = open("gamedata\\Nori\\levels\\level1.txt", "w+")
    level1.write(level1default)

# Function to decipher the text files.
def decipher(pathtofile):
    """Turn a text into an actual map for the game"""
    file = open(pathtofile, "r")
    document = file.readlines()
    map = []
    # Document is like
    # document = [
    #   "wow",
    #   "how"
    #]
    #document[0] == "how"
    width = document[0]
    height = document[1]
    del document[0]
    del document[1]
    for line in document:
        line2 = line.split()
        # what split does is turn line from something like
        # "sajfh asfjha askjfhajsh haha!!!"
        # to
        # ["sajfh", "asfjha", "askjfhajsh", "haha!!!"]
        # Basically, it turns some text into a list
        map.append([])
        for word in line2:
            if word == "W": map[-1].append(wall)
            elif word == ".": map[-1].append(dirt)
            elif word == "E": map[-1].append(end)
            elif word == "P":
                map[-1].append(player)
                # player.position = [X - how right it is, Y - how down it is]
                player.position = [map[-1].index(player), map.index(map[-1])]
    
    return [map, int(width), int(height)]

api.initiatewindow()
screen = api.setres(800, 600)

leveldecipheringresults = decipher("gamedata\\Nori\\levels\\level1.txt")
map = leveldecipheringresults[0]
width = leveldecipheringresults[1]
height = leveldecipheringresults[2]

while not api.isquit():
    api.display(screen, map, width, height)
    
