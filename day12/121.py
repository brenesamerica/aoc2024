def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file if line.strip()]
    return grid

def is_valid(grid, x, y, visited, plant_type):
    return (0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == plant_type)

def explore_region(grid, x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    perimeters = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    while stack:
        cx, cy = stack.pop()
        area += 1
        local_perimeter = 0        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(grid, nx, ny, visited, grid[cx][cy]):
                visited[nx][ny] = True
                stack.append((nx, ny))
            else:
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != grid[cx][cy]:
                    local_perimeter += 1        
        perimeters += local_perimeter    
    return area, perimeters

def calculate_total_cost(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    total_cost = 0    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                area, perimeter = explore_region(grid, i, j, visited)
                total_cost += area * perimeter    
    return total_cost

grid = read_grid_from_file('input.txt')
total_cost = calculate_total_cost(grid)
print(total_cost)
