from sys import exit

def press_enter_to_continue():
    print "(Press ENTER to continue)"
    raw_input()

def int_input_in_range(low, high):
    try:
        i = int(raw_input('>> '))
        if i in range(low, high):
            print "In range!"
            return i
        else:
            print "That isn't one of the levers!\n"
    except KeyboardInterrupt:
        print "SO LONG!"
        exit(1)
    except ValueError:
        print "That's not even a number, fool.\n"
