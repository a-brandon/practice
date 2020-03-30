def get_frame(w, h, ch):
    if w <= 2 or h <= 2:
        return 'invalid'
    frame = []
    for i in range(h):
        if i == 0 or i == h - 1:
            frame.append([ch * w])
        else:
            frame.append([ch + ' ' * (w - 2) + ch])
    return frame
