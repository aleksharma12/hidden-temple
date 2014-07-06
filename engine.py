from levels import *
import display
import interface

level_dict = {
    'gates': Gates()
    }

def run():
    #print introduction
    _load_game_intro()
    interface.press_enter_to_continue()
    #while game is not complete
        #load next level
    _load_level('gates')
    #exit the game

def _load_game_intro():
    display.print_text('text/foreword.txt')
    interface.press_enter_to_continue

def _load_level(level):
    display.print_level_intro(level)
    return level_dict[level]
