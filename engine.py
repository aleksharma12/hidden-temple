from levels import *
from sys import exit
import display
import interface

#TODO: each level should be self-contained
level_dict = {
    'gates': Gates(),
    'mirrors': Mirrors()
    }

#TODO: load current level as cur_level
def run():
    _load_game_intro()
    _load_level('mirrors')
    _load_level('gates')
    exit(0)

def _load_game_intro():
    display.print_text_from('text/foreword.txt')
    interface.press_enter_to_continue()

#TODO: dynamic class instantiation
#TODO: cur_level.play()
def _load_level(level):
    display.print_level_intro(level)
    new_level = level_dict[level]
    new_level.play()
