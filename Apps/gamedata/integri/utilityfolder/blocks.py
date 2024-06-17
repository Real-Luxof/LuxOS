import api

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = api.block(varname="Air",image="#00AAFF",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Air. 
Grs = api.block(varname="Grs",image="#00FF00",passable=False,breakablebytool=True,droptoolvalue=1,drop="Grass",falling=False) # Define Grass.
Drt = api.block(varname="Drt",image="#945035",passable=False,breakablebytool=True,droptoolvalue=2,drop="Dirt",falling=False) # Define Dirt.
Stn = api.block(varname="Stn",image="#606060",passable=False,breakablebytool=True,droptoolvalue=3,drop="Stone",falling=False) # Define Stone.
Snd = api.block(varname="Snd",image="#DDDD55",passable=False,breakablebytool=True,droptoolvalue=1,drop="Sand",falling=False) # Define Sand.
Bdr = api.block(varname="Bdr",image="#000000",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Bedrock.
plr = api.entity(varname="plr",image="#FFC000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],replace=Air,inventory=api.inventory(slotnum=25),dead=False,deffactor=0.5,atkfactor=0.5) # Define the player.
Iro = api.block(varname="Iro",image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False) # Define Iron ore.
Col = api.block(varname="Col",image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False) # Define Coal.
Irn = api.block(varname="Irn",image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False) # Define Iron bar.

# Placeholder
print("Loading placeholders..")
class placeholder:
    """A block but for display purposes."""
    def __init__(
        self,
        varname: str,
        image: str,
        light_level: int,
        passable: bool
    ):
        self.varname = varname
        self.image = image
        self.light_level = light_level
        self.passable = passable
    
    def __str__(self):
        return self.image
    
    def __repr__(self):
        return self.image

class placeholder_dry:
    def __init__(
        self,
        image: str
    ):
        self.image = image
    
    def __str__(self):
        return self.image

    def __repr__(self):
        return self.image

# Oreconfig
print("Loading ore configuration..")

oreconfig = [
    api.OreConfiguration(
        2,
        1,
        10,
        20,
        Iro
    ),
    
    api.OreConfiguration(
        2,
        2,
        20,
        40,
        Col
    ),
    
    api.OreConfiguration(
        5,
        3,
        30,
        100,
        Iro
    ),
    
    api.OreConfiguration(
        5,
        3,
        50,
        120,
        Col
    ),
    
    api.OreConfiguration(
        7,
        5,
        100,
        200,
        Iro
    ),
    
    api.OreConfiguration(
        15,
        13,
        120,
        400,
        Col
    ),
    
    api.OreConfiguration(
        15,
        10,
        180,
        300,
        Iro
    ),
    
    api.OreConfiguration(
        25,
        17,
        390,
        700,
        Col
    ),
    
    api.OreConfiguration(
        25,
        20,
        300,
        700,
        Iro
    ),
    
    api.OreConfiguration(
        30,
        30,
        700,
        1500,
        Col
    ),
    
    api.OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    api.OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    api.OreConfiguration(
        35,
        50,
        1500,
        2500,
        Iro
    ),
    
    api.OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    api.OreConfiguration(
        45,
        60,
        2500,
        4000,
        Iro
    ),
    
    api.OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    api.OreConfiguration(
        50,
        100,
        4000,
        6000,
        Iro
    ),
    
    api.OreConfiguration(
        50,
        100,
        4000,
        6000,
        Col
    ),
    
    api.OreConfiguration(
        60,
        300,
        6000,
        10000,
        Iro
    ),
    
    api.OreConfiguration(
        60,
        300,
        6000,
        10000,
        Col
    )
]

# Biomes
print("Loading biomes..")

# Gonna do the oreconfig shenanigans with biomes.
biomes = [
    api.Biome(
        50,
        10,
        50,
        [Grs, Grs, Drt, Drt, Drt, Drt]
    ),
    
    api.Biome(
        50,
        10,
        50,
        [Snd, Snd, Snd]
    )
]
