

if __name__ == "__main__":
    k = int(input().rstrip())

    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    print(twoArrays(k, A, B))
