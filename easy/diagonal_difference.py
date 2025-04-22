def diagonalDifference(arr):
    top_left_to_bot_right = 0
    top_right_to_bot_left = 0

    top_left_col = 0
    top_right_col = len(arr[0]) - 1

    for row in range(0, len(arr)):
        top_left_to_bot_right += arr[row][top_left_col]
        top_right_to_bot_left += arr[row][top_right_col]
        top_left_col += 1
        top_right_col -= 1

    return abs(top_left_to_bot_right - top_right_to_bot_left)


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(diagonalDifference(arr))
