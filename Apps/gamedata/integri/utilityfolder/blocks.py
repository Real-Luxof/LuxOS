import api

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = api.block(varname="Air",image="#00AAFF",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Air. 
Grs = api.block(varname="Grs",image="#00FF00",passable=False,breakablebytool=True,droptoolvalue=1,drop="Dirt",falling=False) # Define Grass.
Drt = api.block(varname="Drt",image="#945035",passable=False,breakablebytool=True,droptoolvalue=2,drop=None,falling=False) # Define Dirt.
Stn = api.block(varname="Stn",image="#606060",passable=False,breakablebytool=True,droptoolvalue=3,drop="Stone",falling=False) # Define Stone.
Snd = api.block(varname="Snd",image="#DDDD55",passable=False,breakablebytool=True,droptoolvalue=1,drop=None,falling=False) # Define Sand.
Bdr = api.block(varname="Bdr",image="#000000",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Bedrock.
plr = api.entity(varname="plr",character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],replace=Air,inventory=api.inventory(slotnum=20),dead=False,deffactor=0.5,atkfactor=0.5) # Define the player.
Iro = api.block(varname="Iro",image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False) # Define Iron ore.
Col = api.block(varname="Col",image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False) # Define Coal.
Irn = api.block(varname="Irn",image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False) # Define Iron bar.

setattr(Air, "light_level", 0)
setattr(Grs, "light_level", 0)
setattr(Drt, "light_level", 0)
setattr(Stn, "light_level", 0)
setattr(Snd, "light_level", 0)
setattr(Bdr, "light_level", 0)
setattr(plr, "light_level", 0)
setattr(Iro, "light_level", 0)
setattr(Col, "light_level", 0)
setattr(Irn, "light_level", 0)

# Oreconfig
print("Loading ore configuration..")

oreconfig = [
    {
        "spawn_chance": 2,
        "spawn_limit": 1,
        "upper_limit": 10,
        "lower_limit": 20,
        "block": Iro
    },
    
    {
        "spawn_chance": 2,
        "spawn_limit": 2,
        "upper_limit": 20,
        "lower_limit": 40,
        "block": Col
    },
    
    {
        "spawn_chance": 5,
        "spawn_limit": 3,
        "upper_limit": 30,
        "lower_limit": 100,
        "block": Iro
    },
    
    {
        "spawn_chance": 5,
        "spawn_limit": 3,
        "upper_limit": 50,
        "lower_limit": 120,
        "block": Col
    },
    {
        "spawn_chance": 7,
        "spawn_limit": 5,
        "upper_limit": 100,
        "lower_limit": 200,
        "block": Iro
    },
    
    {
        "spawn_chance": 15,
        "spawn_limit": 13,
        "upper_limit": 120,
        "lower_limit": 400,
        "block": Col
    },
    
    {
        "spawn_chance": 15,
        "spawn_limit": 10,
        "upper_limit": 180,
        "lower_limit": 300,
        "block": Iro
    },
    
    {
        "spawn_chance": 25,
        "spawn_limit": 17,
        "upper_limit": 390,
        "lower_limit": 700,
        "block": Col
    },
    {
        "spawn_chance": 25,
        "spawn_limit": 20,
        "upper_limit": 300,
        "lower_limit": 700,
        "block": Iro
    },
    
    {
        "spawn_chance": 30,
        "spawn_limit": 30,
        "upper_limit": 700,
        "lower_limit": 1500,
        "block": Col
    },
    
    {
        "spawn_chance": 30,
        "spawn_limit": 30,
        "upper_limit": 700,
        "lower_limit": 1500,
        "block": Iro
    },
    
    {
        "spawn_chance": 35,
        "spawn_limit": 50,
        "upper_limit": 1500,
        "lower_limit": 2500,
        "block": Col
    },
    
    {
        "spawn_chance": 35,
        "spawn_limit": 50,
        "upper_limit": 1500,
        "lower_limit": 2500,
        "block": Iro
    },
    
    {
        "spawn_chance": 45,
        "spawn_limit": 60,
        "upper_limit": 2500,
        "lower_limit": 4000,
        "block": Col
    },
    
    {
        "spawn_chance": 45,
        "spawn_limit": 60,
        "upper_limit": 2500,
        "lower_limit": 4000,
        "block": Iro
    },
    
    {
        "spawn_chance": 45,
        "spawn_limit": 60,
        "upper_limit": 2500,
        "lower_limit": 4000,
        "block": Col
    },
    
    {
        "spawn_chance": 50,
        "spawn_limit": 100,
        "upper_limit": 4000,
        "lower_limit": 6000,
        "block": Iro
    },
    
    {
        "spawn_chance": 50,
        "spawn_limit": 100,
        "upper_limit": 4000,
        "lower_limit": 6000,
        "block": Col
    },
    
    {
        "spawn_chance": 60,
        "spawn_limit": 300,
        "upper_limit": 6000,
        "lower_limit": 10000,
        "block": Iro
    },
    
    {
        "spawn_chance": 60,
        "spawn_limit": 300,
        "upper_limit": 6000,
        "lower_limit": 10000,
        "block": Col
    },
]

# Biomes
print("Loading biomes..")

# Gonna do the oreconfig shenanigans with biomes.
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
#    
#    {
#        "minimum_length": 25,
#        "maximum_length": 100,
#        "layers": [Grs, Grs, Grs, Grs, Grs, Drt, Drt, Drt, Drt, Drt, Drt, Drt]
#    },
#    
#    {
#        "minimum_length": 10,
#        "maximum_length": 50,
#        "layers": [Snd, Snd, Snd, Snd, Snd, Snd]
#    },
#    
#    
#    {
#        "minimum_length": 50,
#        "maximum_length": 75,
#        "layers": [Grs, Drt]
#    },
#    
#    {
#        "minimum_length": 1,
#        "maximum_length": 10,
#        "layers": [Snd]
#    },
#    
#    
#    {
#        "minimum_length": 20,
#        "maximum_length": 20,
#        "layers": [Grs, Grs, Grs, Drt]
#    },
#    
#    {
#        "minimum_length": 1,
#        "maximum_length": 10,
#        "layers": [Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd, Snd]
#    }
]