import format

def print_level_intro(level_name):
    level_intro = format.to_txt(level_name)
    print_text_from(level_intro)

def print_text_from(file_name):
    text = open(file_name)
    print text.read()

def print_and_center(string):
    print '\t\t\t' + string

#GATES LEVEL
def print_gates(gate):
    print_and_center("[IIIIIIIIIIIII]")
    for i, val in enumerate(gate.positions):
        if val == -1:
            print_and_center(str(i+1) + ' [+++++++++] ' + str(i+1))
        else:
            print_and_center(str(i+1) + ' [         ] ' + str(i+1))
    print_and_center("[IIIIIIIIIIIII]\n")
