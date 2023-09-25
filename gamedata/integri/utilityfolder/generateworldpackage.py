from ...integri.utilityfolder.blocks import *
from ... import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype, width, height):
    global widdth
    global heeight
    global oreconfigabove
    global oreconfigbelow
    widdth = width
    heeight = height
    world = {}
    match worldtype:
        case 1: newworldtype = [100, 5, 95]
        case 2: newworldtype = [200, 10, 190]
        case 3: newworldtype = [400, 20, 380]
        case 4: newworldtype = [700, 35, 665]
        case 5: newworldtype = [1000, 50, 950]
        case 6: newworldtype = [1500, 75, 425]
        case 7: newworldtype = [2000, 100, 1900]
        case 8: newworldtype = [3000, 150, 2850]
        case 9: newworldtype = [10000, 500, 9500]
    world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,[newworldtype[1],newworldtype[2]],oreconfig,)
    return [world, newworldtype]