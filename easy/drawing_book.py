def pageCount(n, p):
    n = n + 1 if n % 2 == 0 else n
    mid_point = n // 2

    # if greater than mid_point, start from end
    if p > mid_point:
        return (n - p) // 2

    else:
        p = p + 1 if p % 2 == 0 else p
        return (p - 1) // 2


if __name__ == "__main__":
    n = int(input().strip())
    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
