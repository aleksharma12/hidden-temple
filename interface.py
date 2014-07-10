from sys import exit

#GENERAL
def press_enter_to_continue():
    print "(Press ENTER to continue)"
    raw_input()

def get_num_in_range(low, high, error_message):
    i = int(raw_input('>> '))
    if low <= i <= high:
        return i
    else:
        print error_message + '\n'
        return 0

#GATES
def select_lever():
    print 'Select a number to choose a lever'
    try:
        return get_num_in_range(1, 6, "That isn't one of the levers!")
    except KeyboardInterrupt:
        print "A trap door opens beneath your feet!"
        exit(1)
    except ValueError:
        print "That's not even a number.\n"
        return 0
