total_score = 0

my_shape = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3, # scissors
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

with open("input.txt", "r") as fd:
    for line in fd:
        opp, me = line.split()
        if me == "X":
            shape = lose[opp]
            total_score += my_shape[lose[opp]]
        elif me == "Y":
            total_score += my_shape[draw[opp]]
            total_score += 3
        elif me == "Z":
            total_score += my_shape[win[opp]]
            total_score += 6

print("total: ", total_score)
