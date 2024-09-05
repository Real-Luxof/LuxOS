from api import pygame as pg, isquit, clear, install
from threading import Thread
from string import ascii_lowercase
from os import system # my justification is title and running my own program

try:
    from colorama import just_fix_windows_console
except ModuleNotFoundError:
    install("colorama")
    from colorama import just_fix_windows_console

try:
    from requests import post
except ModuleNotFoundError:
    install("requests")
    from requests import post

just_fix_windows_console()
system("title ColorWarsDEFINITIVE")
icon = pg.image.load("gamedata\\colorwars\\ColorWarsTitleIcon.png")
pg.display.set_icon(icon)
pg.display.set_caption("ColorWarsDEFINITIVE")

class square:
    def __init__(
        self,
        image: pg.surface.Surface,
        num: int,
        color: str
    ):
        self.image = image
        self.num = num
        self.color = color

# define some vars
width = 20
height = 20
quit_time = False

outline_color = pg.Color(150, 150, 150)
empty_inside_color = pg.Color(255, 255, 255)
red_color = pg.Color("#EC273F")
green_color = pg.Color("#61C258")
blue_color = pg.Color("#3859B3")
yellow_color = pg.Color("#E8D282")


# make the empty square
neutral = pg.surface.Surface((32, 32), flags=pg.SRCALPHA)
neutral.set_at((0, 0), (255, 255, 255, 0))
neutral.set_at((1, 0), (255, 255, 255, 0))
neutral.set_at((0, 1), (255, 255, 255, 0))
neutral.set_at((1, 1), (255, 255, 255, 0))
pg.draw.rect(
    neutral,
    outline_color,
    (0, 0, 31, 31)
)
pg.draw.rect(
    neutral,
    empty_inside_color,
    (4, 4, 24, 24)
)

# make the colored squares
red = neutral.copy()
pg.draw.rect(red, red_color, (4, 4, 24, 24))

green = neutral.copy()
pg.draw.rect(green, green_color, (4, 4, 24, 24))

blue = neutral.copy()
pg.draw.rect(blue, blue_color, (4, 4, 24, 24))

yellow = neutral.copy()
pg.draw.rect(yellow, yellow_color, (4, 4, 24, 24))

color_to_colorval_dict = {
    "red": red_color,
    "green": green_color,
    "blue": blue_color,
    "yellow": yellow_color
}

# text time
# totally not a piskel C file dump
number_sprites = [
    [
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)]  
    ],
    [
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)]
    ],
    [
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)]
    ],
    [
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 0, 0, 0)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
    ],
    [
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)], 
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (20, 20, 20), (20, 20, 20)]
    ]
]
nums = [pg.surface.Surface((10, 20), flags=pg.SRCALPHA) for i in range(5)]

for index in range(len(number_sprites)):
    sprite = number_sprites[index]
    
    for Y in range(len(sprite)):
        for X in range(len(sprite[0])):
            nums[index].set_at((X, Y), (pg.Color(sprite[Y][X])))

zero = nums[0]
one = nums[1]
two = nums[2]
three = nums[3]
four = nums[4]
print(zero)
print(one)
print(two)
print(three)
print(four)
#zero = pg.transform.scale(nums[0], (10, 20))
#one = pg.transform.scale(nums[1], (10, 20))
#two = pg.transform.scale(nums[2], (10, 20))
#three = pg.transform.scale(nums[3], (10, 20))
#four = pg.transform.scale(nums[4], (10, 20))
#nums = [zero, one, two, three, four]
#8Y
#12X

# basic setup done
# main game incoming
grid = [[square(neutral, 0, "neutral") for i in range(20)] for j in range(20)]
status = "LOBBY"
current_turn = "red"

# I need to know where the window's X and Y coordinates are.
# please don't move the window?
# no i don't. pygame automatically handles that for me.
# :clown:
#SCREEN_INFO = pg.display.Info()
#SCREEN_HEIGHT = SCREEN_INFO.current_h
#SCREEN_WIDTH = SCREEN_INFO.current_w
#
#WINDOW_Y = SCREEN_HEIGHT // 2
#WINDOW_X = SCREEN_WIDTH // 2
#
#environ['SDL_VIDEO_WINDOW_POS'] = f"{WINDOW_X},{WINDOW_Y}"


def display_thread() -> None:
    """The function for the display thread. You're welcome."""
    global screen
    global grid
    global quit_time
    global nums
    global current_turn
    global color_to_colorval_dict
    clock = pg.time.Clock()
    sq_width = 32
    sq_height = 32
    while not quit_time:
        for un_mod_Y in range(len(grid)):
            for un_mod_X in range(len(grid[0])):
                X = un_mod_X * sq_width
                Y = un_mod_Y * sq_height
                
                grid_sq = grid[un_mod_Y][un_mod_X]
                
                image = grid_sq.image
                num = grid_sq.num
                color = grid_sq.color
                
                
                if color != current_turn:
                    screen.blit(image, (X, Y))
                    #print("SUCC")
                else:
                    image = pg.surface.Surface((32, 32), flags=pg.SRCALPHA)
                    pg.draw.rect(image, (0, 0, 0, 255), (0, 0, 31, 31))
                    pg.draw.rect(image, color_to_colorval_dict[color], (4, 4, 24, 24))
                    screen.blit(image, (X, Y))
                    #print("ZUCC")
                
                if color == "neutral":
                    continue
                
                if num < 4:
                    #print({nums[num]})
                    screen.blit(nums[num], ((X) + 11, (Y) + 8))
                    #print("success")
                else:
                    screen.blit(four, ((X) + 11, (Y) + 8))
        pg.display.flip()
        clock.tick(60)


def try_transform(
    some_list: list[list[pg.surface.Surface]],
    some_index: int,
    some_index_2: int,
    some_color: pg.surface.Surface,
    some_new_color: str
) -> None:
    """Attempts to transform some_list[some_index] according to the rules of the game.
    If it fails, it won't do anything."""
    if some_index < 0 or some_index_2 < 0:
        return None
    
    try:
        some_list[some_index][some_index_2].num += 1
        some_list[some_index][some_index_2].image = some_color
        some_list[some_index][some_index_2].color = some_new_color
    except Exception:
        pass

def tick(grid: list[list[square]]) -> None:
    """Performs exactly one tick of the rules on the grid.
You'll probably need to use this more than once to make sure all possible fours are eliminated."""
    global neutral
    new_grid = grid
    
    for Y in range(len(grid)):
        #print("OK")
        for X in range(len(grid[0])):
            #print("OK2")
            if grid[Y][X].num >= 4:
                #print("\x1b[6BYES!!!")
                image = grid[Y][X].image
                color = grid[Y][X].color
                try_transform(new_grid, Y + 1, X, image, color)
                try_transform(new_grid, Y - 1, X, image, color)
                try_transform(new_grid, Y, X + 1, image, color)
                try_transform(new_grid, Y, X - 1, image, color)
                new_grid[Y][X].image = neutral
                new_grid[Y][X].num = 0
                new_grid[Y][X].color = "neutral"
                pg.time.delay(500)
    
    return new_grid


def starter_game_loop(num_of_players: int) -> None:
    global grid
    global current_turn
    clock = pg.time.Clock()
    ticks_since_mouse_last_pressed = 0
    player_turn_index = 0
    
    players = [red.copy(), green.copy(), blue.copy(), yellow.copy()]
    players_colors = ["red", "green", "blue", "yellow"]
    
    for i in range(4 - num_of_players):
        del players[-1]
        del players_colors[-1]
    
    while not isquit():
        prev_grid = grid
        
        if player_turn_index == len(players):
            # first initial turns are over so proceed to the main game loop
            print("GET OUT!!!!")
            break
        
        print(f"\x1b[2K---CURRENT TURN: {current_turn}---")
        print(f"\x1b[2KPOS: {pg.mouse.get_pos()}")
        print(f"\x1b[2KFOCUSED: {pg.mouse.get_focused()}")
        print(f"\x1b[2KPRESSED: {pg.mouse.get_pressed(3)}")
        print(f"\x1b[5A")
        
        if pg.mouse.get_focused():
            if pg.mouse.get_pressed(3)[0] and ticks_since_mouse_last_pressed > 10:
                print(end="\x1b[5BWE IN\x1b[5A")
                ticks_since_mouse_last_pressed = 0
                mouse_X, mouse_Y = pg.mouse.get_pos()
                
                if grid[mouse_Y // 32][mouse_X // 32].num != 3:
                    grid[mouse_Y // 32][mouse_X // 32] = square(
                        players[player_turn_index % len(players)],
                        3,
                        players_colors[player_turn_index % len(players)]
                    )
                    player_turn_index += 1
                    current_turn = players_colors[player_turn_index % len(players)]
            
            elif ticks_since_mouse_last_pressed <= 10:
                ticks_since_mouse_last_pressed += 1
        
        clock.tick(60)


def main_game_loop_hotseat(num_of_players) -> None:
    global grid
    global current_turn
    clock = pg.time.Clock()
    
    ticks_since_mouse_last_pressed = 0
    
    players_colors = ["red", "green", "blue", "yellow"]
    
    for i in range(4 - num_of_players):
        del players_colors[-1]
    
    player_turn_index = 0
    current_turn = players_colors[player_turn_index % len(players_colors)]
    
    while not isquit():
        #print(obj in grid)
        #if player_turn_index == len(players):
        #    # first initial turns are over so proceed to the main game loop
        #    print("GET OUT!!!!")
        #    break
        
        print(f"\x1b[2K---CURRENT TURN: {current_turn}---")
        print(f"\x1b[2KPOS: {pg.mouse.get_pos()}")
        print(f"\x1b[2KFOCUSED: {pg.mouse.get_focused()}")
        print(f"\x1b[2KPRESSED: {pg.mouse.get_pressed(3)}")
        print(f"\x1b[5A")
        
        if pg.mouse.get_focused():
            if pg.mouse.get_pressed(3)[0] and ticks_since_mouse_last_pressed > 10:
                print(end="\x1b[5BWE IN\x1b[5A")
                ticks_since_mouse_last_pressed = 0
                mouse_X, mouse_Y = pg.mouse.get_pos()
                
                current_turn_color = players_colors[player_turn_index % len(players_colors)]
                
                if grid[mouse_Y // 32][mouse_X // 32].color == current_turn_color:
                    grid[mouse_Y // 32][mouse_X // 32].num += 1
                    player_turn_index += 1
                    current_turn = players_colors[player_turn_index % len(players_colors)]
            
            elif ticks_since_mouse_last_pressed <= 10:
                ticks_since_mouse_last_pressed += 1
        
        grid = tick(grid)
        
        player_dots = {"red": 0, "green": 0, "blue": 0, "yellow": 0}
        
        for Y in grid:
            for X in Y:
                if X.color != "neutral":
                    player_dots[X.color] += 1
        
        if player_dots["red"] == 0 and "red" in players_colors:
            del players_colors[players_colors.index("red")]
            player_turn_index += 1
        
        if player_dots["green"] == 0 and "green" in players_colors:
            del players_colors[players_colors.index("green")]
            player_turn_index += 1
        
        if player_dots["blue"] == 0 and "blue" in players_colors:
            del players_colors[players_colors.index("blue")]
            player_turn_index += 1
        
        if player_dots["yellow"] == 0 and "yellow" in players_colors:
            del players_colors[players_colors.index("yellow")]
            player_turn_index += 1
        
        current_turn = players_colors[player_turn_index % len(players_colors)]
        
        clock.tick(60)    


def compatibilify(grid: list[list[square]]):
    ret = "["
    
    for Y in grid:
        ret += "["
        for X in Y:
            ret += f"square(image={X.color}, num={X.num}, color=\"{X.color}\"),"
        
        ret = ret.removesuffix(",")
        ret += "],"
    
    ret = ret.removesuffix(",")
    
    ret += "]"
    
    return ret


def server_side_tick_thread():
    global grid
    for i in range(20):
        tick(grid)

def game_server(num_of_players: int) -> None:
    global grid
    
    try:
        from flask import Flask, request, jsonify
    except ModuleNotFoundError:
        system("pip install flask")
        from flask import Flask, request, jsonify
    
    from random import choice, randint
    
    clear()
    
    app = Flask("game server")
    
    global players
    global possible_players
    global colors_in_order_of_turns
    global current_turn
    global password_dict
    global lobby
    global turns
    
    players = []
    possible_players = ["red", "green", "blue", "yellow"]
    colors_in_order_of_turns = ["red", "green", "blue", "yellow"]
    current_turn = "red"
    password_dict = {}
    lobby = True
    turns = 0
    
    for i in range(4 - num_of_players):
        del possible_players[-1]
        del colors_in_order_of_turns[-1]
    
    @app.route("/", methods=["POST"])
    def handle():
        global grid
        global players
        global possible_players
        global colors_in_order_of_turns
        global current_turn
        global password_dict
        global lobby
        global turns
        
        data = request.get_json()
        response = {}
        
        if data["REQUEST"] == "JOIN":
            if not lobby:
                return jsonify({"RESPONSE": "NO"})
            
            password = ""
            for times in range(100):
                password += choice(ascii_lowercase)
            color = possible_players.pop(randint(0, len(possible_players) - 1))
            password_dict[color] = password
            players.append(colors_in_order_of_turns.pop(0))
            
            current_turn = players[0]
            
            response["RESPONSE"] = "YES"
            response["PASSWORD"] = password
            response["COLOR"] = color
            
            if len(possible_players) == 0:
                lobby = False
            
            return jsonify(response)
        
        elif data["REQUEST"] == "PLAY":
            if lobby:
                return jsonify({"RESPONSE": "WAIT", "STATUS": "LOBBY"})
            
            if password_dict[data["color"]] != data["password"]:
                return jsonify({"RESPONSE": "INVALID PASSWORD. WHAT DO YOU THINK YOU'RE DOING?"})
            
            if data["color"] != current_turn:
                return jsonify({"RESPONSE": "WAIT", "STATUS": current_turn})
            
            
            mouse_X, mouse_Y = (int(data["mouse_X"]), int(data["mouse_Y"]))
            
            X = mouse_X // 32
            Y = mouse_Y // 32
            
            if turns < len(players):
                grid[Y][X].color = current_turn
                grid[Y][X].num = 3
                turns += 1
                current_turn = players[turns % len(players)]
            elif grid[Y][X].color == current_turn:
                grid[Y][X].color = current_turn
                grid[Y][X].num += 1
                turns += 1
                current_turn = players[turns % len(players)]
            
            response = {
                "RESPONSE": "OK",
                "STATUS": current_turn,
                "grid": compatibilify(grid)
            }
            
            Thread(target=server_side_tick_thread).start()
            #server_side_tick_thread()
                
            player_dots = {"red": 0, "green": 0, "blue": 0, "yellow": 0}
            
            if turns < len(players):
                return jsonify(response)
            
            for Y in grid:
                for X in Y:
                    if X.color != "neutral":
                        player_dots[X.color] += 1
            
            if player_dots["red"] == 0 and "red" in players:
                del players[players.index("red")]
                turns += 1
            
            if player_dots["green"] == 0 and "green" in players:
                del players[players.index("green")]
                turns += 1
            
            if player_dots["blue"] == 0 and "blue" in players:
                del players[players.index("blue")]
                turns += 1
        
            if player_dots["yellow"] == 0 and "yellow" in players:
                del players[players.index("yellow")]
                turns += 1
            
            current_turn = players[turns % len(players)]
            
            response = {
                "RESPONSE": "OK",
                "STATUS": current_turn,
                "grid": compatibilify(grid)
            }
            
            return jsonify(response)
        
        elif data["REQUEST"] == "SHOW":
            if not lobby:
                current_turn = players[turns % len(players)]
            
            response = {
                "RESPONSE": "OK",
                "STATUS": current_turn,
                "grid": compatibilify(grid)
            }
            
            return jsonify(response)
    
    app.run(host="0.0.0.0")

def main_game_loop_client() -> None:
    global grid
    global status
    global current_turn
    clock = pg.time.Clock()
    ticks_since_mouse_last_pressed = 0
    good_to_go = True
    
    clear()
    server = "http://" + input("Input server IP: ") + ":5000"
    password = ""
    color = ""
    
    serv_response = post(server, json={"REQUEST": "JOIN"}).json()
    
    if serv_response["RESPONSE"] == "NO":
        print(f"ERR: SERVER REJECTED CONNECTION ATTEMPT, HERE'S A BRIEF OVERVIEW:")
        print(f"STATUS CODE: {response.status_code}")
        print(f"RETURN JSON: {response.json()}")
        good_to_go = False
    else:
        password = serv_response["PASSWORD"]
        color = serv_response["COLOR"]
        print(f"COLOR: {color}")
    
    while not isquit() and good_to_go:
        #print(obj in grid)
        #if player_turn_index == len(players):
        #    # first initial turns are over so proceed to the main game loop
        #    print("GET OUT!!!!")
        #    break
        
        print(f"\x1b[2K---CURRENT TURN: {current_turn}---")
        print(f"\x1b[2KPOS: {pg.mouse.get_pos()}")
        print(f"\x1b[2KFOCUSED: {pg.mouse.get_focused()}")
        print(f"\x1b[2KPRESSED: {pg.mouse.get_pressed(3)}")
        print(f"\x1b[5A")
        
        if pg.mouse.get_focused():
            if pg.mouse.get_pressed(3)[0] and ticks_since_mouse_last_pressed > 5:
                print(end="\x1b[5BWE IN\x1b[5A")
                ticks_since_mouse_last_pressed = 0
                mouse_X, mouse_Y = pg.mouse.get_pos()
                
                response = post(server, json={
                    "REQUEST": "PLAY",
                    "mouse_X": mouse_X,
                    "mouse_Y": mouse_Y,
                    "password": password,
                    "color": color
                })
                response_status_code = response.status_code
                response = response.json()
                
                try:
                    grid = eval(response["grid"])
                except Exception:
                    if response["RESPONSE"] == "WAIT":
                        status = response["STATUS"]
                        continue
                    
                    print(f"ERR, HERE'S A BRIEF OVERVIEW:")
                    print(f"STATUS CODE: {response_status_code}")
                    print(f"RETURN JSON: {response.json()}")
                    break
            
            elif ticks_since_mouse_last_pressed <= 10:
                ticks_since_mouse_last_pressed += 1
        
        grid = tick(grid)
        
        response = post(server, json={
            "REQUEST": "SHOW"
        }).json()
        
        grid = eval(response["grid"])
        
        if response["STATUS"] != "LOBBY":
            status = response["STATUS"] + " TURN"
            current_turn = response["STATUS"]
        else:
            status = response["STATUS"]
        
        clock.tick(15)  


if __name__ == "__main__":
    
    from sys import argv
    
    if len(argv) == 3:
        print(argv)
        if argv[1] == "BECOME_SERVER":
            game_server(int(argv[2]))
        
        quit()
    
    clear()
    print("1. Hotseat")
    print("2. Server")
    print("3. Client")
    
    p_input = ""
    choices = ["1", "2", "3"]
    
    while p_input not in choices:
        p_input = input("> ")
    
    clear()
    
    if p_input != "3":
        num_of_players = ""
        choices = ["2", "3", "4"]
        
        print("Number of players?")
        print("Minimum: 2")
        print("Maximum: 4")
        
        while num_of_players not in choices:
            num_of_players = input("> ")
        
        num_of_players = int(num_of_players)
    
    if p_input == "1":
        pg.display.init()
        screen = pg.display.set_mode((32 * width, 32 * height), 0, 32)
        Thread(target=display_thread).start()
        starter_game_loop(num_of_players)
        main_game_loop_hotseat(num_of_players)
    
    elif p_input == "2":
        system(f"start py ColorWars.py BECOME_SERVER {num_of_players}")
        
        pg.display.init()
        screen = pg.display.set_mode((32 * width, 32 * height), 0, 32)
        Thread(target=display_thread).start()
        
        print("Server started. Connect to your own server now.")
        pg.time.delay(2000)
        main_game_loop_client()
    
    elif p_input == "3":
        pg.display.init()
        screen = pg.display.set_mode((32 * width, 32 * height), 0, 32)
        Thread(target=display_thread).start()
        main_game_loop_client()
    quit_time = True
