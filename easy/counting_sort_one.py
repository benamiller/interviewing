def countingSort(arr):
    counts = [0 for _ in range(100)]

    for num in arr:
        counts[num] += 1

    return counts


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    print(countingSort(arr))
