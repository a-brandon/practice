def binary_to_text(n):
    bytes_ = [n[i: i + 8][::-1] for i in range(0, len(n), 8)]
    output = []

    for b in bytes_:
        total = 0
        for i, bit in enumerate(b):
            if bit == '1':
                total += 2 ** i
        output.append(chr(total))

    return ''.join(output)