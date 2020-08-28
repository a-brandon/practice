def mix_middle(txt):
    return ' '.join('{}{}{}'.format(w[0], w[1:-1][::-1], w[-1]) if len(w) > 1 else w for w in txt.split())