def parse_file(file_path):
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
                antinode_x1, antinode_y1 = x2 + dx, y2 + dy
                if 0 <= antinode_x1 < num_lines and 0 <= antinode_y1 < num_columns:
                    antinodes.add((antinode_x1, antinode_y1))
                antinode_x2, antinode_y2 = x1 - dx, y1 - dy
                if 0 <= antinode_x2 < num_lines and 0 <= antinode_y2 < num_columns:
                    antinodes.add((antinode_x2, antinode_y2))
    
    return len(antinodes)

file_path = 'input.txt'
result = parse_file(file_path)
print(result)
