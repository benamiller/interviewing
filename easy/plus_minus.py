def plusMinus(arr):
    num_positive = 0
    num_negative = 0
    num_zero = 0

    for num in arr:
        if num > 0:
            num_positive += 1
        elif num < 0:
            num_negative += 1
        else:
            num_zero += 1

    total_numbers = len(arr)
    positive_ratio = num_positive / total_numbers
    negative_ratio = num_negative / total_numbers
    zero_ratio = num_zero / total_numbers
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
