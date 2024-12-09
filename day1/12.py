import sys

def main():
    safe = 0
    try:
        with open("input2.txt", "r") as inputFile:
            list1 = []
            list2 = []            
            for line in inputFile:
                numbers = list(map(int, line.split()))
                if len(numbers) == 6:
                    if all(numbers[i] < numbers[i + 1] for i in range(5)) or all(numbers[i] > numbers[i + 1] for i in range(5)):
                        if all(abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(5)):
                            safe += 1

    except FileNotFoundError:
        print("Unable to open file input.txt", file=sys.stderr)
        return 1
    print(safe)
    return 0

if __name__ == "__main__":
    main()
