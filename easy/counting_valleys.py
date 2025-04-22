def countingValleys(path):
    altitude = 0
    valleys = 0

    for step in path:
        if step == "D":
            altitude -= 1
        if step == "U":
            altitude += 1
            if altitude == 0:
                valleys += 1

    return valleys


if __name__ == "__main__":
    path = input().strip()

    print(countingValleys(path))
