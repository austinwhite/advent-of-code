data = []
stacks = [[],[],[]]
opps = []

with open("input.txt", "r") as fd:
    for line in fd:
        data.append(line)

i = 0
while '[' in data[i]:
    line = data[i]
    col = -1
    for j in range(1, len(line), 4):
        col += 1
        if line[j].strip():
            stacks[col].append(line[j])
        if col == 2:
            col = -1
    i += 1

i += 2

while i < len(data):
    s = data[i].split()
    opps.append([s[1], s[3], s[5]])
    i += 1


print(stacks)
print(opps)
