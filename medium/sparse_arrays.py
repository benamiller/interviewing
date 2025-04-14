def matchingStrings(stringList, queries):
    results = [0 for i in range(len(queries))]

    string_frequencies = {}
    for curr_string in stringList:
        if curr_string in string_frequencies:
            string_frequencies[curr_string] += 1
        else:
            string_frequencies[curr_string] = 1

    for i, query in enumerate(queries):
        if query in string_frequencies:
            results[i] = string_frequencies[query]

    return results


if __name__ == "__main__":
    stringList = list(input().strip().split(" "))
    queries = list(input().strip().split(" "))

    print(matchingStrings(stringList, queries))
