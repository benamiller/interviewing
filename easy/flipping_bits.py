def flippingBits(n):
    all_ones = 2**32-1
    return n ^ all_ones


if __name__ == "__main__":
    n = int(input().strip())

    print(flippingBits(n))
