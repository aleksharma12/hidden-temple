from levels import *
from sys import exit
import display
import interface

level_dict = {
    'gates': Gates()
    }

def run():
    #print introduction
    _load_game_intro()
    #while game is not complete
        #load next level
    _load_level('gates')
    #exit the game
    exit(0)

def _load_game_intro():
    display.print_text('text/foreword.txt')
    interface.press_enter_to_continue()

def _load_level(level):
    display.print_level_intro(level)
    level_dict[level]
