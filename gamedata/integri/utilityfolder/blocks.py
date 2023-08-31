import os
import sys
# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the parent directory of the current file
parent_dir = os.path.dirname(current_file_path)

# Get the parent directory of the parent directory
grandparent_dir = os.path.dirname(parent_dir)

# Get the parent directory of the grandparent directory
greatgrandparent_dir = os.path.dirname(grandparent_dir)

# Get the parent directory of the greatgrandparent directory
final_dir = os.path.dirname(greatgrandparent_dir)

# Get the path to final_dir
final_path = os.path.abspath(final_dir)

sys.path.append(final_path)

import api

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
print("Loading ore configurations..")

global oreconfigabove # Declare oreconfigabove a global variable.
oreconfigabove = { # oreconfigabove is used to define ore rarity and placement near the surface.
    "Ironore": [20, 10, 40, Iro],
    # Iron ore has a 1/20th (5%) chance of spawning on each Y level between 10 and 40.
    # Its block is Iro.
    "Coalore": [20, 20, 30, Col]
    # Coal ore has a 1/20th (5%) chance of spawning on each Y level between 20 and 30.
    # Its block is Col.
}

global oreconfigbelow # Declare oreconfigbelow a global variable.
oreconfigbelow = { # oreconfigbelow is used to define ore rarity and placement below the surface level.
    "Ironore": [10, 0, 30, Iro],
    # Iron ore has a 1/10th (10%) chance of spawning on each Y level between 0 and 20.
    # Its block is Iro.
    "Coalore": [8, 0, 30, Col]
    # Coal ore has a 1/8th (12.5%) chance of spawning on each Y level between 0 and 30.
    # Its block is Col.
}

# Biome layers
print("Loading biome layers..")

desertlayers = [Snd,Snd,Snd,Snd,Snd,Snd,Snd] # Biome layers for the Desert biome.
plainslayers = [Grs,Grs,Grs,Drt,Drt] # Biome layers for the Plains biome.
allbiomes = [desertlayers,plainslayers]