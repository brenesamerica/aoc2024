def run_program(initial_A, initial_B, initial_C, program):
    A = initial_A
    B = initial_B
    C = initial_C
    instruction_pointer = 0
    output = []

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            raise ValueError("Invalid combo operand")

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        if opcode == 0:
            A //= 2 ** get_combo_value(operand)
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = get_combo_value(operand) % 8
        elif opcode == 3:
            if A != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:
            B = A // (2 ** get_combo_value(operand))
        elif opcode == 7:
            C = A // (2 ** get_combo_value(operand))
        else:
            raise ValueError(f"Invalid opcode {opcode} at position {instruction_pointer}")

        instruction_pointer += 2

    return ",".join(map(str, output))

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    initial_A = int(lines[0].split(":")[1].strip())
    initial_B = int(lines[1].split(":")[1].strip())
    initial_C = int(lines[2].split(":")[1].strip())
    program_line = lines[4].split(":")[1].strip()
    program = list(map(int, program_line.split(",")))
    
    return initial_A, initial_B, initial_C, program

if __name__ == "__main__":
    input_file = "input.txt"
    initial_A, initial_B, initial_C, program = read_input(input_file)
    result = run_program(initial_A, initial_B, initial_C, program)
    print("Output:", result)
