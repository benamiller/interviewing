def miniMaxSum(arr):
    sorted_arr = sorted(arr)

    minimum = sum(sorted_arr[:-1])
    maximum = sum(sorted_arr[1:])

    print(minimum, maximum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
