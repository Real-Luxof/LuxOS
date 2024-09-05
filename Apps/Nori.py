# Import the game engine
import api

# Define stuff


def decipher(text: str):
    """Turn text into an actual map for the game."""
    document = text.split("\n")
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
    del document[0]
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


levels = [
    """36
27
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
W W W W W W W W W W W W W W W W W W W W W W""",

    """16
30
W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W
W P . . . . . W . . . . W . . . W W . W . . . . . . . . . . . . . W . . . . . . . W . . . W . . . E W
W . . . . . . W . . W . . . W . . . . W W W W W . W . . . . . . . W . W W W W W . W . W . W . W W W W
W W W W . W W W W . W W W W W W W W . W . . . . . W . . . . . . . W . . . . . W . . . W . . . W . . W
W . . . . . W . W . . . . . . . . . W . . . . . . W . . . . . . . W W W W W . W W W W W W W W W W W W
W W W W W . . . . . W W W W W W W W W W . . . . . W . . . . . . . W . . . W . . . . W . . . W . . . W
W . . . W . . . . . . . W . . . . . . . . . . . . W W W W W W W W W W W . . W . W . . . W . . . . . W
W . . . W . W W W W W W W . W W W W W W W W W W W W W . . . . W . . . . W . W W W W W W W W W . W W W
W . . . W . W W W W W W . . . . . . . . . . . . . . . . W W . W W . W . W . . . . W . . . W . . . . W
W . . W . . . . W W W W W W W W . W W W W W W W W W W . W . . . . . W . . W . W . W . W . W W W W . W
W . W W . W W W W W W W W W W W W W W W W W W W W W W . W W W W W W W . . W . W . W . W . W . . . . W
W . W . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . W . . W . W . W . W . W . . . . W
W . W . W W W W W W . . . W W W W W W W W W W W W W W W W W W W W W W . . W . W . W . W . . . . . . W 
W . . . . . . . . W . . . W W W W . . . . . . . . . . . . . . . . . W . . W . W . . . W . W W W W W W
W . . . . . . . . W . . . . . . W . . . W W W W W W W W W W W W W W W . . W . W W W W W W W W W W W W
W W W W W W W . . W . . . . . . W . . . . . . . . . . . . . . . . . W . . W . . . . . . . . . . . . W
W . . . . . W . . W W W W . . W W W W W . . . W W W W W W W W . . W W . . W W W W W W W W W W W W . W
W W W W W . . . . . . W . . . . . . . . . . . W . . . . . . . . . . . . . W W W W W W W W W W W W . W
W . . . . . . . . . . W . . . . . . . . . . . W . . . . . . . . . . . . . . . . . . . . . . . . . . W
W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W""",

    """80
60
W W W W W W W W W W
W P . . . . . . . W
W W W W W W W W . W
W . . . . . . . . W
W . W W W W W W . W
W . . . . W . . . W
W . W W W . W . W W
W . W W W . W . W W
W . . . . . W . E W
W W W W W W W W W W"""
]

end_screen = """25
60
W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W
W P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . W
W . W W W W W . W . . . . . . . . W W W W . . . . . . . . W . W
W . . . W . . . W . . . . . . . . W . . . . . . . . . . . W . W
W . . . W . . . W . . . W W W . . W W W W . W . . . . . . W . W
W . . . W . . . W W W . W W W . . W . . . . W W W . W W W W . W
W . . . W . . . W . W . W . . . . W . . . . W . W . W . . W . W
W . . . W . . . W . W . W W W . . W W W W . W . W . W W W W . W
W . . . . . . . . . . . . . . . . . . . . . . . . . . . . . E W
W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W W"""

wall = api.block(varname="wall", image="#c0af97", passable=False)
dirt = api.block(varname="dirt", image="#613e1c", passable=True)
end = api.block(varname="end", image="#9884ad", passable=True)
player = api.entity(varname="player", image="#000000", replace=dirt)
# Replace is what was at somewhere before the player walked into it.
# Like dirt.

api.initiatewindow()
screen = api.setres(800, 600)

levelnum = 0
results = decipher(levels[levelnum])
map = results[0]
width = results[1]
height = results[2]
total_level_count = len(levels) - 1

while not api.isquit():
    api.display(screen, map, width, height)
    
    W_pressed = api.ispressed_key("w")
    A_pressed = api.ispressed_key("a")
    S_pressed = api.ispressed_key("s")
    D_pressed = api.ispressed_key("d")
    
    if W_pressed:
        moving_results = player.move("w", map, player.replace)
        map = moving_results[0]
        player.replace = moving_results[1]
    
    if A_pressed:
        moving_results = player.move("a", map, player.replace)
        map = moving_results[0]
        player.replace = moving_results[1]
    
    if S_pressed:
        moving_results = player.move("s", map, player.replace)
        map = moving_results[0]
        player.replace = moving_results[1]
    
    if D_pressed:
        moving_results = player.move("d", map, player.replace)
        map = moving_results[0]
        player.replace = moving_results[1]
    
    if player.replace.varname == "end" and levelnum < total_level_count:
        levelnum += 1
        results = decipher(levels[levelnum])
        map = results[0]
        width = results[1]
        height = results[2]
        player.replace = dirt
    
    elif player.replace.varname == "end" and levelnum >= total_level_count:
        if levelnum > total_level_count:
            break
        levelnum += 1
        results = decipher(end_screen)
        map = results[0]
        width = results[1]
        height = results[2]
        player.replace = dirt
    
    api.wait(1/15)

api.closewindow()
