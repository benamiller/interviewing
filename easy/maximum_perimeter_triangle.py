def maximumPerimeterTriangle(sticks):
    biggest_perimeter = 0
    biggest_perimeter_lengths = [-1]

    for i in range(len(sticks) - 2):
        for j in range(i + 1, len(sticks) - 1):
            for k in range(j + 1, len(sticks)):
                triplet = [sticks[i], sticks[j], sticks[k]]

                longest_side_length = max(triplet)
                perimeter = sum(triplet)

                if perimeter - longest_side_length <= longest_side_length:
                    continue

                if perimeter > biggest_perimeter:
                    biggest_perimeter = perimeter
                    biggest_perimeter_lengths = triplet

                if perimeter == biggest_perimeter:
                    if max(triplet) > max(biggest_perimeter_lengths):
                        biggest_perimeter_lengths = triplet
                    if min(triplet) > min(biggest_perimeter_lengths):
                        biggest_perimeter_lengths = triplet

    return sorted(biggest_perimeter_lengths)


if __name__ == "__main__":
    sticks = list(map(int, input().strip().split()))

    print(maximumPerimeterTriangle(sticks))
