from ...integri.utilityfolder.blocks import *
from ... import api

# Actual main function
print("Making generateworld function..")
def generateworld(worldtype):
    world = {}
    match worldtype:
        case 1: newworldtype = [100, 5, 95]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig)
        case 2: newworldtype = [200, 10, 190]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig)
        case 3: newworldtype = [400, 20, 380]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig)
        case 4: newworldtype = [700, 35, 665]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,averagesteepness=50,averagelength=40,averagesteepnessofcanyon=50,averagelengthofcanyon=40)
        case 5: newworldtype = [1000, 50, 950]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,averagesteepness=50,averagelength=50,averagesteepnessofcanyon=50,averagelengthofcanyon=50)
        case 6: newworldtype = [1500, 75, 425]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,averagesteepness=50,averagelength=70,averagesteepnessofcanyon=50,averagelengthofcanyon=70)
        case 7: newworldtype = [2000, 100, 1900]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,averagesteepness=50,averagelength=100,averagesteepnessofcanyon=50,averagelengthofcanyon=100)
        case 8: newworldtype = [3000, 150, 2850]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,averagesteepness=50,averagelength=140,averagesteepnessofcanyon=50,averagelengthofcanyon=140)
        case 9: newworldtype = [10000, 500, 9500]; world = api.generate(newworldtype[0],newworldtype[0],biomes,Air,Stn,Bdr,(newworldtype[1],newworldtype[2]),oreconfig,averagesteepness=60,averagelength=300,averagesteepnessofcanyon=60,averagelengthofcanyon=300)
    return [world, newworldtype]