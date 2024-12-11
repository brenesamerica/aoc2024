def simulate_stones(initial_stones, blinks):
    current_stones = initial_stones[:]

    for _ in range(blinks):
        next_stones = []
        for stone in current_stones:
            if stone == 0:
                next_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                num_str = str(stone)
                mid = len(num_str) // 2
                left = int(num_str[:mid])
                right = int(num_str[mid:])
                next_stones.append(left)
                next_stones.append(right)
            else:
                next_stones.append(stone * 2024)
        current_stones = next_stones
    return len(current_stones)

with open('input.txt', 'r') as file:
    lines = file.readlines()
    initial_stones = list(map(int, lines[0].split()))
blinks = 25
result = simulate_stones(initial_stones, blinks)
print(result)
