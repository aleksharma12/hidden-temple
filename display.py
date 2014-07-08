import format

def print_level_intro(level_name):
    level_intro = format.to_txt(level_name)
    print_text(level_intro)

def print_text(file_name):
    text = open(file_name)
    print text.read()

#GATES LEVEL
def print_gates(gate_positions):
    #extract these tabs into a new centering method
    print '\t\t\t' + "[IIIIIIIIIIIII]"
    for i, val in enumerate(gate_positions):
        if val == 0:
            print '\t\t\t' + str(i+1) + ' [+++++++++] ' + str(i+1)
        else:
            print '\t\t\t' + str(i+1) + ' [         ] ' + str(i+1)
    print '\t\t\t' + "[IIIIIIIIIIIII]"
