import sys

def main():
    try:
        with open("input.txt", "r") as inputFile:
            list1 = []
            list2 = []
            for line in inputFile:
                num1, num2 = map(int, line.split())
                list1.append(num1)
                list2.append(num2)
    except FileNotFoundError:
        print("Unable to open file input.txt", file=sys.stderr)
        return 1

    list1.sort()
    list2.sort()
    totaldiff = sum(abs(a - b) for a, b in zip(list1, list2))
    print(totaldiff)
    return 0

if __name__ == "__main__":
    main()
