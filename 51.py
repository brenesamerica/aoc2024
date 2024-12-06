def eval_print(file_path):
    rules = []
    updates = []
    is_rule_section = True

    # Read and parse the file
    with open(file_path, 'r') as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                is_rule_section = False
                continue
            if is_rule_section:
                x, y = map(int, stripped.split('|'))
                rules.append((x, y))
            else:
                updates.append(list(map(int, stripped.split(','))))

    def is_valid_update(update):
        page_index = {page: idx for idx, page in enumerate(update)}
        for x, y in rules:
            if x in page_index and y in page_index:
                if page_index[x] >= page_index[y]:
                    return False
        return True

    total = 0
    for update in updates:
        if is_valid_update(update):
            mid_index = len(update) // 2
            total += update[mid_index]

    print(total)


file_path = 'input.txt'
eval_print(file_path)
