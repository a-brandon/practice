def censor_string(txt, lst, char):
    return ' '.join(char * len(w) if w in lst else w for w in txt.split())