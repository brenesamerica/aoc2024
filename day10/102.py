def read_matrix(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]

def is_valid(matrix, visited, x, y, current_value):
    return (
        0 <= x < len(matrix) and
        0 <= y < len(matrix[0]) and
        (x, y) not in visited and
        matrix[x][y] == current_value + 1
    )

def recursive_search(matrix, x, y, visited):
    if matrix[x][y] == 9:
        return 1
    
    visited.add((x, y))
    count = 0
    current_value = matrix[x][y]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(matrix, visited, nx, ny, current_value):
            count += recursive_search(matrix, nx, ny, visited)
    
    visited.remove((x, y))
    return count

def calculate_trailhead_scores(matrix):
    trailhead_scores = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visited = set()
                score = recursive_search(matrix, i, j, visited)
                trailhead_scores.append(score)
    
    total_score = sum(trailhead_scores)
    return total_score

def main(file_path):
    matrix = read_matrix(file_path)
    
    total_score = calculate_trailhead_scores(matrix)
    print(f"\nSum of the scores of all trailheads: {total_score}")
    return total_score

file_path = "input.txt"
result = main(file_path)
