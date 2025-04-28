

if __name__ == "__main__":
    n = int(input())
    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    print(dynamicArray(n, queries))
