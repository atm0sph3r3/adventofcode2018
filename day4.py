from collections import defaultdict
from collections import Counter

with open('input/day4', 'r') as f:
    lines = [line.strip() for line in f]
    lines_sorted = sorted(lines, key=lambda line: line[1:17])
    guard_minutes = defaultdict(list)

    for line in lines_sorted:
        if line.find('Guard') != -1:
            current_guard = line[26:line.index(' begins')]
        elif line.find('falls asleep') != -1:
            is_sleeping = True
            falls_asleep_minute = int(line[15:17])
            guard_minutes[current_guard].append(falls_asleep_minute)
        elif line.find('wakes up') != -1:
            is_sleeping = False
            wake_up_minute = int(line[15:17])
            delta_wake_sleep = wake_up_minute - falls_asleep_minute
            for i in range(delta_wake_sleep):
                guard_minutes[current_guard].append(falls_asleep_minute + i)

    # part 1
    max_minutes = None
    max_guard = None
    guard_minutes_counted = dict()
    for k, v in guard_minutes.items():
        if max_minutes is None or len(v) > max_minutes:
            max_minutes = len(v)
            max_guard = k
        guard_minutes_counted[k] = Counter(v)

    print(int(max_guard) * guard_minutes_counted[max_guard].most_common(1)[0][0])

    # part 2
    max_guard = None
    max_minute = None
    max_count = None
    for k, v in guard_minutes_counted.items():
        if max_minute is None or v.most_common(1)[0][0] > max_count:
            max_count = v.most_common(1)[0][1]
            max_minute = v.most_common(1)[0][0]
            max_guard = k

    print(int(max_guard) * max_minute)
