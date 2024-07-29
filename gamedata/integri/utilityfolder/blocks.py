from api import block, entity, inventory, Biome, OreConfiguration

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = block(
    varname="Air",
    image="#00AAFF",
    passable=True,
    breakablebytool=False,
    droptoolvalue=None,
    drop=None,
    falling=False
)
Grs = block(
    varname="Grs",
    image="#00FF00",
    passable=False,
    breakablebytool=True,
    droptoolvalue=1,
    drop="Grass",
    falling=False
)
Drt = block(
    varname="Drt",
    image="#945035",
    passable=False,
    breakablebytool=True,
    droptoolvalue=2,
    drop="Dirt",
    falling=False
)
Stn = block(
    varname="Stn",
    image="#606060",
    passable=False,
    breakablebytool=True,
    droptoolvalue=3,
    drop="Stone",
    falling=False
)
Snd = block(
    varname="Snd",
    image="#DDDD55",
    passable=False,
    breakablebytool=True,
    droptoolvalue=1,
    drop="Sand",
    falling=False
)
Bdr = block(
    varname="Bdr",
    image="#000000",
    passable=True,
    breakablebytool=False,
    droptoolvalue=None,
    drop=None,
    falling=False
)
plr = entity(
    varname="plr",
    image="#FFC000",
    maxhealth=100,
    health=100,
    armor=0,
    attack=5,
    defense=5,
    speed=1,
    position=[0,12],
    replace=Air,
    inventory=inventory(slotnum=25),
    dead=False,
    deffactor=0.5,
    atkfactor=0.5,
    handvalue=2
)
Iro = block(
    varname="Iro",
    image="#797979",
    passable=False,
    breakablebytool=True,
    droptoolvalue=4,
    drop="Iron ore",
    falling=False
)
Col = block(
    varname="Col",
    image="#202020",
    passable=False,
    breakablebytool=True,
    droptoolvalue=3,
    drop="Coal",
    falling=False
)
Irn = block(
    varname="Irn",
    image="#909090",
    passable=False,
    breakablebytool=True,
    droptoolvalue=4,
    drop="Iron bar",
    falling=False
)

# this is used for placing blocks
all_blocks_dict = {
    "Iron bar": Irn,
    "Coal": Col,
    "Iron ore": Iro,
    "Sand": Snd,
    "Stone": Stn,
    "Dirt": Drt,
    "Grass": Grs
}

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
        self.varname = "gsgl3r9vkjs3r" # necessity
        self.image = image
    
    def __str__(self):
        return self.image

    def __repr__(self):
        return self.image

# Oreconfig
print("Loading ore configuration..")

oreconfig = [
    OreConfiguration(
        2,
        1,
        10,
        20,
        Iro
    ),
    
    OreConfiguration(
        2,
        2,
        20,
        40,
        Col
    ),
    
    OreConfiguration(
        5,
        3,
        30,
        100,
        Iro
    ),
    
    OreConfiguration(
        5,
        3,
        50,
        120,
        Col
    ),
    
    OreConfiguration(
        7,
        5,
        100,
        200,
        Iro
    ),
    
    OreConfiguration(
        15,
        13,
        120,
        400,
        Col
    ),
    
    OreConfiguration(
        15,
        10,
        180,
        300,
        Iro
    ),
    
    OreConfiguration(
        25,
        17,
        390,
        700,
        Col
    ),
    
    OreConfiguration(
        25,
        20,
        300,
        700,
        Iro
    ),
    
    OreConfiguration(
        30,
        30,
        700,
        1500,
        Col
    ),
    
    OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    OreConfiguration(
        30,
        30,
        700,
        1500,
        Iro
    ),
    
    OreConfiguration(
        35,
        50,
        1500,
        2500,
        Iro
    ),
    
    OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    OreConfiguration(
        45,
        60,
        2500,
        4000,
        Iro
    ),
    
    OreConfiguration(
        45,
        60,
        2500,
        4000,
        Col
    ),
    
    OreConfiguration(
        50,
        100,
        4000,
        6000,
        Iro
    ),
    
    OreConfiguration(
        50,
        100,
        4000,
        6000,
        Col
    ),
    
    OreConfiguration(
        60,
        300,
        6000,
        10000,
        Iro
    ),
    
    OreConfiguration(
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
    Biome(
        "plains",
        50,
        10,
        50,
        [Grs, Drt, Drt, Drt, Drt]
    ),
    
    Biome(
        "desert",
        50,
        10,
        50,
        [Snd, Snd, Snd, Snd, Snd, Snd]
    )
]
