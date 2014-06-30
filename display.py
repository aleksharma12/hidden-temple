def intro(game_name):
    filename = game_name + '.txt'
    intro = open(filename)
    print intro.read()
