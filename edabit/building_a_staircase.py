def build_staircase(height, block):
    return [list(block * (i + 1) + '_' * (height - (i + 1))) for i in range(height)]
