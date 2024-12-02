def is_safe(report):
    levels = list(map(int, report.split()))
    differences = [abs(levels[i + 1] - levels[i]) for i in range(len(levels) - 1)]
    if not all(1 <= diff <= 3 for diff in differences):
        return False
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    levels = list(map(int, report.split()))
    if is_safe(report):
        return True
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i+1:]
        if is_safe(" ".join(map(str, modified_report))):
            return True
    
    return False

def count_safe_reports_with_dampener(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if is_safe_with_dampener(line.strip()):
                safe_count += 1
    return safe_count

filename = 'input2.txt'
safe_reports_with_dampener = count_safe_reports_with_dampener(filename)
print(f"Number of safe reports with Problem Dampener: {safe_reports_with_dampener}")
