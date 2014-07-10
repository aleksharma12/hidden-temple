from sys import exit

def press_enter_to_continue():
    print "(Press ENTER to continue)"
    raw_input()

def select_lever():
    print 'Select a number to choose a lever'
    try:
        i = int(raw_input('>> '))
        if i in range(1, 6):
            return i
        else:
            print "That isn't one of the levers!\n"
            return 0
    except KeyboardInterrupt:
        print "A trap door opens beneath your feet!"
        exit(1)
    except ValueError:
        print "That's not even a number.\n"
        return 0
