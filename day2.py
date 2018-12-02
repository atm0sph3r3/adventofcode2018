with open('input/day2', 'r') as f:
    ids = [line.strip() for line in f]

    for each_id in ids:
        for each_checked_id in ids:
            number_differed_by = 0
            differing_position = 0

            for i in range(len(each_id)):
                if each_id[i] != each_checked_id[i]:
                    number_differed_by += 1
                    differing_position = i

                if number_differed_by > 1:
                    break

            if number_differed_by == 1:
                if differing_position == len(each_id) - 1:
                    print(f'{each_id[:differing_position]}')
                else:
                    print(f'{each_id[:differing_position]}{each_id[differing_position + 1:]}')
