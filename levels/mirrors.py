import display
import user_input

class Mirrors(object):

    def __init__(self):
        self.moves = 0
        self.name = 'mirrors'

    def play(self):
        display.print_maze(self.moves)
