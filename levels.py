import display
import interface

class Gates(object):

    def __init__(self):
        #CLOSED = -1, OPEN = 1
        self.gates = [-1,-1,-1,-1,-1]

    def play(self):
        display.print_gates(self.gates)
        while sum(self.gates) < 5:
            print 'Select a lever'
            lever = interface.int_input()
            self._switch(lever)
            display.print_gates(self.gates)

    def _switch(self, lever):
        pass
