import time

start_time = time.time()
def read_file_to_matrix(filename):
    def run_simulation(matrix):
        """Runs the simulation on the given matrix and returns turning points."""
        curr_coor = None
        directions = [
            (-1, 0),  # up (^)
            (0, 1),   # right (>)
            (1, 0),   # down (v)
            (0, -1)   # left (<)
        ]
        start_dir = None
        turning_points = []
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

        while len(turning_points) == len(set(turning_points)):  
            next_coor = (curr_coor[0] + directions[direction][0], curr_coor[1] + directions[direction][1])
            if not (0 <= next_coor[0] < rows and 0 <= next_coor[1] < cols):
                break
            if matrix[next_coor[0]][next_coor[1]] != '#':
                curr_coor = next_coor
            else:
                direction = (direction + 1) % 4
                turning_points.append((curr_coor, direction))

        if len(turning_points) == len(set(turning_points)):
            return False  
        else:
            return True
    with open(filename, 'r') as file:
        original_matrix = [list(line.strip()) for line in file]

    rows, cols = len(original_matrix), len(original_matrix[0])
    loop_creating_replacements = 0

    for i in range(rows):
        for j in range(cols):
            if original_matrix[i][j] not in ['#', '<', '>', '^', 'v']:
                original_value = original_matrix[i][j]
                original_matrix[i][j] = '#'

                loop_detected = run_simulation(original_matrix)

                if loop_detected:
                    loop_creating_replacements += 1

                original_matrix[i][j] = original_value

    print(f"Loop-creating replacements: {loop_creating_replacements}")
    return loop_creating_replacements


try:
    loop_creating_replacements = read_file_to_matrix('input.txt')
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")
except ValueError as e:
    print(e)
