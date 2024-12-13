from math import gcd

def parse_input(filename):
    machine_data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line_index in range(0, len(lines), 4):
            if lines[line_index].strip():
                button_a_deltas = list(map(lambda value: int(value[2:]), lines[line_index].strip().split(': ')[1].split(', ')))
                button_b_deltas = list(map(lambda value: int(value[2:]), lines[line_index + 1].strip().split(': ')[1].split(', ')))
                prize_coordinates = list(map(lambda value: int(value[2:]), lines[line_index + 2].strip().split(': ')[1].split(', ')))
                machine_data.append((button_a_deltas, button_b_deltas, prize_coordinates))
    return machine_data

def calculate_min_tokens(machine_data):
    total_token_count = 0
    for machine_index, (button_a_deltas, button_b_deltas, prize_coordinates) in enumerate(machine_data):
        button_a_x, button_a_y = button_a_deltas
        button_b_x, button_b_y = button_b_deltas
        prize_x, prize_y = prize_coordinates
        determinant = button_a_x * button_b_y - button_a_y * button_b_x
        if determinant == 0:
            continue
        delta_x = prize_x * button_b_y - prize_y * button_b_x
        delta_y = prize_y * button_a_x - prize_x * button_a_y
        if delta_x % determinant != 0 or delta_y % determinant != 0:
            continue
        button_a_press_count = delta_x // determinant
        button_b_press_count = delta_y // determinant
        if button_a_press_count < 0 or button_b_press_count < 0:
            continue
        token_count = button_a_press_count * 3 + button_b_press_count * 1
        total_token_count += token_count
    return total_token_count

def main():
    input_filename = "input.txt"
    machine_data = parse_input(input_filename)
    result = calculate_min_tokens(machine_data)
    print(f"Minimum tokens required: {result}")

if __name__ == "__main__":
    main()
