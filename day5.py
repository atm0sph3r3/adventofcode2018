with open('input/day5', 'r') as f:
    input_chars = [char for char in f.readline()]
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


    print(len(output_chars))
