with open("input.txt", "r") as file:
    numbers = file.read().strip()

result = []
next_ind = 0

for index, char in enumerate(numbers):
    count = int(char)
    
    if index % 2 == 0:
        result.extend(str(next_ind) for _ in range(count))
        next_ind += 1
    else:
        result.extend("." for _ in range(count))

left = 0
right = len(result) - 1

while left < right:
    if result[left] == ".":
        while result[right] == "." and right > left:
            right -= 1
        if left < right:
            result[left], result[right] = result[right], result[left]
    left += 1

weighted_sum = 0
for index, value in enumerate(result):
    if value.isdigit():
        weighted_sum += int(value) * index

print(f"Weighted Sum: {weighted_sum}")
