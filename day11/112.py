from functools import lru_cache

def simulate_stones_single(stone, blinks):
    @lru_cache(maxsize=None)
    def helper(stone, remaining_blinks):
        if remaining_blinks == 0:
            return 1
        if stone == 0:
            return helper(1, remaining_blinks - 1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])
            return helper(left, remaining_blinks - 1) + helper(right, remaining_blinks - 1)
        else:
            return helper(stone * 2024, remaining_blinks - 1)

    return helper(stone, blinks)

blinks = 75
precomputed_zero_result = simulate_stones_single(0, blinks)

with open('input.txt', 'r') as file:
    lines = file.readlines()
    initial_stones = list(map(int, lines[0].split()))

result = 0
for stone in initial_stones:
    result += simulate_stones_single(stone, blinks)

print(result)
