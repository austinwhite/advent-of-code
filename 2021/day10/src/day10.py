infile = "../input/input.txt"

LAST_INDEX = -1
corrupted_point_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
completion_point_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
completion_points = []
corrupted_points = 0

def is_opening_bracket(bracket):
    open_brackets = ['(', '[', '{', '<']
    return bracket in open_brackets    

def get_opening_bracket(bracket):
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    return bracket_pairs[bracket]

def get_closing_bracket(bracket):
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    return bracket_pairs[bracket]

def get_bracket_pairing(bracket):
    if is_opening_bracket(bracket):
        return get_closing_bracket(bracket)
    else:
        return get_opening_bracket(bracket)

def get_completion_chunk(leftover_stack):
    completion_chunk = ""

    for bracket in leftover_stack:
        bracket_pairing = get_bracket_pairing(bracket)
        completion_chunk = bracket_pairing + completion_chunk

    return completion_chunk

def get_completion_points(leftover_stack):
    completion_points = 0
    completion_chunk = get_completion_chunk(leftover_stack)

    for bracket in completion_chunk:
        completion_points *= 5
        completion_points += completion_point_map[bracket]

    return completion_points

def get_middle_completion_point(completion_points):
    middle_index = len(completion_points)//2
    completion_points.sort()
    return completion_points[middle_index]

with open(infile) as file:
    for line in file:
        stack = []
        incomplete = 1
        line = line.rstrip()
        for bracket in line:
            if is_opening_bracket(bracket):
                stack.append(bracket)
            else:
                top = stack[LAST_INDEX]
                if top == get_bracket_pairing(bracket):
                    stack.pop(LAST_INDEX)
                else:
                    corrupted_points += corrupted_point_map[bracket]
                    incomplete = 0
                    break
        if incomplete:
            completion_points.append(get_completion_points(stack))

print("Corrupted Points:", corrupted_points)
print("Completion Points:", get_middle_completion_point(completion_points))