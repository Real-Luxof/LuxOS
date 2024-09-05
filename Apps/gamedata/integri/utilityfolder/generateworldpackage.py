from ...integri.utilityfolder.blocks import *
import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype: int):
    match worldtype:
        case 1:
            newworldtype: list[int, api.Limit] = [500, api.Limit(25, 495)]
        case 2:
            newworldtype: list[int, api.Limit] = [1000, api.Limit(50, 950)]
        case 3:
            newworldtype: list[int, api.Limit] = [1500, api.Limit(100, 1400)]
        case 4:
            newworldtype: list[int, api.Limit] = [2000, api.Limit(100, 1900)]
        case 5:
            newworldtype: list[int, api.Limit] = [3500, api.Limit(200, 3300)]
        case 6:
            newworldtype: list[int, api.Limit] = [5000, api.Limit(500, 4500)]
        case 7:
            newworldtype: list[int, api.Limit] = [7000, api.Limit(500, 6500)]
        case 8:
            newworldtype: list[int, api.Limit] = [8000, api.Limit(500, 7500)]
        case 9:
            newworldtype: list[int, api.Limit] = [10000, api.Limit(1000, 8000)]
    
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