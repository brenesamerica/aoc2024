def parse_input(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            pos = tuple(map(int, parts[0].split('=')[1].split(',')))
            vel = tuple(map(int, parts[1].split('=')[1].split(',')))
            robots.append({'position': pos, 'velocity': vel})
    return robots

def move_robots(robots, max_columns, max_rows):
    step = 1
    while True:
        for robot in robots:
            new_x = (robot['position'][0] + robot['velocity'][0]) % max_columns
            new_y = (robot['position'][1] + robot['velocity'][1]) % max_rows
            robot['position'] = (new_x, new_y)
        if check_for_pyramid(robots, max_columns, max_rows):
            return step
        step += 1

def check_for_pyramid(robots, max_columns, max_rows):
    robot_positions = set((robot['position'][0], robot['position'][1]) for robot in robots)
    for x in range(max_columns - 6):
        for y in range(max_rows - 6):
            if (
                all((x + i, y + 6) in robot_positions for i in range(7)) and
                all((x + i + 1, y + 5) in robot_positions for i in range(5)) and
                all((x + i + 2, y + 4) in robot_positions for i in range(3)) and
                (x + 3, y + 3) in robot_positions
            ):
                return True
    return False

def main():
    input_file = 'input.txt'
    max_columns = 101
    max_rows = 103
<<<<<<< HEAD
    max_steps = 10000

=======
>>>>>>> a8bbdf3 (14.2 corrected)
    robots = parse_input(input_file)
    pyramid_step = move_robots(robots, max_columns, max_rows)
    print(f"The first step where a 4-level high pyramid is formed: {pyramid_step}")

if __name__ == "__main__":
    main()
