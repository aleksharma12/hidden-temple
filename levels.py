import display
import interface

class Gates(object):

    def __init__(self):
        #CLOSED = 0, OPEN = 1
        self.gates = [0,0,0,0,0]

    def play(self):
        while sum(self.gates) < 5:
            display.print_gates(self.gates)
            print 'Select a lever'
            lever = interface.int_input()
            #open/close gates depending on lever
            display.print_gates(self.gates)
