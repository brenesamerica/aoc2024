def parse_file_part_two(file_path):
    coordinates = []
    antinodes = set() 

    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_columns = len(lines[0].strip()) if lines else 0
        for x, line in enumerate(lines):
            for y, char in enumerate(line.strip()):
                if char != '.':
                    coordinates.append((char, x, y))

    for i, (char1, x1, y1) in enumerate(coordinates):
        for j, (char2, x2, y2) in enumerate(coordinates):
            if i != j and char1 == char2:
                dx = (x2 - x1)
                dy = (y2 - y1)
                nx, ny = x2 + dx, y2 + dy
                while 0 <= nx < num_lines and 0 <= ny < num_columns:
                    antinodes.add((nx, ny))
                    nx += dx
                    ny += dy
                nx, ny = x1 - dx, y1 - dy
                while 0 <= nx < num_lines and 0 <= ny < num_columns:
                    antinodes.add((nx, ny))
                    nx -= dx
                    ny -= dy
                antinodes.add((x1, y1))
                antinodes.add((x2, y2))

    return len(antinodes)

file_path = 'input.txt'
result = parse_file_part_two(file_path)
print(result)
