from itertools import product

def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])  
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        next_number = int(tokens[i + 1])
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
    return result

def generate_combinations(label, input_line):
    elements = input_line.split()
    operators = ['+', '*']
    positions = len(elements) - 1
    operator_combinations = product(operators, repeat=positions)    
   # print(f"\nProcessing label: {label}, elements: {elements}")
    for ops in operator_combinations:
        combination = []
        for i, element in enumerate(elements):
            combination.append(element)
            if i < len(ops):
                combination.append(ops[i])
        expression = " ".join(combination)
        result = evaluate_left_to_right(expression)
        #print(f"Trying combination: {expression} = {result}")
        if result == label:
            #print(f"Match found: {expression} = {label}")
            return label
    #print(f"No match found for label: {label}")
    return 0

def calculate_total(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            label, numbers = line.split(':', 1)
            label = int(label.strip())
            numbers = numbers.strip()
            #print(f"\nReading line: {line}")
            value = generate_combinations(label, numbers)
            #print(f"Value for label {label}: {value}")
            total += value
    #print(f"\nFinal total calibration result: {total}")
    return total

filename = "input.txt"
result = calculate_total(filename)
print(result)
