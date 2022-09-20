from statistics import median, mean

infile = "../input/data.in"
positions = []

with open(infile) as f:
    positions = [int(x) for x in f.readline().strip().split(',')]

def calculate_fuel(position):
    total_fuel = 0
    for num in positions:
        total_fuel += abs(position - num)
    
    return total_fuel

def natural_number_sum(position):
    return (position * (position + 1)) // 2

def part1():
    median_position = int(median(positions))
    return calculate_fuel(median_position)
    
def part2_naive():
    min_fuel = 1 << 100
    min_position = min(positions)
    max_position = max(positions)

    for position in range(min_position, max_position):
        fuel = 0
        for crab in positions:
            fuel += natural_number_sum(abs(crab - position))
        
        min_fuel = min(min_fuel, fuel)

    return min_fuel

def part2_optimal():
    min_fuel = 0
    avg = round(mean(positions))-1

    for position in positions:
        min_fuel += natural_number_sum(abs(position - avg))

    return min_fuel

print("Part 1:", part1())
print("Part 2:", part2_naive())
print("Part 2:", part2_optimal())
