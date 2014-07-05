import format

def print_level_intro(level_name):
    level_intro = format.to_txt(level_name)
    print_text(level_intro)

def print_text(file_name):
    text = open(file_name)
    print text.read()
