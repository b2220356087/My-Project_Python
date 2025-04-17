# Take input from the user to determine the size of the board
size = int(input("What Size Game GoPy?"))

# Initialize the board
board = [[str(i * size + j) for j in range(size)] for i in range(size)]

# Initialize player 1 to start the game
player = "1"

# Variables to keep of the sign (X or O) and the moves made
sign = ""
check = ""

# Function to print the current state of the board
def print_board(board):
    x = len(board)
    for i in range(x):
        for j in range(x):
            print(board[i][j], end=' ')
        print()
print_board(board)
# Function to check if a player has won
def check_winner(board, sign):
    size = len(board)
    for i in range(size):
        for j in range(size):
            # Check horizontal
            if j + size - 1 < size and all(board[i][j+k] == sign for k in range(size)):
                return True
            # Check vertical
            if i + size - 1 < size and all(board[i+k][j] == sign for k in range(size)):
                return True
            # Check diagonal (top-left to bottom-right)
            if i + size - 1 < size and j + size - 1 < size and all(board[i+k][j+k] == sign for k in range(size)):
                return True
            # Check diagonal (top-right to bottom-left)
            if i + size - 1 < size and j - size + 1 >= 0 and all(board[i+k][j-k] == sign for k in range(size)):
                return True
    return False

# Main game loop
while True:
    # Take input from the current player
    move = input(f"Player {player} turn--> ")

    # Check if the input is valid
    if int(move) not in range(0, size * size) or move in check:
        print("Please enter a valid number")
    check += move

    # Determine the sign (X or O) for the current player
    if player == "1":
        sign = "X"
    else:
        sign = "O"

    # Update the board based on the player's move
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == move:
                if player == "1":
                    board[i][k] = "X"
                    player = "2"
                elif player == "2":
                    board[i][k] = "O"
                    player = "1"
                else:
                    continue

    # Print the updated board
    print_board(board)

    # Check if the current player has won
    if check_winner(board, sign):
        # Switch player as the current player has won
        if player == "1":
            print("Winner: O")
        else:
            print("Winner: X")
        # Exit the game loop
        break