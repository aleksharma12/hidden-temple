import display

class Gates(object):

    def __init__(self):
        #CLOSED = 0, OPEN = 1
        self.gates = [0,0,0,0,0]

    def play(self):
        display.print_graphic(self._convert_to_graphic())
        #while game unfinished
            #display gates graphic
            #ask user to pick a lever
            #display gates graphic

    def _convert_to_graphic(self):
        graphic = ["[IIIIIIIIIIIII]"]
        # for gate in gates:
        #     if gate == 0:
        return graphic
