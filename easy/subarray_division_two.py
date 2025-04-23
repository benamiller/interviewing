def birthday(s, d, m):
    running_sum = 0
    number_of_ways = 0

    for i in range(m - 1):
        running_sum += s[i]

    for i in range(m - 1, len(s)):
        running_sum += s[i]
        if running_sum == d:
            number_of_ways += 1
        running_sum -= s[i - m + 1]

    return number_of_ways


def birthdayEdgeCase(s, d, m):
    running_sum = 0
    number_of_ways = 0

    for i in range(m):
        running_sum += s[i]

    if running_sum == d:
        number_of_ways += 1

    for i in range(m, len(s)):
        running_sum = running_sum - s[i - m] + s[i]
        if running_sum == d:
            number_of_ways += 1

    return number_of_ways


if __name__ == "__main__":
    s = list(map(int, input().rstrip().split()))

    d = int(input())
    m = int(input())

    non_edge_case_answer = birthday(s, d, m)
    edge_case_answer = birthdayEdgeCase(s, d, m)
    assert non_edge_case_answer == edge_case_answer

    print(non_edge_case_answer)
