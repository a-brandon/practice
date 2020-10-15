def fix(paragraph):
    return '. '.join(map(str.capitalize, paragraph.split('. ')))