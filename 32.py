import re

def line_splitter(text, separator):
    return text.split(separator)


with open('input.txt', 'r') as file:
    text = file.read()

text = re.sub(r"don't\(\).*?do\(\)", "", text, flags=re.DOTALL)
print(text)
separator = "mul("
result = line_splitter(text, separator)
result = [record.split(')')[0] for record in result]

filtered_result = []
for record in result:
    if ',' in record:
        x, y = record.split(',')
        if x.isdigit() and y.isdigit() and 1 <= len(x) <= 3 and 1 <= len(y) <= 3:
            filtered_result.append((int(x), int(y)))

total_sum = sum(x * y for x, y in filtered_result)

print(total_sum)