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
        if lever == 1:
            self.gates[0] *= -1
        elif lever == 2:
            self.gates[1] *= -1
        elif lever == 3:
            self.gates[2] *= -1
        elif lever == 4:
            self.gates[3] *= -1
        elif lever == 5:
            self.gates[4] *= -1
        else:
            print "That number doesn't match a lever!\n"
