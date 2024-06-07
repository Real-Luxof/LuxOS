from ...integri.utilityfolder.blocks import *
import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype):
    world = {}
    match worldtype:
        case 1:
            newworldtype = [500, {"upper_limit": 25, "lower_limit": 495}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 2:
            newworldtype = [1000, {"upper_limit": 50, "lower_limit": 950}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 3:
            newworldtype = [1500, {"upper_limit": 100, "lower_limit": 1400}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 4:
            newworldtype = [2000, {"upper_limit": 100, "lower_limit": 1900}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 5:
            newworldtype = [3500, {"upper_limit": 200, "lower_limit": 3300}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 6:
            newworldtype = [5000, {"upper_limit": 500, "lower_limit": 4500}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 7:
            newworldtype = [7000, {"upper_limit": 500, "lower_limit": 6500}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 8:
            newworldtype = [8000, {"upper_limit": 500, "lower_limit": 7500}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
        case 9:
            newworldtype = [10000, {"upper_limit": 1000, "lower_limit": 8000}]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                Air=Air,
                Stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig,
            )
    return [world, newworldtype]