import display
import user_input

class Gates(object):

    def __init__(self):
        #CLOSED = -1, OPEN = 1
        self.positions = [-1,-1,-1,-1,-1]
        self.moves = 0
        self.name = 'gates'

    def play(self):
        display.print_gates(self.positions, self.moves)
        while sum(self.positions) < 5:
            lever = user_input.select_lever()
            if lever != 0:
                self._switch(lever)
                self.moves += 1
            display.print_gates(self.positions, self.moves)
        display.print_gates_victory(self.moves)
        user_input.press_enter_to_continue()

    def _switch(self, lever):
        if lever == 1:
            self.positions[0] *= -1
            self.positions[4] *= -1
        elif lever == 2:
            self.positions[4] *= -1
        elif lever == 3:
            self.positions[1] *= -1
            self.positions[2] *= -1
            self.positions[4] *= -1
        elif lever == 4:
            self.positions[0] *= -1
            self.positions[3] *= -1
        else:
            print "Oh no! It looks like this lever has been jammed!"
            print "Too bad, since it's connected to ALL the gates...\n"

class Mirrors(object):

    def __init__(self):
        self.moves = 0
        self.name = 'mirrors'

    def play(self):
        display.print_maze(self.moves)
