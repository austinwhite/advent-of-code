infile = "../input/input.txt"

day = 256
state = [0 for _ in range(9)]

def setNthState(days):
    global state

    for _ in range(days):
        dying = state[0]
        state = state[1:]+[0]
        state[6] += dying
        state[8] += dying

with open(infile) as file:
    values = file.readline().rstrip().split(',')
    for val in values:
        state[int(val)] += 1

    setNthState(day)
    print("fish population on", day, "day:", sum(state))