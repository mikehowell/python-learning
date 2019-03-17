def display_board(board):
    padding_char = ' '
    horizontal_char = '-'
    vertical_char = '|'

    print (' ' * 11)
    print((padding_char * 3) + vertical_char + (padding_char * 3) + vertical_char + (padding_char * 3))
    print(padding_char + board[7] + padding_char + vertical_char + padding_char + board[8] + padding_char + vertical_char + padding_char + board[9] + padding_char)
    print((horizontal_char * 3) + vertical_char + (horizontal_char * 3) + vertical_char + (horizontal_char * 3))
    print(padding_char + board[4] + padding_char + vertical_char + padding_char + board[5] + padding_char + vertical_char + padding_char + board[6] + padding_char)
    print((horizontal_char * 3) + vertical_char + (horizontal_char * 3) + vertical_char + (horizontal_char * 3))
    print(padding_char + board[1] + padding_char + vertical_char + padding_char + board[2] + padding_char + vertical_char + padding_char + board[3] + padding_char)
    print((padding_char * 3) + vertical_char + (padding_char * 3) + vertical_char + (padding_char * 3))


# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# empty_board = [' '] * 10
# display_board(empty_board)

start_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(start_board)

# def player_input():
#     marker = ''
    
#     while marker != 'X' and marker != 'O':
#         marker = input ("Player 1, enter 'X' or 'O' to begin: ")
        
#     player1 = marker
#     player2 = 'X' if player1 == 'O' else 'O'
    
#     return(player1, player2)
    

# result = player_input()
# print(result)

def place_marker(board, marker, position):
    board[position] = marker

place_marker(start_board, 'X', 1)
display_board(start_board)