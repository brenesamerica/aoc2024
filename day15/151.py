def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    map_section = []
    instructions = []
    instructions_start = False
    for line in lines:
        if line.strip() == "":
            instructions_start = True
            continue
        if instructions_start:
            instructions.append(line)
        else:
            map_section.append(list(line))
    return map_section, "".join(instructions)

def find_robot(map_section):
    for i, row in enumerate(map_section):
        if "@" in row:
            return i, row.index("@")
    return None

def calculate_gps_sum(map_section):
    gps_sum = 0
    for i, row in enumerate(map_section):
        for j, cell in enumerate(row):
            if cell == "O":
                gps_sum += 100 * i + j
    return gps_sum

def move_robot(map_section, instructions):
    directions = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
    robot_pos = find_robot(map_section)

    for move in instructions:
        if move not in directions:
            continue
        delta_row, delta_col = directions[move]
        new_row, new_col = robot_pos[0] + delta_row, robot_pos[1] + delta_col
        if map_section[new_row][new_col] == "#":
            continue
        if map_section[new_row][new_col] == "O":
            temp_row, temp_col = new_row, new_col
            while map_section[temp_row][temp_col] == "O":
                temp_row += delta_row
                temp_col += delta_col
            if map_section[temp_row][temp_col] == ".":
                while temp_row != new_row or temp_col != new_col:
                    temp_row -= delta_row
                    temp_col -= delta_col
                    map_section[temp_row + delta_row][temp_col + delta_col] = "O"
                map_section[new_row][new_col] = "@"
                map_section[robot_pos[0]][robot_pos[1]] = "."
                robot_pos = (new_row, new_col)
        elif map_section[new_row][new_col] == ".":
            map_section[new_row][new_col] = "@"
            map_section[robot_pos[0]][robot_pos[1]] = "."
            robot_pos = (new_row, new_col)
    return map_section

def print_map(map_section):
    for row in map_section:
        print("".join(row))

def main():
    input_file = "input.txt"
    map_section, instructions = read_input(input_file)
    print("Initial state:")
    print_map(map_section)
    map_section = move_robot(map_section, instructions)
    print("\nFinal state:")
    print_map(map_section)
    gps_sum = calculate_gps_sum(map_section)
    print(f"\nSum of all boxes' GPS coordinates: {gps_sum}")

if __name__ == "__main__":
    main()
