import sys

def check(board):
    # Check for consecutive 'H' or 'B' in rows and columns
    for row in range(len(board)):
        for col in range(len(board[row])):
            if not col == len(board[row]) - 1:
                if board[row][col] == board[row][col + 1] == 'H':
                    return False
                if board[row][col] == board[row][col + 1] == 'B':
                    return False
            if not row == 0:
                if board[row][col] == board[row - 1][col] == 'H':
                    return False
                if board[row][col] == board[row - 1][col] == 'B':
                    return False
    return True


def check_limits(board, constrains):
    def check_row(board, high, base):
        # Check if the counts of 'H' and 'B' in each row satisfy the constraints
        for row in range(len(board)):
            base_ct , high_ct = 0, 0
            for col in range(len(board[0])):
                if board[row][col] == 'H':
                    high_ct += 1
                if board[row][col] == 'B':
                    base_ct  += 1
            if int(high[row]) >= 0:
                if not high_ct == int(high[row]):
                    return False
            if int(base[row]) >= 0:
                if not base_ct == int(base[row]):
                    return False
        return True

    def check_col(board, high, base):
        # Check if the counts of 'H' and 'B' in each column satisfy the constraints
        for column in range(len(board[0])):
            base_ct, high_ct = 0, 0
            for row in range(len(board)):
                if board[row][column] == 'H':
                    high_ct += 1
                if board[row][column] == 'B':
                    base_ct += 1
            if int(high[column]) >= 0:
                if not high_ct == int(high[column]):
                    return False
            if int(base[column]) >= 0:
                if not base_ct == int(base[column]):
                    return False
        return True

    # Check both row and column constraints
    return check_row(board, constrains[0], constrains[1]) and \
           (check_col(board, constrains[2], constrains[3]))


def high_base(board, constrains):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'L':
                # Place 'H' and 'B' in consecutive cells
                board[row][col], board[row][col + 1] = 'H', 'B'
                if final_check(board):
                    # Check if the puzzle is solved and satisfies constraints
                    if not (check(board) and
                            check_limits(board, constrains)):
                        return False
                return True
            if board[row][col] == 'U':
                # Place 'H' and 'B' in consecutive cells
                board[row][col], board[row + 1][col] = 'H', 'B'
                if final_check(board):
                    # Check if the puzzle is solved and satisfies constraints
                    if not (check(board) and
                            check_limits(board, constrains)):
                        return False
                return True
    return True


def base_high(board, constrains):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'L':
                # Place 'B' and 'H' in consecutive cells
                board[row][col], board[row][col + 1] = 'B', 'H'
                if final_check(board):
                    # Check if the puzzle is solved and satisfies constraints
                    if not (check(board) and
                            check_limits(board, constrains)):
                        return False
                return True
            if board[row][col] == 'U':
                # Place 'B' and 'H' in consecutive cells
                board[row][col], board[row + 1][col] = 'B', 'H'
                if final_check(board):
                    # Check if the puzzle is solved and satisfies constraints
                    if not (check(board) and
                            check_limits(board, constrains)):
                        return False
                return True
    return True


def N_N(board, constrains):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'L':
                # Place 'N' in consecutive cells
                board[row][col], board[row][col + 1] = 'N', 'N'
                if final_check(board):
                    # Check if the puzzle is solved and satisfies constraints
                    if not (check(board) and
                            check_limits(board, constrains)):
                        return False
                return True
            if board[row][col] == 'U':
                # Place 'N' in consecutive cells
                board[row][col], board[row + 1][col] = 'N', 'N'
                if final_check(board):
                    # Check if the puzzle is solved and satisfies constraints
                    if not (check(board) and
                            check_limits(board, constrains)):
                        return False
                return True
    return True


def solve_puzzle(board, constrains, output_file):
    # Check if the initial board already satisfies constraints
    if final_check(board) and\
            check(board) and\
            check_limits(board, constrains):
        print_board(board, output_file)
        return board

    # Create a copy of the board to try different possibilities
    board_copy = [row[:] for row in board]

    # Try placing 'H' and 'B'
    if high_base(board_copy, constrains) and\
            check(board_copy):
        result = solve_puzzle(board_copy, constrains, output_file)
        if result:
            return result

    # Create another copy of the board to try different possibilities
    board_copy = [row[:] for row in board]

    # Try placing 'B' and 'H'
    if base_high(board_copy, constrains) and\
            check(board_copy):
        result = solve_puzzle(board_copy, constrains, output_file)
        if result:
            return result

    # Create another copy of the board to try different possibilities
    board_copy = [row[:] for row in board]

    # Try placing 'N'
    if N_N(board_copy, constrains) and\
            check(board_copy):
        result = solve_puzzle(board_copy, constrains, output_file)
        if result:
            return result

    return None


def final_check(board):
    # Check if there are no 'L' or 'U' cells in the board
    for row in board:
        if 'U' in row:
            return False
        if 'L' in row:
            return False
    return True


def print_board(board, output_file):
    # Print the board to the output file
    for row in board:
        if not row == len(board) - 1:
            output_file.write(' '.join(row) + '\n')
        else:
            output_file.write(' '.join(row))


def main():
    # Get input and output file names from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Open and read input file
    input_file = open(input_file, "r")
    lines = [line.split() for line in input_file]
    constrains = lines[:4]
    board = lines[4:]

    # Open output file
    output_file = open(output_file, "w")

    # Solve the puzzle and print the result
    result = solve_puzzle(board, constrains, output_file)
    if not result:
        output_file.write("No solution!")


if __name__ == "__main__":
    main()