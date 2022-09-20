infile = "../input/input.txt"

def part_one():
    larger = 0

    with open(infile) as file:
        prev = float("inf")
        for line in file:
            curr = int(line)
            if curr > prev:
                larger += 1
            prev = curr

    return larger

def part_two():
    larger = 0

    with open(infile) as file:
        lines = file.readlines()
        for i in range(len(lines)-3):
            a = int(lines[i])
            b = int(lines[i+1])
            c = int(lines[i+2])
            d = int(lines[i+3])
            first = a+b+c
            second = b+c+d
            if first < second:
                larger += 1

    return larger

print("Part 1:", part_one())
print("Part 2:", part_two())

