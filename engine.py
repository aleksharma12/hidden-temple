from levels import *
from sys import exit
import display
import format
import user_input

level_list = [
    'gates',
    'mirrors'
    ]

def run():
    _load_game_intro()
    for level in level_list:
        _load_level(level)
    exit(0)

def _load_game_intro():
    display.print_game_intro()
    user_input.press_enter_to_continue()

def _load_level(level):
    cur_level = globals()[format.capitalize(level)]()
    display.print_level_intro(level)
    cur_level.play()
