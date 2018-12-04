from collections import defaultdict

with open('input/day3', 'r') as f:
    claims = [line.split('@')[1].strip() for line in f]
    corners = [claim.split(':')[0] for claim in claims]
    dimensions = [claim.split(':')[1] for claim in claims]

    dimensions_tuples = [(int(dimension.split('x')[0]), int(dimension.split('x')[1])) for dimension in dimensions]
    corners_tuples = [(int(corner.split(',')[0]), int(corner.split(',')[1])) for corner in corners]

    claims_map = defaultdict(list)

    for i in range(len(corners_tuples)):
        for m in range(dimensions_tuples[i][0]):
            for n in range(dimensions_tuples[i][1]):
                x = corners_tuples[i][0] + m
                y = corners_tuples[i][1] + n
                claims_map[f'{x}x{y}'].append(i + 1)

    in_two_or_more = 0
    independent_ids = defaultdict(lambda: True)
    for k, v in claims_map.items():
        if len(v) >= 2:
            in_two_or_more += 1

        for each in v:
            if len(v) == 1:
                independent_ids[each] &= True
            else:
                independent_ids[each] &= False

    print(f'Part one: {in_two_or_more}')

    for k, v in independent_ids.items():
        if v:
            print(f'Part two: {k}')
