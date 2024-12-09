from collections import defaultdict, deque

def eval_print2(file_path):
    rules = []
    updates = []
    is_rule_section = True

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

    def reorder_update(update):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        pages_in_update = set(update)

        for x, y in rules:
            if x in pages_in_update and y in pages_in_update:
                graph[x].append(y)
                in_degree[y] += 1
                in_degree.setdefault(x, 0)

        queue = deque([page for page in pages_in_update if in_degree[page] == 0])
        sorted_pages = []

        while queue:
            current = queue.popleft()
            sorted_pages.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_pages

    total = 0
    reordered_updates = []
    for update in updates:
        if not is_valid_update(update):
            reordered = reorder_update(update)
            reordered_updates.append(reordered)
            mid_index = len(reordered) // 2
            total += reordered[mid_index]

    print(total)

file_path = 'input.txt'
eval_print2(file_path)
