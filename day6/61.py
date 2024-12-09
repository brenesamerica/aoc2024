def read_file_to_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        matrix = [list(line.strip()) for line in file]
    
    curr_coor = None
    directions = [
        (-1, 0),  # up (^)
        (0, 1),   # right (>)
        (1, 0),   # down (v)
        (0, -1)   # left (<)
    ]
    start_dir = None
    visited_positions = set()

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value in ['<', '>', '^', 'v']:
                curr_coor = (i, j)
                if value == '<':
                    start_dir = 3
                elif value == '>':
                    start_dir = 1
                elif value == '^':
                    start_dir = 0
                elif value == 'v':
                    start_dir = 2
                break
        if curr_coor:
            break
    if not curr_coor or start_dir is None:
        raise ValueError("No valid starting point or direction found in the file.")
    rows, cols = len(matrix), len(matrix[0])
    direction = start_dir
    visited_positions.add(curr_coor)
    turning_points=[]
    while True:
        next_coor = (curr_coor[0] + directions[direction][0], curr_coor[1] + directions[direction][1])
        if not (0 <= next_coor[0] < rows and 0 <= next_coor[1] < cols):
            break
        if matrix[next_coor[0]][next_coor[1]] != '#':
            curr_coor = next_coor
            visited_positions.add(curr_coor)
        else:
            direction = (direction + 1) % 4
            turning_points.append((curr_coor, direction))
    print(turning_points)
    return visited_positions

try:
    visited_positions = read_file_to_matrix('input.txt')
    print(f"Distinct positions visited: {len(visited_positions)}")
except ValueError as e:
    print(e)
