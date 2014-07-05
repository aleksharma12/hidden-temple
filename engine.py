import display
import format
from levels import *

level_dict = {
    'foreword': Foreword('foreword'),
    'gates': Gates('foreword')
    }

def load_level(level):
    #TODO: move intro text printing into level
    level_intro = format.to_txt(level)
    display.print_text(level_intro)

    level_dict[level]
