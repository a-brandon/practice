with open('text_file.txt') as file:
    modules = [(int(line.strip()) // 3) - 2 for line in file]
    total = sum(modules)
