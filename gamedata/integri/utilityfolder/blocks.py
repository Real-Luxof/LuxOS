from ... import api

# - Variables -
print("Loading Variables..")

# Blocks
print("Loading blocks..")

Air = api.block(image="#00AAFF",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Air. 
Grs = api.block(image="#00FF00",passable=False,breakablebytool=True,droptoolvalue=1,drop="Dirt",falling=False) # Define Grass.
Drt = api.block(image="#945035",passable=False,breakablebytool=True,droptoolvalue=2,drop=None,falling=False) # Define Dirt.
Stn = api.block(image="#606060",passable=False,breakablebytool=True,droptoolvalue=3,drop="Stone",falling=False) # Define Stone.
Snd = api.block(image="#DDDD55",passable=False,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Sand.
Bdr = api.block(image="#000000",passable=True,breakablebytool=False,droptoolvalue=None,drop=None,falling=False) # Define Bedrock.
plr = api.player(character="#000000",maxhealth=100,health=100,armor=0,attack=5,defense=5,speed=1,position=[0,12],inventory=api.inventory(slotnum=20),dead=False,deffactor=0.5,atkfactor=0.5) # Define the player.
Iro = api.block(image="#797979",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron ore",falling=False) # Define Iron ore.
Col = api.block(image="#202020",passable=False,breakablebytool=True,droptoolvalue=3,drop="Coal",falling=False) # Define Coal.
Irn = api.block(image="#909090",passable=False,breakablebytool=True,droptoolvalue=4,drop="Iron bar",falling=False) # Define Iron bar.

# Oreconfig
print("Loading ore configuration..")

global oreconfig # Declare oreconfig a global variable.
oreconfig = { # oreconfigabove is used to define ore rarity and placement near the surface.
    "Ironore": [50, 10, 40, Iro],
    # Iron ore has a 1/50th (2%) chance of spawning between 10 and 40 blocks below the top solid block.
    # Its block is Iro.
    "Coalore": [50, 20, 30, Col],
    # Coal ore has a 1/50th (2%) chance of spawning between 20 and 30 blocks below the top solid block.
    # Its block is Col.
    
    # Switching to deeper blocks.
    
    "Ironore1": [45, 40, 60, Iro],
    # Iron ore has a 1/45th (2.2%) chance of spawning between 40 and 70 blocks below the top solid block.
    # Its block is Iro.
    "Coalore1": [45, 30, 50, Col],
    # Coal ore has a 1/45th (2.2%) chance of spawning between 30 and 70 blocks below the top solid block.
    # Its block is Col.
    
    # Just imagine this below every entry:
    # "[x] has a 1/[index0] chance of spawning between [index1] and [index2] blocks below the top solid block.
    # Its block is [index3]."
    # I don't wanna continue commenting.
    
    "Ironore2": [35, 70, 100, Iro],
    "Coalore2": [35, 70, 100, Col],
    
    "Ironore2": [30, 100, 200, Iro],
    "Coalore2": [30, 100, 200, Col],
    
    "Ironore2": [20, 200, 350, Iro],
    "Coalore2": [20, 200, 350, Col],
    
    "Ironore2": [15, 350, 450, Iro],
    "Coalore2": [15, 350, 450, Col],
    
    "Ironore2": [10, 450, 99999999999999, Iro],
    "Coalore2": [10, 450, 99999999999999, Col],
}

# Biome layers
print("Loading biome layers..")

# Gonna do the oreconfig shenanigans with biomes.
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
biomes = [desert1,plains1,desert2,plains2,desert3,plains3,desert4,plains4,desert5,plains5,desert6,plains6]