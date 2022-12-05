max_calories = 0

with open("input.txt", "r") as fd:
    calories = 0

    for line in fd:
        if line.strip():
            calories += int(line)
        else:
            max_calories = max(max_calories, calories)
            calories = 0

print("Max calories: ", max_calories)
