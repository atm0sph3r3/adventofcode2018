import time

with open('input/day4', 'r') as f:
    lines = [line.strip() for line in f]
    lines_sorted = sorted(lines, key=lambda line: line[1:17])
    print(lines_sorted)
    for line in lines_sorted:
        if line.find('Guard') != -1:
            current_guard = line[26:line.index(' begins')]
            print(current_guard)

