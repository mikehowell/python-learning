import random


def display_board(board):
    padding_char = " "
    horizontal_char = "-"
    vertical_char = "|"

    print(" " * 11)
    print(
        (padding_char * 3)
        + vertical_char
        + (padding_char * 3)
        + vertical_char
        + (padding_char * 3)
    )
    print(
        padding_char
        + board[7]
        + padding_char
        + vertical_char
        + padding_char
        + board[8]
        + padding_char
        + vertical_char
        + padding_char
        + board[9]
        + padding_char
    )
    print(
        (horizontal_char * 3)
        + vertical_char
        + (horizontal_char * 3)
        + vertical_char
        + (horizontal_char * 3)
    )
    print(
        padding_char
        + board[4]
        + padding_char
        + vertical_char
        + padding_char
        + board[5]
        + padding_char
        + vertical_char
        + padding_char
        + board[6]
        + padding_char
    )
    print(
        (horizontal_char * 3)
        + vertical_char
        + (horizontal_char * 3)
        + vertical_char
        + (horizontal_char * 3)
    )
    print(
        padding_char
        + board[1]
        + padding_char
        + vertical_char
        + padding_char
        + board[2]
        + padding_char
        + vertical_char
        + padding_char
        + board[3]
        + padding_char
    )
    print(
        (padding_char * 3)
        + vertical_char
        + (padding_char * 3)
        + vertical_char
        + (padding_char * 3)
    )


def win_check(board, mark):

    return (
        (board[7] == mark and board[8] == mark and board[9] == mark)
        or (  # across the top
            board[4] == mark and board[5] == mark and board[6] == mark
        )
        or (  # across the middle
            board[1] == mark and board[2] == mark and board[3] == mark
        )
        or (  # across the bottom
            board[7] == mark and board[4] == mark and board[1] == mark
        )
        or (  # down the middle
            board[8] == mark and board[5] == mark and board[2] == mark
        )
        or (  # down the middle
            board[9] == mark and board[6] == mark and board[3] == mark
        )
        or (  # down the right side
            board[7] == mark and board[5] == mark and board[3] == mark
        )
        or (board[9] == mark and board[5] == mark and board[1] == mark)  # diagonal
    )  # diagonal


def player_input():
    marker = ""

    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(
        board, position
    ):
        position = int(input("Choose your next position: (1-9) "))

    return position


def replay():

    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")


def space_check(board, position):
    return board[position] != "X" or board[position] != "O"
    # return board[position] == " "


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


##################################

print("Welcome to Tic Tac Toe!")

while replay():
    # Set the game up here
    Player_1, Player_2 = player_input()

    player_turn = choose_first()
    print(f"{player_turn} will go first")
    start_board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    display_board(start_board)
    current_board = start_board

    while not (full_board_check(current_board)):

        if player_turn == "Player 1":
            # how to check if position is in use!!
            current_board[(player_choice(current_board))] = Player_1
            display_board(current_board)
            # need to test if move resulted in win or draw
            if win_check(current_board, Player_1):
                print(f"{player_turn} wins")
                break
            elif full_board_check(current_board):
                print("It's a draw")
                break
            else:
                player_turn = "Player 2"

        if player_turn == "Player 2":
            current_board[(player_choice(current_board))] = Player_2
            display_board(current_board)
            if win_check(current_board, Player_2):
                print(f"{player_turn} wins")
                break
            elif full_board_check(current_board):
                print("It's a draw")
                break
            else:
                player_turn = "Player 1"

    # while game_on:
    # Player 1 Turn

    # Player2's turn.

    # pass

    if not replay():
        break

# if __name__ == "__main__":
#     print(__name__)
#     start_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     display_board(start_board)

