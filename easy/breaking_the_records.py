def breakingRecords(scores):
    if len(scores) < 2:
        return [0, 0]

    max_score = scores[0]
    min_score = scores[0]

    min_score_breaks = 0
    max_score_breaks = 0

    for score in scores:
        if score < min_score:
            min_score_breaks += 1
            min_score = score
        if score < max_score:
            max_score_breaks += 1
            max_score = score

    return [max_score_breaks, min_score_breaks]


if __name__ == "__main__":
    scores = input().strip().split(" ")
    print(breakingRecords(scores))
