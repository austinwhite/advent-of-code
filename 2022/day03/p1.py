total = 0

def get_code(c):
    value = 0

    if ord('A') <= ord(c) <= ord('Z'):
        value += 26

    value += ord(c.lower()) - ord('a')

    return value + 1


with open("input.txt", "r") as fd:
    for line in fd:
        ruck_a = line[:len(line)//2]
        ruck_b = line[len(line)//2:]

        items_a = {}
        items_b = {}

        for item in ruck_a:
            items_a[item] = items_a.get(item, 0) + 1

        for item in ruck_b:
            items_b[item] = items_b.get(item, 0) + 1

        for item in items_a:
            if item in items_b:
                total += get_code(item)

print("total: ", total)
