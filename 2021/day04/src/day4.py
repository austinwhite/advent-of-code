infile = "../input/input.txt"

def get_draws():
    with open(infile) as file:
        draws = file.readline()
        draws = draws.rstrip()
        draws = draws.split(',')
        return [int(x) for x in draws]

def get_boards():
    boards = []

    with open(infile) as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
            if lines[i] == "\n":
                boards.append([])
            else:
                board_row = [[int(x), False] for x in lines[i].split()]
                boards[-1].append(board_row)

    return boards

def check_segment(segment):
    total = 0
    for ele in segment:
        if ele[1] == False:
            return False
        total += ele[0]
    return total

def sum_unmarked(board):
    total = 0

    for i in range(len(board[0])):
        for j in range(len(board[i])):
            if not board[i][j][1]:
                total += board[i][j][0]
    return total

def check_for_win(board, i, j):
    winning_row = check_segment(board[i])
    if winning_row:
        return sum_unmarked(board)
    winning_col = check_segment([col[j] for col in board])
    if winning_col:
        return sum_unmarked(board)
    return False

def is_last_winner(win_tracker):
    for x in win_tracker:
        if not x:
            return False
    return True

def process_draw(draw, boards, win_tracker=[]):
    for board_num, board in enumerate(boards):
        for i in range(len(board[0])):
            for j in range(len(board[i])):
                if board[i][j][0] == draw:
                    board[i][j][1] = True
                    is_winner = check_for_win(board, i, j)
                    if is_winner:
                        win_tracker[board_num] = True
                        if is_last_winner(win_tracker):
                            return is_winner

def part_one():
    draws = get_draws()
    boards = get_boards()
    
    for draw in draws:
        winner = process_draw(draw, boards)
        if winner:
            return draw * winner 

def part_two():
    draws = get_draws()
    boards = get_boards()
    win_tracker = [False for board in boards]

    for draw in draws:
        winner = process_draw(draw, boards, win_tracker)
        if winner:
            return draw * winner
    

# print("Part 1:", part_one())
print("Part 2:", part_two())