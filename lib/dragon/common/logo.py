# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import random

from lib.dragon.common.colors import color, yellow, red, bold
from lib.dragon.common.constants import CUCKOO_VERSION

def logo():
    """Cuckoo asciiarts.
    @return: asciiarts array.
    """
    apt = """
                            xxxxxx       xxxx
                             xxx        xxxx
                              x         xxxx
                   xxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxx              x
                        xxxx    xxxx    xxxx                        x
                 xxx    xxx     xxxxxxxxxxxxxxx         x
                          xx    xx                 xxxx      x
      x      xxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxx     x
          x             xxxxxxxxxxxx    xxxx                 x
            x           xxxx    xxxx    xxxxxxxxxxxxx          x
             x          xxxxxxxxxxxx    xxxx                x
            x           xxxx    xxxx    xxxxxxxxxxxxx                x
         x              xxxxxxxxxxxx    xxxx                           xx
       xx               xxxx    xxxx    xxxxxxxxxxxxx                  xxx
      xxx              xxxx  x  xxxx    xxxx                         xxxxx
       xxxx          xxxx     xxxxx      xxxx                     xxxxxx
         xxxxxxxxxxxxx         xxx         xxxxxxxxxxxxxxxxxxxxxxxxx
                                    /   \\       
   _                        )      ((   ))     (
  (@)                      /|\\      ))_((     /|\\
  |-|                     / | \\    (/\\|/\\)   / | \\                      (@)
  | | -------------------/--|-voV---\\`|'/--Vov-|--\\---------------------|-|
  |-|                         '^`   (o o)  '^`                          | |
  | |                               `\\Y/'                               |-|
  |-|                                                                   | |
  | |                        Dragon Sandbossss                          |-|
  | |                                                                   |-|
  |_|___________________________________________________________________| |
  (@)              l   /\\ /         ( (       \\ /\\   l                `\\|-|
                   l /   V           \\ \\       V   \\ l                  (@)
                   l/                _) )_          \\I
                                     `\\ /'
                                       `"""

    print(red(bold(apt)))
    print("")
    print(" Dragon Sandbox " + yellow(CUCKOO_VERSION))
    sys.stdout.flush()
