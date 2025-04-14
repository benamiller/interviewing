def rotateLeft(d, arr):
    num_elements = len(arr)

    rotated_array = [None for i in range(num_elements)]

    d = d % num_elements

    slot_index = 0

    for i in range(d, num_elements):
        rotated_array[slot_index] = arr[i]
        slot_index += 1

    for i in range(0, d):
        rotated_array[slot_index] = arr[i]
        slot_index += 1

    return rotated_array


if __name__ == "__main__":
    d = int(input().strip())
    arr = list(map(int, input().strip().split(" ")))
    print(rotateLeft(d, arr))
