def count_xmas_pattern(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] == 'A':
                if (
                    (matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and
                     matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or
                    (matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and
                     matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M') or
                    (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and
                     matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or
                    (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and
                     matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M')
                ):
                    count += 1

    return count


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(line.strip()) for line in file]
    return matrix


if __name__ == "__main__":
    matrix = read_matrix_from_file('input.txt')
    result = count_xmas_pattern(matrix)
    print(result)
