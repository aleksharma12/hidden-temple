from levels import *
import display
import interface

level_dict = {
    'foreword': Foreword(),
    'gates': Gates()
    }

#PUBLIC
def run():
  _load_level('foreword')
  interface.press_enter_to_continue()
  _load_level('gates')

#PRIVATE
def _load_level(level):
    display.print_level_intro(level)
    return level_dict[level]
