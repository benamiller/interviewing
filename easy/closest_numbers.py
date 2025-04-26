def closestNumbers(arr):
    result = []

    arr = sorted(arr)
    min_difference = float('inf')

    for i in range(0, len(arr) - 1):
        first = arr[i]
        second = arr[i + 1]
        difference = abs(first - second)

        if difference < min_difference:
            min_difference = difference

    for i in range(0, len(arr) - 1):
        first = arr[i]
        second = arr[i + 1]
        difference = abs(first - second)

        if difference == min_difference:
            result.append(first)
            result.append(second)

    return result


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    print(closestNumbers(arr))
