with open('input/day5', 'r') as f:
    counts = dict()
    output_chars = list()
    original_input = [char for char in f.readline()]

    for i in range(26):
        starting_char = chr(ord("a") + i)
        input_chars = [char for char in original_input if char.lower() != starting_char]
        length_change = len(input_chars)

        while length_change != 0:
            i = 0
            output_chars = list()

            while i < len(input_chars):
                if i == len(input_chars) - 1:
                    output_chars.append(input_chars[i])
                    break
                elif input_chars[i].lower() == input_chars[i + 1].lower() and \
                        ((input_chars[i].isupper() and input_chars[i + 1].islower()) or
                         (input_chars[i].islower() and input_chars[i + 1].isupper())):
                    i += 2
                else:
                    output_chars.append(input_chars[i])
                    i += 1

            length_change = len(input_chars) - len(output_chars)
            input_chars = output_chars

        counts[starting_char] = len(output_chars)

    min_value = None
    optimized_unit = None
    for k, v in counts.items():
        if min_value is None or v < min_value:
            min_value = v
            optimized_unit = k

    print(f'{optimized_unit}: {min_value}')
