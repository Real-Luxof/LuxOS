from api import block
from api import Limit
from api import Biome
from api import OreConfiguration
from api import rand_num
from api import reachableindex
from api import mountain_terrain_type
from api import inverse_mountain_terrain_type
from api import plateau_terrain_type
from gamedata.integri.utilityfolder.blocks import *
import api
import time
import random

# I'm not even stopping to think of what i'm writing
# my coherent thoughts died at building a parser

# they say code as if the person who has to maintain
# your code will be a violent psychopath who knows
# where you live
# but god knows, google knows, and even i know that
# no person in the history of mankind will ever have
# to maintain this code
def generate_3d(
    seed: str,
    width: int,
    height: int,
    depth: int,
    
    air: block,
    
    stone: block,
    
    limit: Limit = Limit(100, 700),
    
    biomes: list[Biome] = [
            Biome(
                50,
                10,
                50,
                ["Grs", "Grs", "Drt", "Drt", "Drt", "Drt"]
            ),
            
            Biome(
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
    
    terrain_types: list = [mountain_terrain_type, inverse_mountain_terrain_type, plateau_terrain_type]
):
    """3D!!!!!!

    Summary: Need I say more?

    Args:
        seed (str): The seed for the world. Leave as None for the engine to pick one for you.
        width (int): The width of the world.
        height (int): The height of the world.
        depth (int): ̶g̶̶o̶̶d̶ ̶i̶̶'̶̶m̶ ̶h̶̶a̶̶r̶̶d̶ ̶a̶̶l̶̶r̶̶e̶̶a̶̶d̶̶y̶ DEPTH!!! what is there to be confused about?
        
        air (block): The thing that permeates open spaces.
        stone (block): The thing that permeates closed spaces.
        
        limit (Limit): Prevents world generation indexes above upper_limit and below lower_limit.

        biomes (list[Biome]): Biomes. Just look at the default to figure out its structure.

        ore_config (list[OreConfiguration]): Look at the default. spawn_limit limits how many of that ore can spawn at a single Y coordinate.
        
        next_block_limits (Limit): Look at the default. This controls how far up or down a block can be from another block.
        
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
    else:
        random.seed(seed)
    
    # set seed again cause i'm not sure if random.randint can change random.seed
    random.seed(seed)
    # Y is used to generate blocks below the top solid layer.
    X = 0
    Y = random.randint(limit.upper_limit, limit.lower_limit)
    Z = 0
    # generating_terrain blocks other terrain types from generating while one is on.
    generating_terrain = False
    # current_terrain_type is the currently generating terain type.
    current_terrain_type = None
    
    # - Create the initial space -

    # Pretty self-explanatory if you're not a silly lil dum dum.
    space = {}
    for k in range(depth):
        for j in range(height):
            for i in range(width):
                space[(i, j, k)] = air
    
    # initialize variables before jumping into O(n^3) territory.
    # Used later for structure and ore generation.
    # Now also used for 3D world generation.
    top_layers = []
    #top_layers.append([Y, X])
    # i need this for cohesive 3d world generation
    top_layer_index = 0

    for times_Z in range(depth):

        # Initalize some more variables
        # ofc this must happen
        X = 0
        # i have no thoughts i can express in words about this
        if len(top_layers) == width:
            Y = top_layers[0][0]

        top_layers = []
        #top_layers.append([Y, X])
        top_layer_index = 0
        
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
        # WE GETTING FIVE THOUSAND ZEROES IN THE FPS PAST THE DOT WITH THIS ONE 🗣🗣🗣💯💯!!!
        top_layer_index = -1 # explanations are for capitalists LOL
        
        for times_X in range(width):
            # biome_Y is used for biomes, so that the original Y is not contaminated.
            if len(top_layers) == width:
                top_layer_index += 1
                biome_Y = top_layers[top_layer_index][0]
            else:
                biome_Y = Y
            
            for times_Y in range(height):
                
                #print(current_biome_layers)
                #print(times_Y)
                # Actually do the biome work.
                if not reachableindex(space, (X, biome_Y, times_Z)):
                    break
                
                # If you don't know why times_Y is being used for this,
                # don't worry. I'm not explaining.
                if reachableindex(current_biome_layers, times_Y):
                    #print("MR KRABBBBSSSS")
                    space[(X, biome_Y, times_Z)] = current_biome_layers[times_Y]
                else:
                    space[(X, biome_Y, times_Z)] = stone
                
                biome_Y += 1
            
            # Out of times_Y, into times_X.
            
            # next_place is added to Y to decide how many blocks above or below the previous block the next
            # block should be.
            next_place = random.randint(
                next_block_limits.upper_limit,
                next_block_limits.lower_limit
            )
            
            # Terrain generation time. BUT ONLY IF MY ASSHOLE SAYS SO!
            # i have no clue where that came from im sorry
            if len(top_layers) != width:
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
            #print(f"width: {width}")
            #print(f"len(top_layers): {len(top_layers)}")
            #print(f"top_layer_index: {top_layer_index}")
            #if len(top_layers) != width:
            while Y + next_place < limit.upper_limit:
                next_place += 1
            
            while Y + next_place > limit.lower_limit:
                next_place -= 1
        
            #else:
            #    while top_layers[top_layer_index][0] + next_place < limit.upper_limit:
            #        next_place += 1
            #    
            #    while top_layers[top_layer_index][0] + next_place > limit.lower_limit:
            #        next_place -= 1
            
            # The show must go on!
            top_layers.append([Y, X])
            if X < width:
                #print(f"next_place: {next_place}")
                if len(top_layers) == width:
                    # yeah idk why i just think this will work
                    print(f"Y: {Y}")
                    print(f"next_place: {next_place}")
                    print(f"top_layers[top_layer_index]: {top_layers[top_layer_index]}")
                    Y = top_layers[top_layer_index][0] + next_place
                    # set this to the new Y at that index
                    top_layers[top_layer_index][0] = Y
                else:
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
                    
                    space[(top_block[1], spawn_area, Z)] = ore.block

    # FINALLY return the world.
    return space

start = time.time()
world = generate_3d(
    "999ab",
    100,
    100,
    100,
    Air,
    Stn,
    Limit(2, 98),
    biomes,
    oreconfig,
    Limit(-1, 1)
)
end = time.time()
print(f"Total world generation time: {end - start}s")

api.initiatewindow()
screen = api.setres(800, 600)
running = True

while running:
    for k in range(100):
        newscreen = []
        for j in range(100):
            newscreen.append([])
            for i in range(100):
                newscreen[-1].append(world[(i, j, k)])
            
        if api.isquit():
            api.closewindow()
            running = False
        
        api.display(
            screen,
            newscreen,
            8,
            6
        )
        api.wait(0.5)
    
