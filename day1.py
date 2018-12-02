with open("input/day1", "r") as f:
    sum = 0

    for line in f:
        new_line = int(line.strip())
        sum += new_line

    print(sum)

