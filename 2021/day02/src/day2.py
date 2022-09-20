import operator

infile = "../input/input.txt"

def part_one():
    horizontal = 0
    depth = 0
    direct = {
        "forward": operator.add,
        "down": operator.add,
        "up": operator.sub,
    }

    with open(infile) as file:
        for line in file:
            line = line.split()
            direction = line[0]
            distance = int(line[1])
            if direction == "forward":
                horizontal = direct[direction](horizontal, distance)
            else:
                depth = direct[direction](depth, distance)
                
    return horizontal * depth

def part_two():
    horizontal = 0
    depth = 0
    aim = 0
    direct = {
        "forward": {
            "horizontal": operator.add,
            "depth": operator.mul,
        },
        "down": operator.add,
        "up": operator.sub,
    }

    with open(infile) as file:
        for line in file:
            line = line.split()
            direction = line[0]
            distance = int(line[1])
            if direction == "forward":
                horizontal = direct[direction]["horizontal"](horizontal, distance)
                depth += direct[direction]["depth"](aim, distance)
            else:
                aim = direct[direction](aim, distance)

    return horizontal * depth

print("Part 1:", part_one())
print("Part 2:", part_two())
