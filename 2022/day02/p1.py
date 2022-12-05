total_score = 0

my_shape = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3, # scissors
}

win = {
    "X": "C", # rock beats scissors
    "Y": "A", # paper beats rock
    "Z": "B", # scissors beats paper
}

draw = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

with open("input.txt", "r") as fd:
    for line in fd:
        opp, me = line.split()
        total_score += my_shape[me]
        if draw[me] == opp:
            total_score += 3
        if win[me] == opp:
            total_score += 6

print("total: ", total_score)
