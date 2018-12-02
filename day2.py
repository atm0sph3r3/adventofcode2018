from collections import defaultdict

with open('input/day2', 'r') as f:
    ids = [line.strip() for line in f]

    three_letters = 0
    two_letters = 0

    for each_id in ids:
        lookup = defaultdict(int)
        for char in each_id:
            lookup[char] += 1

        found_two = False
        found_three = False
        for k, v in lookup.items():
            if v == 2 and not found_two:
                two_letters += 1
                found_two = True
            if v == 3 and not found_three:
                three_letters += 1
                found_three = True

    print(three_letters * two_letters)