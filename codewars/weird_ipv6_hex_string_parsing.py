def parse_IPv6(iPv6):
    for ch in iPv6:
        if ch not in 'ABCDEF0123456789':
            iPv6 = iPv6.split(ch)
            break

    result = []

    for ip in iPv6:
        total = sum(int(f'0x{val}', 16) for val in ip)
        result.append(str(total))

    return ''.join(result)