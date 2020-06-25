def get_vert(it):
    for col in zip(*it):
        c = set(col)
        if len(c) == 1:
            return 'X' if c == {'X'} else 'O'


def get_horizontal(it):
    for row in it:
        r = set(row)
        if len(r) == 1:
            return 'X' if r == {'X'} else 'O'


def get_diagnol(it):
    forward_diags = set([it[i][i] for i, _ in enumerate(it)])
    reverse_diags = set([it[::-1][i][i] for i, _ in enumerate(it)])
    if forward_diags == {'X'} or reverse_diags == {'X'}:
        return 'X'
    elif forward_diags == {'O'} or reverse_diags == {'O'}:
        return 'O'


def tic_tac_toe(board):
    return (get_vert(board) or get_horizontal(board) or
            get_diagnol(board) or 'Draw')