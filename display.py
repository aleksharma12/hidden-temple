import format

def print_level_intro(level_name):
    level_intro = format.to_txt(level_name)
    print_text_from(level_intro)

def print_text_from(file_name):
    text = open(file_name)
    print text.read()

def print_and_center(string):
    print '\t\t\t' + string

def print_moves(num_moves):
    print_and_center("Moves Taken: " + str(num_moves) + "\n")

#GATES
def print_gates(gate_positions, num_moves):
    print_and_center("[IIIIIIIIIIIII]")
    for i, val in enumerate(gate_positions):
        if val == -1:
            print_and_center(str(i+1) + ' [+++++++++] ' + str(i+1))
        else:
            print_and_center(str(i+1) + ' [         ] ' + str(i+1))
    print_and_center("[IIIIIIIIIIIII]\n")
    print_moves(num_moves)

def print_gates_victory(num_moves):
    if num_moves < 10:
        print "Piece of sugary cake. You're a puzzle master, and this"
        print "temple is about to get blasted by your huge brain."
    elif num_moves < 25:
        print "Well, you haven't thought that hard since Admiral Snark"
        print "asked for your hand in marriage on your way over here."
    else:
        print "Sweat pours down your face. A brightly-colored vein"
        print "on your face throbs violently. That puzzle hurt."
    print "\n"

#MIRRORS
def print_maze(num_moves):
    print_and_center("   0  1  2  3  4 ")
    for i in xrange(10):
        print_and_center(str(i) + " [ ][ ][ ][ ][ ]")
    print "\n"
    print_moves(num_moves)
