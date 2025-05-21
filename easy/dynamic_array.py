def dynamicArray(n, queries):
    arr = [[] for i in range(n)]

    last_answer = 0
    answers = []

    for query in queries:
        query_type = query[0]
        query_x = query[1]
        query_y = query[2]

        if query_type == 1:
            index = (query_x ^ last_answer) % n
            arr[index].append(query_y)

        if query_type == 2:
            index = (query_x ^ last_answer) % n
            last_answer = arr[index][query_y % len(arr[index])]
            answers.append(last_answer)

    return answers


if __name__ == "__main__":
    n = int(input())
    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    print(dynamicArray(n, queries))
