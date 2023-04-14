
def intro():
    """
    Gives the user information and rules about the games.
    Allows the user to start the game by entering 'y'.
    Catches error for data input incorrectly.
    """
    print("Welcome to Tic-Tac-Toe, 2 player edition!")
    print("\nRules:\n")
    print("Player 1 is given 'X'")
    print("Player 2 is given 'O'\n")
    print("A 3x3 board is printed and is marked 1-9\n")
    print("Win: If 3 spots are filled in a row, column or diagonally.\n")
    print("Tie: The board is filled and 'X' or 'O' are not in a row.\n")
    print("Are you ready to play?\n")

    yes_no = input("Enter 'Y' for Yes - Enter 'N' for No: ")
    if yes_no == "y":
        print_board()
    elif yes_no == "n":
        print("\n\nPlease read the rules again.\n\n")
        intro()
    else:
        print(f"You entered: '{yes_no}', Please enter 'y' or 'n'.")
        print("")
        intro()


# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def print_board():
    """
    Displays the board for the game.
    """
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")


intro()


def play_game():
    """
    controls the game.
    """

    check_if_game_going = True
    player = "X"
    winner = None

    while check_if_game_going:
        handle_turn(player)

    if winner == "X":
        print("\nX won.")
    elif winner == "O":
        print("\nO won.")
    elif winner is None:
        print("Game is a draw.")


def handle_turn(player):
    """
    Allows the user to input a number from 1-9.
    """
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = "X"
    print_board()


play_game()

def check_for_win():
    """
    Checks for a winner by checking rows, columns and diagonals.
    """

    winner = None

    # Check for rows, columns, or diagonals
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
    return


def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return        