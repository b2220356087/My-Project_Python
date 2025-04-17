import sys
file = input("please enter your file path: ") #takes the file path
with open(r"{}".format(file), "r", encoding='utf-8') as f:
    lines = f.readlines()
    a = ""
    sudoku = [[], [], [], [], [], [], [], [], []] #transform the data to a list that includes only intagers
    for i in lines:
        a += i
    a = a.replace(" ", "")
    b = a.split("\n")
    c = 0
    timer = 0
    for i in b:
        for k in i:
            k = int(k)
            sudoku[c].append(k)
        c = c + 1


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:   # Check if the number is not present in the current row and column
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)   # Check if the number is not present in the current 3x3 matrix
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty(board):
    for i in range(9):    # Find the first empty slot
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None


def eliminate_solve(board):
    global timer
    while True:
        progress = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:   #Check row and column
                    possibilities = set(range(1, 10))
                    possibilities -= set(board[i])
                    possibilities -= {board[x][j] for x in range(9)}
                    start_row, start_col = 3 * (i // 3), 3 * (j // 3)    # Check 3x3 grid
                    for x in range(3):
                        for y in range(3):
                            possibilities.discard(board[start_row + x][start_col + y])

                    if len(possibilities) == 1:
                        num = possibilities.pop()
                        board[i][j] = num
                        timer = timer+1
                        print("-"*18)
                        print(f"Step {timer} - {num} @ R{i+1}C{j+1}")
                        print("-"*18)
                        print_board(sudoku)
                        progress = True

        if not progress:
            break


def solve_sudoku(board):

    row, col = find_empty(board)    # Find an empty location


    if row is None:    # If there is no empty cell, sudoku is solved
        return True


    for num in range(1, 10):    # Try placing a number in the empty cell
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True


            board[row][col] = 0            # If placing the current number doesn't lead to a solution, backtrack


    return False    # If no number can be placed, backtrack


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()



eliminate_solve(sudoku)