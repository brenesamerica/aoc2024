from collections import Counter

def can_make_design(patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
    return dp[-1]

def count_possible_designs(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')
    patterns = lines[0].split(', ')
    designs = lines[2:]
    possible_design_count = sum(1 for design in designs if can_make_design(patterns, design))
    return possible_design_count

if __name__ == "__main__":
    input_file = "input.txt"
    result = count_possible_designs(input_file)
    print(f"Number of possible designs: {result}")
