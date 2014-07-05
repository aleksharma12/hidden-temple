import display
import format
from levels import *

level_dict = {
    'foreword': Foreword(),
    'gates': Gates()
    }

def load_level(level):
    #TODO: move intro text printing into level
    level_intro = format.to_txt(level)
    display.print_text(level_intro)

    return level_dict[level]
