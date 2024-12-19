from collections import Counter

def count_ways_to_make_design(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[-1]

def total_arrangement_count(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')

    patterns = lines[0].split(', ')
    designs = lines[2:]

    total_count = sum(count_ways_to_make_design(patterns, design) for design in designs)

    return total_count

if __name__ == "__main__":
    input_file = "input.txt"
    result = total_arrangement_count(input_file)
    print(f"Total number of arrangements: {result}")
