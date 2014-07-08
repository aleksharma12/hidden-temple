import display

class Gates(object):

    def __init__(self):
        #CLOSED = 0, OPEN = 1
        self.gates = [0,0,0,0,0]

    def play(self):
        display.print_gates(self.gates)
        #while game unfinished
            #display gates graphic
            #ask user to pick a lever
            #display gates graphic
