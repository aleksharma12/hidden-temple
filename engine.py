from levels import *
from sys import exit
import display
import interface

#TODO: this should theoretically be a list of levels you want
#      program should be smart enough to go get those files
#      and import them as needed
level_list = [
    Gates(),
    Mirrors()
    ]

def run():
    _load_game_intro()
    for level in level_list:
        _load_level(level)
    exit(0)

def _load_game_intro():
    display.print_text_from('text/foreword.txt')
    interface.press_enter_to_continue()

def _load_level(level):
    cur_level = level
    display.print_level_intro(cur_level.name)
    cur_level.play()
