def marsExploration(s):
    difference = 0

    for i in range(0, len(s) - 2, 3):
        substring = s[i:i+3]

        if substring[0] != "S":
            difference += 1
        if substring[1] != "O":
            difference += 1
        if substring[2] != "S":
            difference += 1

    return difference


if __name__ == "__main__":
    s = input()

    print(marsExploration(s))
