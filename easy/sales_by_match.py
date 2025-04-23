def sockMerchant(ar):
    sock_frequencies = {}
    num_pairs = 0

    for sock in ar:
        sock_frequencies[sock] = sock_frequencies.get(sock, 0) + 1

    for sock, frequency in sock_frequencies.items():
        if frequency >= 2:
            num_pairs += frequency // 2

    return num_pairs


if __name__ == "__main__":
    ar = list(map(int, input().rstrip().split()))

    print(sockMerchant(ar))
