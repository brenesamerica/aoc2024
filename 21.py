def is_safe(report):
    # Convert the report (string) to a list of integers
    levels = list(map(int, report.split()))
    
    # Check if all differences are between 1 and 3
    differences = [abs(levels[i + 1] - levels[i]) for i in range(len(levels) - 1)]
    if all(1 <= diff <= 3 for diff in differences)>1:
        return False
    
    # Check if levels are strictly increasing or decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    return increasing or decreasing


def count_safe_reports(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if is_safe(line.strip()):
                safe_count += 1
    return safe_count


# File containing the input data
filename = 'input2.txt'

# Count and print the number of safe reports
safe_reports = count_safe_reports(filename)
print(f"Number of safe reports: {safe_reports}")
