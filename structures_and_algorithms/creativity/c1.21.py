def reverse_input():
    """C-1.21

    Write a Python program that repeatedly reads lines from standard
    input until an EOFError is raised, and then outputs those lines
    in reverse order (a user can indicate end of input by typing CTRL - D)."""
    lines = []
    while True:
        try:
            inp = input('Enter a line: ')
            lines.append(inp)
        except EOFError:
            break

    for line in reversed(lines):
        print(line)
