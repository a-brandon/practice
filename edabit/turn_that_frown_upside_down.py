def make_happy(txt):
    sad_faces = [':(', '8(', 'x(', ';(']
    for face in sad_faces:
        if face in txt:
            txt = txt.replace(face, face[0] + ')')
    return txt
