def killer(suspect_info, dead):
    for k, v in suspect_info.items():
        if all(n in v for n in dead):
            return k