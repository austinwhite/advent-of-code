infile = "../input/data.in"

with open(infile) as f:
    data = [line for line in f.read().strip().split('\n')]

def part1():
    outputs = [line.split('|')[1].strip().split(' ') for line in data]

    lengths_allowed = [2, 3, 4, 7]

    total_count = 0
    for output in outputs:
        for digit in output:
            if len(digit) in lengths_allowed:
                total_count += 1

    return total_count

def part2():
    inputs = [line.split('|')[0].strip().split(' ') for line in data]
    outputs = [line.split('|')[1].strip().split(' ') for line in data]

    total_sum = 0

    for i in range(len(data)):
        digit_map = {}

        for digit in inputs[i]:
            if len(digit) == 2:
                digit_map[1] = digit
            elif len(digit) == 4:
                digit_map[4] = digit
            elif len(digit) == 3:
                digit_map[7] = digit
            elif len(digit) == 7:
                digit_map[8] = digit
        
        for digit in inputs[i]:
            if len(digit) == 6:
                if set(digit_map[4]).issubset(set(digit)):
                    digit_map[9] = digit
                elif set(digit_map[1]).issubset(set(digit)):
                    digit_map[0] = digit
                else:
                    digit_map[6] = digit

        for digit in inputs[i]:
            if len(digit) == 5:
                if set(digit).issubset(set(digit_map[6])):
                    digit_map[5] = digit
                elif set(digit_map[1]).issubset(set(digit)):
                    digit_map[3] = digit
                else:
                    digit_map[2] = digit


        number = []
        for digit in outputs[i]:
            for key, value in digit_map.items():
                if set(digit) == set(value):
                    number.append(str(key))

        number = int(''.join(number))
        total_sum += number

    return total_sum
            

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')