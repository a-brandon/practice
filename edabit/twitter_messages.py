def pad(message):
    msg_length = len(message)
    s = '{}{}' if msg_length % 2 else '{} {}'
    return s.format(message, 'lo' * (140 - msg_length))[:140]