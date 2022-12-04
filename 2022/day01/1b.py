max_calories_a = 0
max_calories_b = 0
max_calories_c = 0

with open("input.txt", "r") as fd:
    calories = 0

    for line in fd:
        if line.strip():
            calories += int(line)
        else:
            if calories > max_calories_a:
                max_calories_c = max_calories_b
                max_calories_b = max_calories_a
                max_calories_a = calories
            elif calories > max_calories_b:
                max_calories_c = max_calories_b
                max_calories_b = calories
            elif calories > max_calories_c:
                max_calories_c = calories
            calories = 0

print("Top three: ", max_calories_a, max_calories_b, max_calories_c)
print("Total: ", max_calories_a + max_calories_b + max_calories_c)
