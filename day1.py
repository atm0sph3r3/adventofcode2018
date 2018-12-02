with open("input/day1", "r") as f:
    frequency_changes = [int(line.strip()) for line in f]
    all_frequencies = set()
    current_frequency = 0
    repeated_frequency = None

    while repeated_frequency is None:
        for frequency in frequency_changes:
            current_frequency += frequency

            if current_frequency in all_frequencies:
                repeated_frequency = current_frequency
                break
            else:
                all_frequencies.add(current_frequency)

    print(repeated_frequency)