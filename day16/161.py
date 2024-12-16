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

def a_star(grid, start, end):
    DIRECTIONS = ['E', 'S', 'W', 'N']
    MOVE_COST = 1
    ROTATE_COST = 1000
    pq = []
    heapq.heappush(pq, (0, start, 'E'))
    visited = set()
    while pq:
        cost, (x, y), direction = heapq.heappop(pq)
        if (x, y) == end:
            return cost
        if ((x, y), direction) in visited:
            continue
        visited.add(((x, y), direction))
        dx, dy = 0, 0
        if direction == 'E':
            dx, dy = 1, 0
        elif direction == 'S':
            dx, dy = 0, 1
        elif direction == 'W':
            dx, dy = -1, 0
        elif direction == 'N':
            dx, dy = 0, -1
        next_x, next_y = x + dx, y + dy
        if is_valid(grid, next_x, next_y):
            heapq.heappush(pq, (cost + MOVE_COST, (next_x, next_y), direction))
        for rotation in [-1, 1]:
            new_direction = DIRECTIONS[(DIRECTIONS.index(direction) + rotation) % 4]
            heapq.heappush(pq, (cost + ROTATE_COST, (x, y), new_direction))
    return float('inf')

if __name__ == "__main__":
    filename = "input.txt"
    grid = read_grid(filename)
    start, end = find_points(grid)
    lowest_score = a_star(grid, start, end)
    print("Lowest score to reach the end:", lowest_score)
