from api import display
from api import reachableindex
from api import block
from api import entity
from api import Terrain
from api import mountain_terrain_type
from api import inverse_mountain_terrain_type
from api import plateau_terrain_type
from api import setres
from api import initiatewindow
from api import generate
from api import average
from math import floor
from api import isquit
from api import optimized_generate
from api import Limit
from api import OreConfiguration
from api import Biome
import random
import time
import os

Air = block(varname="Air",image="#00AAFF",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False)
Grs = block(varname="Grs",image="#00FF00",passable=False,breakablebytool=True,droptoolvalue=1,drop="Dirt",falling=False)
Drt = block(varname="Drt",image="#945035",passable=False,breakablebytool=True,droptoolvalue=2,drop=None,falling=False)
Stn = block(varname="Stn",image="#606060",passable=False,breakablebytool=True,droptoolvalue=3,drop="Stone",falling=False)
Snd = block(varname="Snd",image="#DDDD55",passable=False,breakablebytool=True,droptoolvalue=1,drop=None,falling=False)
#plr = entity(varname="plr",character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],replace=Air,inventory=inventory(slotnum=20),dead=False,deffactor=0.5,atkfactor=0.5)
Iro = block(varname="Iro",image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False)
Col = block(varname="Col",image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False)
Irn = block(varname="Irn",image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False)
Bdr = block(varname="Bdr",image="#000000",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Bedrock.

Aire = Air
Leaf = "Leaf"
Logg = "Logg"

biomes = [
    Biome(
        50,
        10,
        50,
        [Grs, Grs, Drt, Drt, Drt, Drt]
    ),
    
    Biome(
        50,
        10,
        50,
        [Snd, Snd, Snd]
    )
]

limit = Limit(
    2,
    598
)

oreconfig = [
    OreConfiguration(
        5,
        1,
        10,
        20,
        Iro
    ),
    
    OreConfiguration(
        30,
        3,
        20,
        40,
        Col
    ),
    
    OreConfiguration(
        30,
        3,
        30,
        100,
        Iro
    ),
    
    OreConfiguration(
        30,
        10,
        50,
        250,
        Col
    )
]

next_block_limits = Limit(
    -2,
    2
)
{
    "upper_limit": 2,
    "lower_limit": 2
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


unoptimized_oreconfig = { # oreconfigabove is used to define ore rarity and placement near the surface.
    "Ironore": (50, 10, 40, Iro),
    # Iron ore has a 1/50th (2%) chance of spawning between 10 and 40 blocks below the top solid block.
    # Its block is Iro.
    "Coalore": (50, 20, 30, Col),
    # Coal ore has a 1/50th (2%) chance of spawning between 20 and 30 blocks below the top solid block.
    # Its block is Col.
    
    # Switching to deeper blocks.
    
    "Ironore1": (45, 40, 60, Iro),
    # Iron ore has a 1/45th (2.2%) chance of spawning between 40 and 70 blocks below the top solid block.
    # Its block is Iro.
    "Coalore1": (45, 30, 50, Col),
    # Coal ore has a 1/45th (2.2%) chance of spawning between 30 and 70 blocks below the top solid block.
    # Its block is Col.
    
    # Just imagine this below every entry:
    # "[x] has a 1/[index0] chance of spawning between [index1] and [index2] blocks below the top solid block.
    # Its block is [index3]."
    # I don't wanna continue commenting.
    
    "Ironore2": (35, 70, 100, Iro),
    "Coalore2": (35, 70, 100, Col),
    
    "Ironore2": (30, 100, 200, Iro),
    "Coalore2": (30, 100, 200, Col),
    
    "Ironore2": (20, 200, 350, Iro),
    "Coalore2": (20, 200, 350, Col),
    
    "Ironore2": (15, 350, 450, Iro),
    "Coalore2": (15, 350, 450, Col),
    
    "Ironore2": (10, 450, 99999999999999, Iro),
    "Coalore2": (10, 450, 99999999999999, Col),
}

desert1 = [10, 30, Snd,Snd,Snd,Snd,Snd,Snd,Snd] # Biome layers for the Desert biome.
plains1 = [10, 30, Grs,Grs,Grs,Drt,Drt] # Biome layers for the Plains biome.
desert2 = [15,50,Snd,Snd,Snd,Snd,Snd,Snd]
plains2 = [15,50,Grs,Grs,Grs,Drt,Drt]
desert3 = [25,60,Snd,Snd,Snd,Snd,Snd,Snd]
plains3 = [25,60,Grs,Grs,Grs,Drt,Drt]
desert4 = [40,90,Snd,Snd,Snd,Snd,Snd,Snd]
plains4 = [40,90,Grs,Grs,Grs,Drt,Drt]
desert5 = [60,120,Snd,Snd,Snd,Snd,Snd,Snd]
plains5 = [60,120,Grs,Grs,Grs,Drt,Drt]
desert6 = [70,200,Snd,Snd,Snd,Snd,Snd,Snd]
plains6 = [70,200,Grs,Grs,Grs,Drt,Drt]
unoptimized_biomes = [desert1,plains1,desert2,plains2,desert3,plains3,desert4,plains4,desert5,plains5,desert6,plains6]


#def optimized_optimized_generate()


#average_calculation_repitition = 5
#calculation_width = 800
#calculation_height = 600
#
#optimized_times = []
#optimized_average = 0
#
#unoptimized_times = []
#unoptimized_average = 0
#
#print("calculating optimized times!")
#print()
#
#for times_optimized in range(average_calculation_repitition):
#    start = time.time()
#    optimized_generate(
#        seed="666",
#        width=calculation_width,
#        height=calculation_height,
#        air=Air,
#        stone=Stn,
#        limit=limit,
#        biomes=biomes,
#        ore_config=oreconfig
#    )
#    end = time.time()
#    optimized_times.append(end - start)
#
#optimized_average = average(optimized_times, True)
#
#print("calculating unoptimized times!")
#print()
#
#for times_unoptimized in range(average_calculation_repitition):
#    start = time.time()
#    generate(
#        width=calculation_width,
#        height=calculation_height,
#        biomes=unoptimized_biomes,
#        Air=Air,
#        Stn=Stn,
#        Bedrock=Bdr,
#        limit=(2, 598),
#        oreconfig=unoptimized_oreconfig
#    )
#    end = time.time()
#    unoptimized_times.append(end - start)
#
#unoptimized_average = average(unoptimized_times, True)
#
#print(f"optimized_average: {optimized_average}")
#print(f"optimized_times: {optimized_times}")
#print()
#print(f"unoptimized_average: {unoptimized_average}")
#print(f"unoptimized_times: {unoptimized_times}")
#
#with open("timingresults.txt", "w+") as f:
#    f.write(f"""optimized_average: {optimized_average}
#optimized_times: {optimized_times}
#
#unoptimized_average: {unoptimized_average}
#unoptimized_times: {unoptimized_times}""")

space = optimized_generate(
    seed=None,
    width=800,
    height=600,
    air=Air,
    stone=Stn,
    limit=limit,
    biomes=biomes,
    ore_config=oreconfig
)
initiatewindow()
screen = setres()
display(screen, space, 1, 1)
while True:
    time.sleep(1/20)
    if isquit():
        break
