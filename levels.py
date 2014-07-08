import display

class Gates(object):

    def __init__(self):
        #CLOSED = 0, OPEN = 1
        self.gates = [0,0,0,0,0]

    def play(self):
        display.print_graphic(self._gates_graphic())
        #while game unfinished
            #display gates graphic
            #ask user to pick a lever
            #display gates graphic

    def _gates_graphic(self):
        graphic = [
        "[IIIIIIIIIIIII]",
        "1 [+++++++++] 1",
        "2 [+++++++++] 2",
        "3 [+++++++++] 3",
        "4 [+++++++++] 4",
        "5 [+++++++++] 5",
        "[IIIIIIIIIIIII]"
        ]
        # for gate in gates:
        #     if gate == 0:
        return graphic
