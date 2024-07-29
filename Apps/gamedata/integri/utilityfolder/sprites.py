from ...integri.utilityfolder.blocks import *
from api import Surface, Color

# this is for the inventory don't mind this
black = placeholder_dry("#0000f0")
filler_black = placeholder_dry("#3F3F3F")

filler_black_row = [filler_black, filler_black, filler_black, filler_black, filler_black, filler_black, filler_black]
filler_inv_row = [black]
black_inv_row = []
inventory_sprite = []
inventory_sprite_slot_coords = []

for i in range(20):
    black_inv_row.append(black)

for i in range(21):
    black_inv_row.append(black)

for i in range(5):
    filler_inv_row += filler_black_row
    filler_inv_row.append(black)

inventory_sprite.append(black_inv_row)
for i in range(5):
    for j in range(7):
        inventory_sprite.append(filler_inv_row)
    inventory_sprite.append(black_inv_row)

for i in range(5):
    for j in range(5):
        inventory_sprite_slot_coords.append(((i * 8) + 1, (j * 8) + 1))

all_sprites_text = f"""health_bar_full
#0000f0 {"#10121C "*19}#10121C
#10121C {"#63101B "*4}{"#99192A "*4}{"#EC273F "*2}#FFA2AC {"#EC273F "*2}#FFA2AC #EC273F {"#FFA2AC "*3}#EC273F #EC273F
#10121C {"#63101B "*3}{"#99192A "*4}{"#EC273F "*3}#FFA2AC {"#EC273F "*2}#FFA2AC #EC273F #FFA2AC {"#EC273F "*2}#FFA2AC #EC273F
#10121C {"#63101B "*3}{"#99192A "*4}{"#EC273F "*3}{"#FFA2AC "*4}#EC273F #FFA2AC {"#EC273F "*2}#FFA2AC #EC273F
#10121C {"#63101B "*2}{"#99192A "*4}{"#EC273F "*4}#FFA2AC {"#EC273F "*2}#FFA2AC #EC273F {"#FFA2AC "*3}#EC273F #EC273F #EC273F
#10121C {"#63101B "*2}{"#99192A "*4}{"#EC273F "*4}#FFA2AC {"#EC273F "*2}#FFA2AC #EC273F #FFA2AC {"#EC273F "*3}#EC273F
#0000f0 {"#10121C "*19}#10121C
END
Coal
#0000f0 #0000f0 #0000f0 #0000f0 #0000f0 #0000f0 #0000f0
#0000f0 #0000f0 #0000f0 #0000f0 #0000f0 #0000f0 #0000f0
#0000f0 #0000f0 #0000f0 #333333 #0000f0 #0000f0 #0000f0
#0000f0 #0000f0 #2e2e2e #333333 #0000f0 #0000f0 #0000f0
#0000f0 #2e2e2e #262626 #2e2e2e #333333 #0000f0 #0000f0
#333333 #262626 #262626 #262626 #2e2e2e #333333 #0000f0
#262626 #262626 #141414 #141414 #262626 #2e2e2e #333333
END
Iron ore
#525252 #5e5e5e #525252 #5e5e5e #525252 #999999 #999999 
#5e5e5e #525252 #454545 #525252 #525252 #5e5e5e #454545 
#525252 #5e5e5e #454545 #5e5e5e #5e5e5e #525252 #525252 
#5e5e5e #999999 #525252 #525252 #454545 #525252 #999999 
#454545 #525252 #5e5e5e #454545 #454545 #525252 #999999 
#999999 #454545 #525252 #999999 #454545 #454545 #525252 
#5e5e5e #5e5e5e #454545 #5e5e5e #999999 #999999 #525252
END
Stone
#525252 #5e5e5e #525252 #5e5e5e #525252 #383838 #383838
#5e5e5e #525252 #454545 #525252 #525252 #5e5e5e #454545
#525252 #5e5e5e #454545 #5e5e5e #5e5e5e #525252 #525252
#5e5e5e #383838 #525252 #525252 #454545 #525252 #383838
#454545 #525252 #5e5e5e #454545 #454545 #525252 #383838
#383838 #454545 #525252 #383838 #454545 #454545 #525252
#5e5e5e #5e5e5e #454545 #5e5e5e #383838 #383838 #525252
END
Dirt
#78512f #6e4c30 #6e4c30 #593e27 #593e27 #45301e #593e27 
#6e4c30 #78512f #78512f #593e27 #78512f #593e27 #6e4c30 
#78512f #593e27 #593e27 #78512f #593e27 #6e4c30 #593e27 
#593e27 #6e4c30 #6e4c30 #45301e #45301e #593e27 #6e4c30 
#6e4c30 #593e27 #593e27 #78512f #593e27 #593e27 #45301e 
#45301e #593e27 #78512f #6e4c30 #78512f #593e27 #78512f 
#593e27 #78512f #593e27 #593e27 #593e27 #78512f #6e4c30
END
Grass
#5ab552 #61c258 #5ab552 #61c258 #5ab552 #52a64b #61c258
#61c258 #52a64b #61c258 #5ab552 #61c258 #5ab552 #5ab552
#5ab552 #5ab552 #52a64b #52a64b #593e27 #52a64b #52a64b
#52a64b #6e4c30 #52a64b #45301e #45301e #5ab552 #52a64b
#6e4c30 #593e27 #593e27 #78512f #593e27 #593e27 #61c258
#45301e #593e27 #78512f #6e4c30 #78512f #593e27 #78512f
#593e27 #78512f #593e27 #593e27 #593e27 #78512f #6e4c30
END
Sand
{"#FFED7C "*6}#FFED7C
{"#FFED7C "*6}#FFED7C
{"#FFED7C "*6}#FFED7C
{"#FFED7C "*6}#FFED7C
{"#FFED7C "*6}#FFED7C
{"#FFED7C "*6}#FFED7C
{"#FFED7C "*6}#FFED7C
END
Iron bar
{"#ABABAB "*5}#FFFFFF #ABABAB
#ABABAB #FFFFFF #ABABAB{" #FFFFFF"*4}
{"#ABABAB "*5}#FFFFFF #ABABAB
{"#ABABAB "*6}#ABABAB
{"#ABABAB "*5}#FFFFFF #ABABAB
{"#ABABAB "*6}#ABABAB
{"#ABABAB "*6}#ABABAB
END
Drt
#78512f #6e4c30 #6e4c30 #593e27 #593e27 #45301e #593e27 #593e27
#6e4c30 #78512f #78512f #593e27 #78512f #593e27 #6e4c30 #6e4c30
#78512f #593e27 #593e27 #78512f #593e27 #6e4c30 #593e27 #45301e
#593e27 #6e4c30 #6e4c30 #45301e #45301e #593e27 #6e4c30 #6e4c30
#6e4c30 #593e27 #593e27 #78512f #593e27 #593e27 #45301e #78512f
#45301e #593e27 #78512f #6e4c30 #78512f #593e27 #78512f #593e27
END
Grs
#61c258 #61c258 #52a64b #5ab552 #5ab552 #52a64b #5ab552 #52a64b
#61c258 #52a64b #5ab552 #52a64b #5ab552 #5ab552 #52a64b #61c258
#61c258 #52a64b #61c258 #61c258 #593e27 #52a64b #61c258 #45301e
#593e27 #61c258 #6e4c30 #45301e #45301e #61c258 #6e4c30 #6e4c30
#6e4c30 #593e27 #593e27 #78512f #593e27 #593e27 #45301e #78512f
#45301e #593e27 #78512f #6e4c30 #78512f #593e27 #78512f #593e27
END
Stn
#525252 #5e5e5e #525252 #5e5e5e #525252 #383838 #383838 #525252
#5e5e5e #525252 #454545 #525252 #525252 #5e5e5e #454545 #5e5e5e
#525252 #5e5e5e #454545 #5e5e5e #5e5e5e #525252 #525252 #454545
#5e5e5e #383838 #525252 #525252 #454545 #525252 #383838 #454545
#454545 #525252 #5e5e5e #454545 #454545 #525252 #383838 #525252
#383838 #454545 #525252 #383838 #454545 #454545 #525252 #454545
END
plr
#f3a833 #f3a833 #f3a833 #f3a833 #f3a833 #f3a833 #f3a833 #f3a833
#f3a833 #f3a833 #ffffff #f3a833 #f3a833 #ffffff #f3a833 #f3a833
#f3a833 #f3a833 #ffffff #f3a833 #f3a833 #ffffff #f3a833 #f3a833
#f3a833 #f3a833 #f3a833 #f3a833 #f3a833 #f3a833 #f3a833 #f3a833
#f3a833 #ffffff #f3a833 #f3a833 #f3a833 #f3a833 #ffffff #f3a833
#f3a833 #f3a833 #ffffff #ffffff #ffffff #ffffff #f3a833 #f3a833
END"""
all_sprites_text = all_sprites_text.split("\n")

sprites = {}

current_sprite_name = ""
current_sprite_contents: list[list[placeholder_dry]] = []
reading_sprite = False

for line in all_sprites_text:
    
    if line == "END":
        if reading_sprite:
            sprites[current_sprite_name] = current_sprite_contents
            current_sprite_contents = []
            reading_sprite = False
        continue
    
    elif not line.startswith("#"):
        if not reading_sprite:
            current_sprite_name = line
            current_sprite_contents.append([])
            reading_sprite = True
        else:
            sprites[current_sprite_name] = current_sprite_contents
            
            current_sprite_name = ""
            current_sprite_contents = []
            reading_sprite = False
    
    elif reading_sprite:
        for hex_code in line.split(" "):
            if hex_code == "":
                continue
            elif hex_code == "#0000f0":
                current_sprite_contents[-1].append(None)
            else:
                current_sprite_contents[-1].append(Color(hex_code))
            #elif current_sprite_name != "health_bar_full":
            #    current_sprite_contents[-1].append(Color(f"#{hex_code}"))
            #else:
            #    current_sprite_contents.append(f"#{hex_code}")
        current_sprite_contents.append([])

# Now to turn all those arrays into surfaces.
# there is a better way to do this but for readability i want surface creation and the hex interpreter
# to be at different parts of the file.
for key in sprites.keys():
    
    width = len(sprites[key][0]) 
    height = len(sprites[key])
#    if key == "health_bar_full":
#        width = 21
#        height = 7
#    elif len(sprites[key]) > 6:
#        width = 7
#        height = 7
#    else:
#        width = 8
#        height = 6

    new_sprite = Surface((width, height))

    for Y in range(len(sprites[key])):
        
        for X in range(len(sprites[key][Y])):
            if sprites[key][Y][X] != None:
                new_sprite.set_at((X, Y), sprites[key][Y][X])
            else:
                new_sprite.set_at((X, Y), (0, 0, 0, 0))
    
    sprites[key] = new_sprite
