def init_board():
    rowA = [".", ".", "."]
    rowB = [".", ".", "."]
    rowC = [".", ".", "."]
    board = [rowA, rowB, rowC]
    return board

def validate_user_input(input):
    valid = False
    if len(input) == 2:
        if input[0] in ["A", "B", "C"] and input[1] in ["1", "2", "3"]:
            valid = True
        else:
            print('Wrong coordinates')
    else:
        print('Please enter valid coordinates')
    return valid

def get_move():
    valid_user_input = ''
    while valid_user_input == '':
        user_input = input('Please provide cordindate: ')
        if validate_user_input(user_input):
            valid_user_input = user_input
        else:
            valid_user_input = ''
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    print("   1   2   3   ")
    print("   " + board[0][0] + " | " + board[0][1]  + " | " + board[0][2]  )
    print("  ---+---+---")
    print("   " + board[1][0] + " | " + board[1][1]  + " | " + board[1][2]  )
    print("  ---+---+---")
    print("   " + board[2][0] + " | " + board[2][1]  + " | " + board[2][2]  )
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass

'''
def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
'''
############################
#Testing purpose only
init_board = init_board()
print_board(init_board)
