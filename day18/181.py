import heapq

def read_obstacles(filename, max_lines=1024):
    obstacles = set()
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i >= max_lines:
                break
            y, x = map(int, line.strip().split(','))
            print(x, y)
            obstacles.add((x, y))
    return obstacles

def create_map(size, obstacles):
    matrix = [['.' for _ in range(size)] for _ in range(size)]
    for x, y in obstacles:
        matrix[x][y] = '#'
    return matrix

def print_map(matrix):
    for row in matrix:
        print(''.join(row))

def is_valid(x, y, size, obstacles, visited):
    return 0 <= x < size and 0 <= y < size and (x, y) not in obstacles and (x, y) not in visited

def find_shortest_path(size, obstacles):
    start = (0, 0)
    goal = (size - 1, size - 1)
    if start in obstacles or goal in obstacles:
        return None
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    visited = set()
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        visited.add(current)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if not is_valid(neighbor[0], neighbor[1], size, obstacles, visited):
                continue
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append((0, 0))
    return path[::-1]

if __name__ == "__main__":
    size = 71
    obstacles = read_obstacles('input.txt', max_lines=1024)
    matrix = create_map(size, obstacles)
    print("Initial Map:")
    print_map(matrix)
    path = find_shortest_path(size, obstacles)
    if path:
        print("\nShortest Path:")
        for step in path:
            print(step)
        print(f"\nLength of the shortest path: {len(path)-1} steps")
        for x, y in path:
            if (x, y) != (0, 0) and (x, y) != (size - 1, size - 1):
                matrix[x][y] = 'O'
        matrix[0][0]='O'
        matrix[size-1][size-1]='O'
        print("\nMap with Path:")
        print_map(matrix)
    else:
        print("No path found from (0, 0) to (70, 70)")
