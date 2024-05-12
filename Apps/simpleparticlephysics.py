print("Hold on, I'm getting shit ready for you.")

import api
import os
import math
from threading import Thread

generator = "gamedata\\partphys\\generator.py"

if not os.path.exists(generator):
    os.mkdir(generator)
    with open(generator, "w") as f:
        f.write("""
                """)

api.clear()
