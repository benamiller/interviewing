def lonelyInteger(arr):
    value_frequencies = {}

    for value in arr:
        value_frequencies[value] = value_frequencies.get(value, 0) + 1

    for key, value in value_frequencies.items():
        if value == 1:
            return key

    return


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))

    print(lonelyInteger(arr))
