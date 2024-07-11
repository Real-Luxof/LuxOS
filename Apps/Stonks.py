"""Most shitty simulation of economics ever, inspired by Victoria II."""

# - Loading Started -

# Import os. It is needed to check for and create folders, as well as to install modules.
import os

# vars yay
l_1 = list("|==========|")
bar = list("|$$$$$$$$$$|")
l_2 = list("|==========|")
random_facts = [
    "The U.S. federal reserve is not actually federal, it considers itself an independent central bank.",
    "The minimum wage in the U.S. has not been raised since 2009.",
    "Damn, the Bermuda triangle really fell off, didn't it?",
    "God save humanity, because no one else can.",
    "The official animal of Scotland is the unicorn.",
    "At the time of writing Nigeria is the most populous country in Africa.",
    "If you keep worrying about the past or future, you will always be stressed. Enjoy the present.",
    "Being born with a special talent is not gonna fix your life, damn it!",
    "At the time of writing 9.3 million Venezuelans are moderately to severely food insecure, which is one-third of the population.",
    "Having dream exams way past your school life and into your adult life is not normal.",
    "*Insert Chinese child labor joke here*",
    "*Insert Chinese dog eating joke here*",
    "Holy shit, you have bad taste in porn.",
    "Who cares? I do. I care. You should too.",
    "Life is way better when you start yapping. Keep yapping.",
    "I am high out of my mind right now.",
    "Whopper Whopper Whopper Whopper\nJunior Double Triple Whopper\nFlame-grilled taste with perfect toppers\nI rule\nI rule\nI rule this day."
]

suitable_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l_1)
print(bar)
print(l_2)

def display_bar() -> None:
    """Display the loading bar."""
    global l_1
    global l_2
    global bar
    
    print("Loading...")
    
    for char in l_1:
        print(char, end="")
    print()
    
    for char in bar:
        print(char, end="")
    print()
    
    for char in l_2:
        print(char, end="")
    print()

def increment() -> None:
    """Make the loading bar progress ahead and display it."""
    global l_1
    global l_2
    global bar
    global suitable_choices
    
    total_ls = [l_1, l_2]
    api.clear()
    
    index = suitable_choices.pop(random.choice(range(len(suitable_choices)))) # 5 billion parenthesis :)
    random.choice(total_ls)[index] = "$"
    bar[index] = " "
    
    display_bar()

display_bar()

print("Chocolate chip chip chip chocolate chip cookies..")
try: import api
except(ModuleNotFoundError): input("Couldn't find the engine, I'm gonna quit now! LUL."); quit

print("Planting crack in particularly poor communities..")
import random

print("Sending money to local politicians..")
from importlib import import_module

print("I can't believe *insert journalist name here* would shoot themselves after exposing us!")
from typing import NamedTuple

increment()

# Folder variables used for loading

print("Loading pathfinding to various government offices..")
files = "gamedata\\stonks" # Variable for main game files
save = "gamedata\\stonks\\save.py" # Variable for the save.
                                   # Yeah, I'm too lazy to do save management. So what?
#st = "gamedata\\stonks\\soundtrack" # Variable for the soundtrack folder.

# Real file shit

print("Checking and installing Windows XP/98 on all computers across every bank..")
if os.path.exists(files) == False:
    print("Installing..")
    os.system("md " + files)

if os.path.exists(save) == False:
    print("Installing..")
    os.system("md " + save)

increment()

print("Blaming it on the *insert group name here*..")
# items n stuff
class Item(NamedTuple):
    name: str
    num: int
    per_person: int
    effect: str

class TypeOfNeed(NamedTuple):
    name: str
    buff: list[str]
    debuff: list[str]

#class Effect(NamedTuple):
#    no_effect = False
#    action: str
#    trait: str
#    num_to_add_1: int
#    num_to_add_2: int
#
#class EffectFloat(NamedTuple):
#    no_effect = False
#    action: str
#    trait: str
#    num_to_add_1: float
#    num_to_add_2: float
#
#class NoEffect:
#    no_effect = True
#
# that's a lot of classes
# i don't like them

print("Poorly addressing a crisis..")
# jobs
class Miner:
    # That girl's a mineeeer, that girl's a mineeer!
    job_needs = [
        Item("PICKAXE", 1, 1, "debuff work disable"), # this is what happens when the needs are not met
        Item("TORCH AND LIGHTER", 5, 1, "debuff work pop -1 -50")
    ]
    extra_needs = {
        Item("CANARY", 1, 10, "buff work pop 1 1") # this is what happens when the needs are met
    }
    pop_effects = [
        "work satisfaction -0.00001 -0.0001",
        "work consciousness 0.00001 0.0001", # mining isn't really a desirable job
        "work pop -1 -1" # yeah das why also cuz u in a mine damnit
    ]
    
    possible_produce = [
        "70.0 10 COAL", # chance_of_produce num_of_produce name_of_produce is the format here
        "30.0 5 IRON_ORE"
    ]

class Lumberjack:
    job_needs = [
        Item("AXE", 1, 1, "debuff work disable")
    ]
    pop_effects = [
        "work consciousness 0.00001 0.00005" # you wouldn't wanna be cutting trees all day but at least
        # you aint a miner
    ]
    
    possible_produce = [
        "100.0 10 WOOD_LOG"
    ]

# enough near commentless coding, time to actually make you understand.
# tf is this "effect" thing and how does it work?
# simple, like this: "type_of_buff action pop_trait num_to_add_1 num_to_add_2"
# type_of_buff can be "debuff" or "buff", "buff" will happen if the need is met and "debuff" for the opposite.
# anything with type_of_buff is usually not an Item so screw that
# action is on what action the pop will have an effect.
# pop_trait is what trait of the pop the effect is working on.
# the num_to_adds are a range of nums of which a number is randomly added.
# also use "action disable" to disable that action :D
# yield is a special trait through which you can modify the produce
# its types are yield_int and yield_percent respectively
# you can guess what those do by their names

print("VR Glasses, buy today.")
class Poor:
    important_needs = [
        TypeOfNeed(
            "BASIC",
            [
                "passive satisfaction 0.0005 0.002"
            ],
            [
                "passive pop -1 -250" # if u aint getting BASIC needs you DEAD
            ]
        ),
        TypeOfNeed(
            "JOB",
            [
                "passive satisfaction 0.0005 0.002"
            ],
            [
                "" # job decides debuff/disable or whatevs
            ]
        )
    ]
    # they don't care if they don't get luxuries, but it would be nice

class Middle:
    important_needs = [
        TypeOfNeed(
            "BASIC",
            [
                "passive satisfaction 0.0005 0.002"
            ],
            [
                "passive pop -1 -250"
            ]
        ),
        TypeOfNeed(
            "JOB",
            [
                "passive satisfaction 0.0005 0.002"
            ],
            [
                "" # job decides debuff/disable or whatevs
            ]
        ),
        TypeOfNeed(
            "LUXURY-1",
            [
                "passive satisfaction 0.005 0.009",
                "passive consciousness -0.009 -0.005"
            ],
            [
                "passive consciousness 0.005 0.009"
                # no luxuries? at their richness? yeah, right.
            ]
        )
    ]
    # kinda rich, they want nice things too.

class Rich:
    important_needs = [
        TypeOfNeed(
            "BASIC",
            [
                "passive satisfaction 0.0005 0.002"
            ],
            [
                "passive pop -1 -250"
            ]
        ),
        TypeOfNeed(
            "JOB",
            [
                "passive satisfaction 0.0005 0.002"
            ],
            [
                "" # job decides debuff/disable or whatevs
            ]
        ),
        TypeOfNeed(
            "LUXURY-1",
            [
                "passive consciousness -0.009 -0.005"
            ],
            [
                "passive consciousness 0.009 0.03",
                "passive satisfaction -0.009 -0.005"
            ]
        ),
        TypeOfNeed(
            "LUXURY-2",
            [
                "passive satisfaction 0.05 0.009"
            ],
            [
                "passive consciousness 0.009 0.03"
            ]
        )
    ]
    # i don't need my designer clothes, but i do need that roasted turkey filled with mayo.
    # yeah LUXURY-3 exists which absolutely blows the minds of whoever gets it

# oh btw don't worry, if the higher classes don't get their stuff for a long enough time
# they'll either get demoted (bad because the factories close) or make petitions n stuff

print("Granting consciousness to Humanity at the low low price of $3.99..")
# Population unit
class POP:
    def __init__(
        self,
        pop: int,
        satisfaction: float,
        consciousness: float,
        social_class,
        job
    ):
        self.pop = pop # num of people
        self.satisfaction = satisfaction # satisfaction with life
        self.consciousness = consciousness # how conscious they are of what's going on around them
        # decides what kinds of needs they consider really important
        # and what jobs they'll have
        self.social_class = social_class
        # supposed to be one of the job classes
        self.job = job
            
