import heapq

def read_grid(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]

def find_points(grid):
    start = None
    end = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end

def is_valid(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#'

def find_all_paths(grid, start, end):
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(start, [], 'E')]
    all_paths = []
    while stack:
        (x, y), path, direction = stack.pop()
        if (x, y) == end:
            all_paths.append((path + [(x, y)], direction))
            continue
        for idx, (dx, dy) in enumerate(DIRECTIONS):
            next_x, next_y = x + dx, y + dy
            if is_valid(grid, next_x, next_y) and (next_x, next_y) not in path:
                new_direction = ['E', 'S', 'W', 'N'][idx]
                stack.append(((next_x, next_y), path + [(x, y)], new_direction))
    return all_paths

def calculate_path_cost(path_with_direction):
    path, initial_direction = path_with_direction
    DIRECTIONS = {'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'N': (0, -1)}
    cost = 0
    current_direction = initial_direction
    for i in range(1, len(path)):
        prev_x, prev_y = path[i - 1]
        curr_x, curr_y = path[i]
        dx, dy = curr_x - prev_x, curr_y - prev_y
        move_direction = [k for k, v in DIRECTIONS.items() if v == (dx, dy)][0]
        if move_direction != current_direction:
            cost += 1000
            current_direction = move_direction
        cost += 1
    return cost

def visualize_combined_map(grid, paths):
    grid_copy = [row[:] for row in grid]
    for path in paths:
        for x, y in path:
            if grid_copy[y][x] in {'.', 'S', 'E'}:
                grid_copy[y][x] = 'O'
    total_tiles = sum(row.count('O') for row in grid_copy)
    return '\n'.join(''.join(row) for row in grid_copy), total_tiles

if __name__ == "__main__":
    filename = "input.txt"
    grid = read_grid(filename)
    start, end = find_points(grid)
    all_paths = find_all_paths(grid, start, end)
    path_costs = [(path_with_direction[0], calculate_path_cost(path_with_direction)) for path_with_direction in all_paths]
    path_costs.sort(key=lambda x: x[1])
    min_cost = path_costs[0][1]
    minimal_cost_paths = [path for path, cost in path_costs if cost == min_cost]
    print("Combined map with minimal cost paths:")
    combined_map, total_tiles = visualize_combined_map(grid, minimal_cost_paths)
    print(combined_map)
    print(f"Total tiles used: {total_tiles}")