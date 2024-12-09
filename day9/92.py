import numpy as np

with open("input.txt") as file:
    numbers = file.read().strip()

result = []
next_ind = 0

for index, char in enumerate(numbers):
    if index % 2 == 0:
        result.append((str(next_ind), char))
        next_ind += 1
    else:
        result.append((".", char))

restart = True
while restart:
    restart = False
    for i in range(len(result) - 1, -1, -1):
        m, v = result[i]
        if m.isdigit():
            v = int(v)
            for j in range(len(result)):
                m_top, x = result[j]
                if m_top == "." and i >= j:
                    x = int(x)
                    if x == v:
                        # Swap the elements
                        result[i], result[j] = result[j], result[i]
                        i=-1
                        restart = True  # Restart from the beginning
                        break
                    elif x > v:
                        remaining = x - v
                        if result[j + 1][0] != '.' and result[j - 1][0] != '.':
                            result[j] = (m, str(v))
                            result[i] = (".", str(v))
                            result.insert(j + 1, (".", str(remaining)))
                        elif result[j + 1][0] == '.':
                            result[j] = (m, str(v))
                            result[i] = (".", str(v))
                            result[j + 1] = (result[j + 1][0], str(int(result[j + 1][1]) + remaining))
                        elif result[j - 1][0] == '.':
                            result[j] = (m, str(v))
                            result[i] = (".", str(v))
                            result[j - 1] = (result[j - 1][0], str(int(result[j - 1][1]) + remaining))
                        i=-1
                        restart = True  # Restart from the beginning
                        break
            if restart:
                break

output = ""
for m, v in result:
    if m == ".":
        output += "." * int(v)
    else:
        output += m * int(v)

weighted_sum = np.int64(0)
for index, char in enumerate(output):
    if char.isdigit():
        weighted_sum += np.int64(int(char) * index)

weighted_sum = np.int64(weighted_sum)
print(f"Weighted sum: {weighted_sum}")
