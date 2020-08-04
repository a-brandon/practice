def rearrange(sentence):
    nums = []

    for w in sentence.split():
        chars = sorted(w)
        w = w.replace(chars[0], '')
        nums.append((w, chars[0]))

    return ' '.join(w[0] for w in sorted(nums, key=lambda t: t[1]))