def parse_input(file_path):
    robots = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            pos = tuple(map(int, parts[0].split('=')[1].split(',')))
            vel = tuple(map(int, parts[1].split('=')[1].split(',')))
            robots.append({'position': pos, 'velocity': vel})
    return robots

def move_robots(robots, steps, max_columns, max_rows):
    for _ in range(steps):
        for robot in robots:
            new_x = (robot['position'][0] + robot['velocity'][0]) % max_columns
            new_y = (robot['position'][1] + robot['velocity'][1]) % max_rows
            robot['position'] = (new_x, new_y)
    return robots

def count_robots_in_quadrants(robots, max_columns, max_rows):
    mid_x = max_columns // 2
    mid_y = max_rows // 2
    quadrants = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}
    for robot in robots:
        x, y = robot['position']
        if 0 <= x < mid_x and 0 <= y < mid_y:
            quadrants['Q1'] += 1
        elif mid_x < x < max_columns and 0 <= y < mid_y:
            quadrants['Q2'] += 1
        elif 0 <= x < mid_x and mid_y < y < max_rows:
            quadrants['Q3'] += 1
        elif mid_x < x < max_columns and mid_y < y < max_rows:
            quadrants['Q4'] += 1
    return quadrants

def main():
    input_file = 'input.txt'
    max_columns = 101
    max_rows = 103
    steps = 100
    robots = parse_input(input_file)
    robots = move_robots(robots, steps, max_columns, max_rows)
    quadrants = count_robots_in_quadrants(robots, max_columns, max_rows)
    result = 1
    for quadrant, count in quadrants.items():
        result = result * quadrants[quadrant]
    print(result)
    
if __name__ == "__main__":
    main()
