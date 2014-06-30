def text(game_name):
    filename = game_name + '.txt'
    text = open(filename)
    print text.read()
