def parse_input(file_path):
    """Parses the input file and returns a list of robots with their positions and velocity."""
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            pos = tuple(map(int, parts[0].split('=')[1].split(',')))
            vel = tuple(map(int, parts[1].split('=')[1].split(',')))
            robots.append({'position': pos, 'velocity': vel})
    return robots

def move_robots(robots, max_columns, max_rows, max_steps):
    """Moves the robots continuously until a pyramid is formed or max steps reached, overwriting the output file."""
    step = 0
    while step < max_steps:
        for robot in robots:
            new_x = (robot['position'][0] + robot['velocity'][0]) % max_columns
            new_y = (robot['position'][1] + robot['velocity'][1]) % max_rows
            robot['position'] = (new_x, new_y)
        
        if print_robots(robots, 'robots_output.txt', step):
            return step
        step += 1

    # If no pyramid is found, return the max steps
    return max_steps

def print_robots(robots, output_file, step):
    """Overwrites the robots' positions into a text file and checks for a pyramid."""
    max_x = max(robot['position'][0] for robot in robots) + 1
    max_y = max(robot['position'][1] for robot in robots) + 1
    matrix = [['.' for _ in range(max_x)] for _ in range(max_y)]

    for robot in robots:
        x, y = robot['position']
        matrix[y][x] = '█'

    with open(output_file, 'w') as file:
        file.write(f"Step {step}: {len(robots)} robots\n")
        for row in matrix:
            file.write(''.join(row) + '\n')

    # Check every possible 4x4 section of the matrix for a pyramid
    for i in range(max_y - 3):
        for j in range(max_x - 3):
            sub_matrix = [row[j:j+4] for row in matrix[i:i+4]]
            if is_pyramid(sub_matrix):
                return True

    return False


def is_pyramid(matrix):
    """Checks if the given 4x4 matrix contains a 4-level high pyramid."""
    # Ensure matrix is 4x4
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        return False

    # Check rows for the pyramid pattern
    expected_patterns = [
        [0, 1, 2, 3],  # Bottom row (4 blocks)
        [1, 2],        # Second row (3 blocks)
        [1],           # Third row (2 blocks)
        [2]            # Top row (1 block)
    ]

    for row_index, expected_cols in enumerate(expected_patterns):
        row = matrix[3 - row_index]  # Bottom row is index 3
        for col in range(4):
            if col in expected_cols and row[col] != '█':
                return False
            if col not in expected_cols and row[col] == '█':
                return False

    return True



def main():
    input_file = 'input.txt'
    output_file = 'robots_output.txt'
    max_columns = 101
    max_rows = 103
    max_steps = 8290

    robots = parse_input(input_file)

    # Run until the first pyramid is found or max steps reached
    pyramid_step = move_robots(robots, max_columns, max_rows, max_steps)

    if pyramid_step < max_steps:
        print(f"The first step where a 4-level high pyramid is formed: {pyramid_step}")
    else:
        print("No 4-level high pyramid was formed within the given steps.")

    # Print final status
    print_robots(robots, output_file, pyramid_step)

if __name__ == "__main__":
    main()
