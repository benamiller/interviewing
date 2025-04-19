def divisibleSumPairs(arr, k):
    n = len(arr)

    num_pairs = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            i_value = arr[i]
            j_value = arr[j]
            if (i_value + j_value) % k == 0:
                num_pairs += 1

    return num_pairs


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))

    k = int(input())

    print(divisibleSumPairs(arr, k))
