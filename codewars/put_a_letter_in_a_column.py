def build_row_text(index, character):
    cols = ['|' for i in range(9)]
    cols[index] = f'|{character}|'
    return ' '.join(cols)