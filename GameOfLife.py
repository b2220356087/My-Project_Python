def nextGeneration(grid, M, N):
    # Create a new grid for the next generation
    future = [[0 for i in range(N)] for j in range(M)]

    # Loop through every cell
    for l in range(M):
        for m in range(N):
            # finding no Of Neighbours that are alive
            aliveNeighbours = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ((l + i >= 0 and l + i < M) and (m + j >= 0 and m + j < N)):
                        aliveNeighbours += grid[l + i][m + j]

            # The cell needs to be subtracted from
            # its neighbours as it was counted before
            aliveNeighbours -= grid[l][m]

            # Implementing the Rules of Life

            # Cell is lonely and dies
            if ((grid[l][m] == 1) and (aliveNeighbours < 2)):
                future[l][m] = 0

            # Cell dies due to overpopulation
            elif ((grid[l][m] == 1) and (aliveNeighbours > 3)):
                future[l][m] = 0

            # A new cell is born
            elif ((grid[l][m] == 0) and (aliveNeighbours == 3)):
                future[l][m] = 1

            # Remains the same
            else:
                future[l][m] = grid[l][m]

    # Return the next generation
    return future


def print_board(board, generation, living_cells):
    M = len(board)
    N = len(board[0])

    # Print column indices
    print("   ", end="")
    for i in range(N):
        print(f"{i:2}", end=" ")
        if (i + 1) % 5 == 0 and i < N - 1:
            print("|", end=" ")
    print()

    # Print top border
    print("  ", end="")
    print("┌" + "─" * ((N * 3) - 2) + "┐")

    # Print board contents with row indices and borders
    for i in range(M):
        print(f"{i:2} │ ", end="")
        for j in range(N):
            print("_" if board[i][j] == 0 else "O", end="  ")
            if (j + 1) % 5 == 0 and j < N - 1:
                print("| ", end="")
        print("│")

    # Print bottom border
    print("  ", end="")
    print("└" + "─" * ((N * 3) - 2) + "┘")

    print(f"\nLiving cells: {living_cells}")
    print(f"Generation: {generation}\n")


def toggle_cell_state(board):
    while True:
        try:
            cell_input = input("Enter the row, column indices separated by a comma to toggle cell state: ")
            if cell_input.lower() == 'r':
                return False, None, None
            row, col = map(int, cell_input.split(","))
            return True, row, col
        except ValueError:
            print("Invalid input! Please enter row and column numbers separated by a comma.")
        except IndexError:
            print("Invalid input! Please enter valid row and column numbers.")


def main_menu():
    # Print the main menu options
    print("Main Menu:")
    print("1. Select initial pattern")
    print("2. Control simulation speed")
    print("3. Start Game")
    print("4. Quit Game")


def game_menu():
    # Print the game menu options
    print("Game Menu:")
    print("1. Toggle cell state")
    print("2. Continue the next generation(s)")
    print("3. Quit Game")


def main(rows, cols, generations):
    # Create the initial grid for the game
    grid = [[0] * cols for _ in range(rows)]
    generation = 0

    while True:
        main_menu()
        choice = input("Your selection: ")

        if choice == '1':
            # Implement pattern selection later
            print("Pattern selection will be implemented later.")
        elif choice == '2':
            # Implement simulation speed control later
            print("Simulation speed control will be implemented later.")
        elif choice == '3':
            print("Starting the game...")
            # Print the initial board configuration
            print_board(grid, generation, sum(sum(row) for row in grid))
            while True:  # Enter game loop after starting the game
                game_menu()
                game_choice = input("Your selection: ")
                if game_choice == '1':
                    # Toggle the state of a cell
                    toggle, row, col = toggle_cell_state(grid)
                    if toggle:
                        if row is not None and col is not None:
                            grid[row][col] = 1 if grid[row][col] == 0 else 0
                            # Print the updated board configuration
                            print_board(grid, generation, sum(sum(row) for row in grid))
                elif game_choice == '2':
                    # Proceed to the next generation
                    generation += 1
                    grid = nextGeneration(grid, rows, cols)
                    # Print the updated board configuration
                    print_board(grid, generation, sum(sum(row) for row in grid))
                elif game_choice == '3':
                    # Quit the game
                    print("Quitting the game...")
                    return
        elif choice == '4':
            # Quit the game
            print("Quitting the game...")
            return

if __name__ == "__main__":
    rows = 30
    cols = 30
    generations = 50
    main(rows, cols, generations)

#2220356087 Fikret Karakuzu