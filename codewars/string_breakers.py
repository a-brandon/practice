def string_breakers(n, st):
    s = st.replace(' ', '')
    chunks = [s[i: i + n] for i in range(0, len(s), n)]
    return '\n'.join(chunks)