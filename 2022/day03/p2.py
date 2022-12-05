total = 0

def get_code(c):
    value = 0

    if ord('A') <= ord(c) <= ord('Z'):
        value += 26

    value += ord(c.lower()) - ord('a')

    return value + 1


data = []

with open("input.txt", "r") as fd:
    for line in fd:
        data.append(line)

i = 0
while i < len(data):
    ruck_0 = data[i].strip()
    ruck_1 = data[i+1].strip()
    ruck_2 = data[i+2].strip()

    items_0 = {}
    items_1 = {}
    items_2 = {}

    for item in ruck_0:
        items_0[item] = items_0.get(item, 0) + 1

    for item in ruck_1:
        items_1[item] = items_1.get(item, 0) + 1

    for item in ruck_2:
        items_2[item] = items_2.get(item, 0) + 1

    for item in items_0:
        if item in items_1 and item in items_2:
            total += get_code(item)

    i += 3

print("total: ", total)
