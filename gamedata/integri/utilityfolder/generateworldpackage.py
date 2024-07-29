from ...integri.utilityfolder.blocks import *
import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype):
    match worldtype:
        case 1:
            newworldtype = [500, api.Limit(25, 495)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 2:
            newworldtype = [1000, api.Limit(50, 950)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 3:
            newworldtype = [1500, api.Limit(100, 1400)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 4:
            newworldtype = [2000, api.Limit(100, 1900)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 5:
            newworldtype = [3500, api.Limit(200, 3300)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 6:
            newworldtype = [5000, api.Limit(500, 4500)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 7:
            newworldtype = [7000, api.Limit(500, 6500)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 8:
            newworldtype = [8000, api.Limit(500, 7500)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
        case 9:
            newworldtype = [10000, api.Limit(1000, 8000)]
            world = api.optimized_generate(
                seed=None,
                width=newworldtype[0],
                height=newworldtype[0],
                air=Air,
                stone=Stn,
                limit=newworldtype[1],
                biomes=biomes,
                ore_config=oreconfig
            )
    return [world, newworldtype]