overlaps = 0

with open("input.txt", "r") as fd:
    for line in fd:
        a, b = line.strip().split(',')
        a = a.split('-')
        b = b.split('-')

        if int(a[0]) <= int(b[0]) <= int(a[1]) or int(a[0]) <= int(b[1]) <= int(a[1]):
            overlaps += 1
        elif int(b[0]) <= int(a[0]) <= int(b[1]) or int(b[0]) <= int(a[1]) <= int(b[1]):
            overlaps += 1

print("overlaps: ", overlaps)
