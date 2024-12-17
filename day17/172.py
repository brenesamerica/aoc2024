def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    reg_x_initial = int(lines[0].split(":")[1].strip())
    reg_y_initial = int(lines[1].split(":")[1].strip())
    reg_z_initial = int(lines[2].split(":")[1].strip())
    program_line = lines[4].split(":")[1].strip()
    instructions = list(map(int, program_line.split(",")))

    return reg_x_initial, reg_y_initial, reg_z_initial, instructions

def get_operand_value(operand, registers):
    if operand <= 3:
        return operand
    if operand <= 6:
        return registers[operand - 4]
    return None

def execute_instruction(registers, instructions, pointer, output_list):
    opcode = instructions[pointer]
    operand = instructions[pointer + 1]
    operand_value = get_operand_value(operand, registers)
    
    if opcode == 0:
        registers[0] = int(registers[0] / 2 ** operand_value)
    elif opcode == 1:
        registers[1] = registers[1] ^ operand
    elif opcode == 2:
        registers[1] = operand_value % 8
    elif opcode == 3 and registers[0] != 0:
        pointer = operand
        return registers, pointer, output_list
    elif opcode == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5:
        output_list.append(operand_value % 8)
    elif opcode == 6:
        registers[1] = int(registers[0] / 2 ** operand_value)
    elif opcode == 7:
        registers[2] = int(registers[0] / 2 ** operand_value)
    
    pointer += 2
    return registers, pointer, output_list

def run_program(registers, instructions):
    instruction_pointer = 0
    output_list = []
    while instruction_pointer < len(instructions):
        registers, instruction_pointer, output_list = execute_instruction(registers, instructions, instruction_pointer, output_list)
    return output_list

def reverse_engineer_x(file_path):
    reg_x_initial, reg_y_initial, reg_z_initial, instructions = read_input(file_path)
    registers = [reg_x_initial, reg_y_initial, reg_z_initial]
    valid_states = {0: [val for val in range(8)]}
    
    for step in range(1, len(instructions)):
        valid_states[step] = []
        for state in valid_states[step - 1]:
            for candidate in range(8):
                reg_x = 8 * state + candidate
                test_registers = [reg_x, registers[1], registers[2]]
                output = run_program(test_registers, instructions)
                output_length = len(output)
                if output == instructions[-output_length:]:
                    valid_states[step].append(reg_x)
                if output == instructions:
                    return reg_x

def main():
    input_file_path = "input.txt"
    print(reverse_engineer_x(input_file_path))

if __name__ == "__main__":
    main()
