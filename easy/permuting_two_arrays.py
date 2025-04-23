def twoArrays(k, A, B):
    a = sorted(A)
    b = sorted(B, reverse=True)

    for i in range(len(a)):
        if a[i] + b[i] < k:
            return "NO"

    return "YES"


if __name__ == "__main__":
    k = int(input().rstrip())

    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    print(twoArrays(k, A, B))
