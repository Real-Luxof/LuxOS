from api import display
from api import reachableindex
import random
import time
import os

width = 70
height = 70
Air = "Air"
Grs = "Grs"
Drt = "Drt"
Stn = "Stn"
Bdr = "Bdr"
Leaf = "Leaf"
Logg = "Logg"
Aire = Air
I_ore = "I_ore"
L_ore = "L_ore"
config = [Grs, Grs, Drt, Drt, Drt, Drt]
oreconfig = {
    "ironore": [5, 10, 20, I_ore],
    "Luxian": [15, 20, 40, L_ore]
}
colors = {
    "Air": ["lightblue", "back", "  "],
    "Grs": ["green", "back", "  "],
    "Drt": ["yellow", "back", "  "],
    "Stn": ["lightblack", "back", "  "],
    "Bdr": ["lightwhite", "back", "  "],
    "Leaf": ["green", "back", "  "],
    "Logg": ["lightyellow", "back", "  "],
    "I_ore": ["white", "back", "  "],
    "L_ore": ["blue", "back", "  "]
}
structures = {
    "tree": {
        "struct": [
            [Aire, Leaf, Leaf, Leaf, Aire],
            [Leaf, Leaf, Leaf, Leaf, Leaf],
            [Leaf, Leaf, Logg, Leaf, Leaf],
            [Aire, Aire, Logg, Aire, Aire],
            [Aire, Aire, Logg, Aire, Aire],
        ],
        "spawnchance": 5,
        "ylevel": -1,
        "totalspace": [-4, 5]
    }
}
limit = [1, 30]



space = generate(width, height, config, Air, Stn, Bdr, limit=limit, oreconfig=oreconfig, structures=structures)
display(space,colors)
input()
while True:
    display(space,colors)
    time.sleep(1/20)
    os.system("cls")
