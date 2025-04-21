import sys

for line in sys.stdin:
    separation = line[0]
    formatting = line[2]

    line = line[4:].strip()

    if separation == "C":
        words = line.split(" ")

        start = words.pop(0)

        if formatting == "C":
            start = start.capitalize()

        for word in words:
            start += word.capitalize()

        if formatting == "M":
            start += "()"

        print(start)

    if separation == "S":
        if line[-2:] == "()":
            line = line[:-2]

        words = []
        starting_index = 0

        for end_index in range(1, len(line)):
            if line[end_index].isupper():
                words.append(line[starting_index:end_index])
                starting_index = end_index
                end_index = starting_index + 1

        words = [word.lower() for word in words]

        final_word = line[starting_index: end_index + 1]

        words.append(final_word.lower())

        words_string = " ".join(words)
        print(words_string)
