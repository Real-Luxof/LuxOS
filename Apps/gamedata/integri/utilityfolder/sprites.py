from ...integri.utilityfolder.blocks import *

black_black = placeholder_dry("#000000")
filler_black = placeholder_dry("#3F3F3F")
black = placeholder_dry("#10121C")
coal_dark_gray = placeholder_dry("#141414")
stone_gray = placeholder_dry("#474747")
coal_gray = placeholder_dry("#2E2E2E")
iron_light_gray = placeholder_dry("#ABABAB")
white = placeholder_dry("#FFFFFF")
dirt_light_brown = placeholder_dry("#A26D3F")
dirt_brown = placeholder_dry("#6E4C30")
sand_yellow = placeholder_dry("#FFED7C")
grass_green = placeholder_dry("#00A020")
drs = placeholder_dry("#63101B") # drs = darker_spot
dsp = placeholder_dry("#99192A") # dsp = dark_spot
lsp = placeholder_dry("#EC273F") # lsp = light_spot
TXT = placeholder_dry("#FFA2AC") # TXT = text

none_row = [None, None, None, None, None, None, None]
stone_row = [stone_gray, stone_gray, stone_gray, stone_gray, stone_gray, stone_gray, stone_gray]
dirt_row = [dirt_brown, dirt_brown, dirt_brown, dirt_brown, dirt_brown, dirt_brown, dirt_brown]
grass_row = [grass_green, grass_green, grass_green, grass_green, grass_green, grass_green, grass_green]
sand_row = [sand_yellow, sand_yellow, sand_yellow, sand_yellow, sand_yellow, sand_yellow, sand_yellow]
iron_row = [iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray]
filler_black_row = [filler_black, filler_black, filler_black, filler_black, filler_black, filler_black, filler_black]
filler_inv_row = [black_black]
black_row = []
black_inv_row = []
inventory_sprite = []
inventory_sprite_slot_coords = []

for i in range(20):
    black_row.append(black)
    black_inv_row.append(black_black)

for i in range(21):
    black_inv_row.append(black_black)

for i in range(5):
    filler_inv_row += filler_black_row
    filler_inv_row.append(black_black)

inventory_sprite.append(black_inv_row)
for i in range(5):
    for j in range(7):
        inventory_sprite.append(filler_inv_row)
    inventory_sprite.append(black_inv_row)

for i in range(5):
    for j in range(5):
        inventory_sprite_slot_coords.append(((i * 8) + 1, (j * 8) + 1))

health_bar_full = [
    [None] + black_row,
    [black, drs, drs, drs, drs, dsp, dsp, dsp, dsp, lsp, lsp, TXT, lsp, lsp, TXT, lsp, TXT, TXT, TXT, lsp, lsp],
    [black, drs, drs, drs, dsp, dsp, dsp, dsp, lsp, lsp, lsp, TXT, lsp, lsp, TXT, lsp, TXT, lsp, lsp, TXT, lsp],
    [black, drs, drs, dsp, dsp, dsp, dsp, dsp, lsp, lsp, lsp, TXT, TXT, TXT, TXT, lsp, TXT, lsp, lsp, TXT, lsp],
    [black, drs, drs, dsp, dsp, dsp, dsp, lsp, lsp, lsp, lsp, TXT, lsp, lsp, TXT, lsp, TXT, TXT, TXT, lsp, lsp],
    [black, drs, drs, dsp, dsp, dsp, dsp, lsp, lsp, lsp, lsp, TXT, lsp, lsp, TXT, lsp, TXT, lsp, lsp, lsp, lsp],
    [None] + black_row
]

coal_item = [
    none_row,
    none_row,
    none_row,
    [None, None, coal_gray, coal_gray, None, None, None],
    [None, coal_gray, coal_gray, coal_gray, coal_gray, None, None],
    [coal_gray, coal_gray, coal_dark_gray, coal_dark_gray, coal_gray, coal_gray, None],
    [coal_gray, coal_dark_gray, coal_dark_gray, coal_dark_gray, coal_dark_gray, coal_gray, coal_gray]
]

iron_ore_item = [
    stone_row,
    [stone_gray, iron_light_gray, stone_gray, stone_gray, stone_gray, stone_gray, stone_gray],
    [stone_gray, stone_gray, stone_gray, stone_gray, stone_gray, iron_light_gray, stone_gray],
    stone_row,
    [stone_gray, stone_gray, iron_light_gray, stone_gray, stone_gray, stone_gray, stone_gray],
    [stone_gray, stone_gray, stone_gray, stone_gray, iron_light_gray, stone_gray, stone_gray],
    stone_row
]

stone_item = [
    stone_row,
    stone_row,
    stone_row,
    stone_row,
    stone_row,
    stone_row,
    stone_row
]

dirt_item = [
    dirt_row,
    [dirt_brown, dirt_brown, dirt_brown, dirt_light_brown, dirt_brown, dirt_brown, dirt_brown],
    [dirt_light_brown, dirt_brown, dirt_brown, dirt_brown, dirt_brown, dirt_brown, dirt_light_brown],
    dirt_row,
    [dirt_brown, dirt_brown, dirt_brown, dirt_brown, dirt_light_brown, dirt_brown, dirt_brown],
    dirt_row,
    [dirt_brown, dirt_brown, dirt_light_brown, dirt_brown, dirt_brown, dirt_brown, dirt_brown]
]

grass_item = [
    grass_row,
    grass_row,
    [grass_green, dirt_brown, grass_green, grass_green, grass_green, grass_green, dirt_brown],
    [dirt_brown, dirt_brown, dirt_brown, grass_green, dirt_brown, dirt_brown, dirt_brown],
    dirt_row,
    dirt_row,
    dirt_row
]

sand_item = [
    sand_row,
    sand_row,
    sand_row,
    sand_row,
    sand_row,
    sand_row,
    sand_row
]

iron_bar_item = [
    [iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, white, iron_light_gray],
    [iron_light_gray, white, iron_light_gray, white, white, white, white],
    [iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, white, iron_light_gray],
    iron_row,
    [iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, iron_light_gray, white, iron_light_gray],
    iron_row,
    iron_row
]

#whole_lotta_nothing = [
#    none_row,
#    none_row,
#    none_row,
#    none_row,
#    none_row,
#    none_row,
#    none_row
#]

sprites = {
    #"None": whole_lotta_nothing,
    "Grass": grass_item,
    "Stone": stone_item,
    "Dirt": dirt_item,
    "Sand": sand_item,
    "Iron ore": iron_ore_item,
    "Coal": coal_item,
    "Iron bar": iron_bar_item
}
