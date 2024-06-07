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
    {
        "minimum_length": 10,
        "maximum_length": 50,
        "layers": [Grs, Grs, Drt, Drt, Drt, Drt]
    },
    
    {
        "minimum_length": 10,
        "maximum_length": 50,
        "layers": [Snd, Snd, Snd]
    }
]

limit = {
    "upper_limit": 200,
    "lower_limit": 600
}

oreconfig = [
    {
        "spawn_chance": 5,
        "spawn_limit": 1,
        "upper_limit": 10,
        "lower_limit": 20,
        "block": Iro
    },
    
    {
        "spawn_chance": 30,
        "spawn_limit": 3,
        "upper_limit": 20,
        "lower_limit": 40,
        "block": Col
    },
    
    {
        "spawn_chance": 30,
        "spawn_limit": 3,
        "upper_limit": 30,
        "lower_limit": 100,
        "block": Iro
    },
    
    {
        "spawn_chance": 30,
        "spawn_limit": 10,
        "upper_limit": 50,
        "lower_limit": 250,
        "block": Col
    },
]

next_block_limits = {
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


def optimized_generate(
    seed: str,
    width: int,
    height: int,
    
    Air: block,
    
    Stone: block,
    
    limit: dict = {
        "upper_limit": 100,
        "lower_limit": 700
    },
    
    biomes: list = [
            {
                "minimum_length": 10,
                "maximum_length": 50,
                "layers": ["Grs", "Grs", "Drt", "Drt", "Drt", "Drt"]
            },
            
            {
                "minimum_length": 10,
                "maximum_length": 50,
                "layers": ["Snd", "Snd", "Snd"]
            }
        ],
        
    ore_config: list = [
            {
                "spawn_chance": 5,
                "spawn_limit": 1,
                "upper_limit": 10,
                "lower_limit": 20,
                "block": "IronOre"
            },
            
            {
                "spawn_chance": 30,
                "spawn_limit": 3,
                "upper_limit": 20,
                "lower_limit": 40,
                "block": "CoalOre"
            },
            
            {
                "spawn_chance": 30,
                "spawn_limit": 3,
                "upper_limit": 30,
                "lower_limit": 100,
                "block": "IronOre"
            },
            
            {
                "spawn_chance": 30,
                "spawn_limit": 10,
                "upper_limit": 50,
                "lower_limit": 250,
                "block": "CoalOre"
            },
        ],
    
    next_block_limits = {
        "upper_limit": -2,
        "lower_limit": 2
    },
        
    starting_Y: int = None, # my reasoning for this is that starting_Y will be randomly chosen if None.
    terrain_types: list = [mountain_terrain_type, inverse_mountain_terrain_type, plateau_terrain_type]
):
    """Time to toss the so-called "epitome of my labor" in the trash and make a better one.

    Summary: it generates a world, but hopefully faster.

    Args:
        seed (str): The seed for the world. Leave as None for the engine to pick one for you.
        width (int): The width of the world.
        height (int): The height of the world.
        
        Air (block): The thing that permeates open spaces.
        Stone (block): The thing that permeates closed spaces.
        
        limit (dict, optional): Prevents world generation indexes above upper_limit and below lower_limit.

        biomes (list, NOT optional): Biomes. Just look at the default to figure out its structure.

        ore_config (list, optional): Look at the default. spawn_limit limits how many of that ore can spawn at a single Y coordinate.
        
        next_block_limits (dict, optional): Look at the default. This controls how far up or down a block can be from another block.
        
        starting_Y (int, optional): Where to start from? Excellent for chunk building as it allows for chunks connecting. If left as None, the engine will randomly pick one for you.
        terrain_types (list): What terrain types do you want to be able to be generated? Defaults to the default ones from the Engine.

    Returns:
        A 2D Array. This is your 2D world.
    """
    # - Variable Checking -
    
    # Select the first biome.
    if biomes == []:
        print("HEY! YOU FORGOT TO GIVE ME ACTUAL BIOMES!!\n[biomes] IS LITERALLY JUST A BLANK LIST!")
        ValueError()
    
    # None is pretty falsy, so I'll just use if not [variable].
    if not seed:
        seed = random.randint(0, 1000000000000)
    else:
        random.seed(seed)
    
    if not starting_Y:
        starting_Y = random.randint(limit["upper_limit"], limit["lower_limit"])
    
    # set seed again cause i'm not sure if random.randint can change random.seed
    random.seed(seed)
    # Y is used to generate blocks below the top solid layer.
    Y = starting_Y
    X = 0
    # generating_terrain blocks other terrain types from generating while one is on.
    generating_terrain = False
    # current_terrain_type is the currently generating terain type.
    current_terrain_type = None
    
    # - Create the initial space -

    # Pretty self-explanatory if you're not a silly lil dum dum.
    space = []
    for ylevel in range(height):
        space.append([])
        
        for xlevel in range(width):
            space[-1].append(Air)

    # - Add blocks (finally use biomes) -

    # Initalize some variables

    # [Y] is used for biomes, to generate things below the top layer.
    # Used later for structure and ore generation.
    top_layers = []
    top_layers.append([starting_Y, X])
    
    biome = random.choice(biomes)
    
    current_biome_length = 1
    current_biome_layers = biome["layers"]
    current_biome_max_length = random.randint(
        biome["minimum_length"],
        biome["maximum_length"]
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
                space[biome_Y][X] = Stone
            
            if biome_Y < height:
                biome_Y += 1
        
        # Out of times_Y, into times_X.
        
        # next_place is added to Y to decide how many blocks above or below the previous block the next
        # block should be.
        next_place = random.randint(
            next_block_limits["upper_limit"],
            next_block_limits["lower_limit"]
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
                    print(f"type: {type.name}")
                
        
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
        while Y + next_place < limit["upper_limit"]:
            #print("next place must go down")
            #print(f"next_place going down: {next_place}")
            next_place += 1
        
        while Y + next_place > limit["lower_limit"]:
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
        current_biome_length += 1
        
        # If the biome's length if finished, select a different one.
        if current_biome_length > current_biome_max_length:
                biome = random.choice(biomes)

                current_biome_length = 1
                current_biome_layers = biome["layers"]
                current_biome_max_length = random.randint(
                    biome["minimum_length"],
                    biome["maximum_length"]
                )
        
        if current_terrain_type_length > current_terrain_type_max_length:
            generating_terrain = False

    # Ore and structure generation

    # Ore -
    for top_block in top_layers:
        for ore in ore_config:
            
            for times in range(random.randint(1, ore["spawn_limit"])):
                # Part of the great de-nesting.
                if not random.randint(1, 100) <= ore["spawn_chance"] or not reachableindex(
                    space,
                    top_block[0] + ore["upper_limit"]
                ):
                    continue
                
                # Self-explanatory for the most part.
                spawn_area = random.randint(
                    ore["upper_limit"],
                    ore["lower_limit"]
                ) + top_block[0]
                
                # If spawn_area's too far away, just reel it back in.
                # Yeah this might cause some ores to cluster up at the bottom of the world, so what?
                if spawn_area >= height:
                    continue
                
                space[spawn_area][top_block[1]] = ore["block"]

    # FINALLY return the world.
    return space

#average_calculation_repitition = 5
#calculation_width = 2000
#calculation_height = 2000
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
#        Air=Air,
#        Stone=Stn,
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
#        oreconfig=unoptimized_oreconfig,
#        logging=False
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
   Air=Air,
    Stone=Stn,
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
