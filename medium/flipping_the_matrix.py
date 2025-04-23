def flippingMatrix(matrix):
    max_quadrant_sum = 0

    row_end = len(matrix) - 1
    col_end = len(matrix) - 1

    for row in range(len(matrix) // 2):
        col_end = len(matrix) - 1
        for col in range(len(matrix[0]) // 2):
            max_value_for_pos = max(
                    matrix[row][col],
                    matrix[row][col_end],
                    matrix[row_end][col],
                    matrix[row_end][col_end])
            max_quadrant_sum += max_value_for_pos
            col_end -= 1
        row_end -= 1

    return max_quadrant_sum


if __name__ == "__main__":
    n = int(input().strip())

    matrix = []

    for _ in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))

    print(flippingMatrix(matrix))
