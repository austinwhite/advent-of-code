import re

infile = "../input/input.txt"
board = [[0]]
overlaps = 0

def print_board():
    for row in board:
        for col in row:
            print(col, end="")
        print("\n", end="")
    
    print("\n")

def expand_width(new_width):
    curr_width = len(board[0])

    for i in range(len(board)):
        add_n = new_width - curr_width
        board[i] = board[i] + ([0] * add_n)

def expand_height(new_height):
    add_n = new_height - len(board)

    for _ in range(add_n):
        board.append([0]*len(board[0]))

def expand_baord(point_a, point_b):
    max_width = max(point_a[0], point_b[0])+1
    max_height = max(point_a[1], point_b[1])+1

    if len(board[0]) < max_width:
        expand_width(max_width)
    if len(board) < max_height:
        expand_height(max_height)

def plot_vertical(point_a, point_b):
    global overlaps
    col = point_a[0]
    top = min(point_a[1], point_b[1])
    bottom = max(point_a[1], point_b[1])+1

    for row in range(top, bottom):
        if board[row][col] == 1:
            overlaps += 1
        board[row][col] += 1

def plot_horizontal(point_a, point_b):
    global overlaps
    row = board[point_a[1]]
    left = min(point_a[0], point_b[0])
    right = max(point_a[0], point_b[0])+1

    for i in range(left, right):
        if row[i] == 1:
            overlaps += 1
        row[i] += 1

def plot_diagonal_positive(bottom_left_point, top_right_point):
    global overlaps
    start_x = bottom_left_point[0]
    start_y = bottom_left_point[1]
    end_x = top_right_point[0]+1

    for i in range(0, end_x-start_x):
        if board[start_y+i][start_x+i] == 1:
            overlaps += 1
        board[start_y+i][start_x+i] += 1

def plot_diagonal_negative(top_left_point, bottom_right_point):
    global overlaps
    start_x = top_left_point[0]
    start_y = top_left_point[1]
    end_x = bottom_right_point[0]+1

    for i in range(0, end_x-start_x):
        if board[start_y-i][start_x+i] == 1:
            overlaps += 1
        board[start_y-i][start_x+i] += 1

def plot_diagonal(point_a, point_b):
    lower_point = 0
    upper_point = 0
    left_point = 0
    right_point = 0

    if point_a[0] < point_b[0]:
        lower_point = point_a
        upper_point = point_b
    else:
        lower_point = point_b
        upper_point = point_a

    if point_a[1] < point_b[1]:
        left_point = point_a
        right_point = point_b
    else:
        left_point = point_b
        right_point = point_a

    if left_point == lower_point:
        plot_diagonal_positive(left_point, right_point)
    else:
        plot_diagonal_negative(lower_point, upper_point)

def plot_line(point_a, point_b):
    if point_a[0] == point_b[0] and not (point_a[1] == point_b[1]):
        plot_vertical(point_a, point_b)
    elif point_a[1] == point_b[1] and not (point_a[0] == point_b[0]):
        plot_horizontal(point_a, point_b)
    else:
        plot_diagonal(point_a, point_b)

with open(infile) as file:
    for line in file:
        x1, y1, _, _, x2, y2, _ = re.split(',|\s|->|\n', line)
        point_a = [int(x1), int(y1)]
        point_b = [int(x2), int(y2)]
        expand_baord(point_a, point_b)
        plot_line(point_a, point_b)

print("Horizontal|Vertical|Diagonal Overlaps:", overlaps)
