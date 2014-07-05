from levels import *
import display

level_dict = {
    'foreword': Foreword(),
    'gates': Gates()
    }

def load_level(level):
    display.print_level_intro(level)
    return level_dict[level]
