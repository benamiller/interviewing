def getRemovableRange(str1, starting_index):
    removable_indices = [starting_index]
    character = str1[starting_index]

    for i in range(starting_index - 1, - 1, - 1):
        if str1[i] == character:
            removable_indices.append(i)
        else:
            break

    for i in range(starting_index + 1, len(str1)):
        if str1[i] == character:
            removable_indices.append(i)
        else:
            break

    return removable_indices


def getRemovableIndices(str1, str2):
    str1_index = 0
    str2_index = 0

    removable_indices = []

    mismatches_removed = 0

    while str1_index < len(str1) and str2_index < len(str2):

        str1_character = str1[str1_index]
        str2_character = str2[str2_index]

        if str1_character == str2_character:
            str1_index += 1
            str2_index += 1

        # Found a character to remove
        else:
            mismatches_removed += 1
            if mismatches_removed > 1:
                return [-1]
            removable_indices = getRemovableRange(str1, str1_index)
            str1_index += 1

    # Last character must be removed, but guaranteed success
    if mismatches_removed == 0:
        removable_indices = getRemovableRange(str1, len(str1) - 1)

    return removable_indices


if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    print(getRemovableIndices(str1, str2))
