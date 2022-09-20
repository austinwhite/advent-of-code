infile = "../input/input.txt"

def binary_to_decimal(binary):
    return int(binary, base=2)

def get_oxygen_rating(values):
    value_set = values;
    ones_set = []
    zeros_set = []

    i = 0
    while len(value_set) > 1:
        for value in value_set:
            if value[i] == '1':
                ones_set.append(value)
            else:
                zeros_set.append(value)
        if len(ones_set) < len(zeros_set):
            value_set = zeros_set
        else:
            value_set = ones_set
        ones_set = []
        zeros_set = []
        i += 1
        
    return binary_to_decimal(value_set[0])

def get_c02_rating(values):
    value_set = values;
    ones_set = []
    zeros_set = []

    i = 0
    while len(value_set) > 1:
        for value in value_set:
            if value[i] == '1':
                ones_set.append(value)
            else:
                zeros_set.append(value)
        if len(ones_set) >= len(zeros_set):
            value_set = zeros_set
        else:
            value_set = ones_set
        ones_set = []
        zeros_set = []
        i += 1
        
    return binary_to_decimal(value_set[0])

def part_one():
    num_rates = 0
    total_ones = {}
    gamma = ""
    epsilon = ""

    with open(infile) as file:
        for line in file:
            num_rates += 1
            line = line.rstrip()
            for i in range(len(line)):
                if not total_ones.get(i):
                    total_ones[i] = 0
                total_ones[i] += int(line[i])

    for _, val in total_ones.items():
        mid = num_rates // 2
        if val < mid:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    gamma = binary_to_decimal(gamma)
    epsilon = binary_to_decimal(epsilon)
    
    return gamma * epsilon

def part_two():
    values = []
    
    with open(infile) as file:
        for line in file:
            line = line.rstrip()
            values.append(line)

    oxygen_rating = get_oxygen_rating(values)
    c02_rating = get_c02_rating(values)
    return oxygen_rating * c02_rating

print("Part 1:", part_one())
print("Part 2:", part_two())
