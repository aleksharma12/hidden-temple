import format

def text(name):
    text = open(format.to_txt(name))
    print text.read()
