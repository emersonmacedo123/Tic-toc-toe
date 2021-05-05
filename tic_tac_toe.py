def init_board():
    rowA = [".", ".", "."]
    rowB = [".", ".", "."]
    rowC = [".", ".", "."]
    board = [rowA, rowB, rowC]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    if board[row][col] == ".":
        if player == "P1":
            board[row][col] = "X"
        else:
            board[row][col] = "0"
    else:
        #do nothing
        pass
    return board



def has_won(board, player):
    i = 0
    while i >= 0:
        print("test")


    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    print("   1   2   3   ")
    print("A   " + board[0][0] + " | " + board[0][1]  + " | " + board[0][2]  )
    print("  ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1]  + " | " + board[1][2]  )
    print("  ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1]  + " | " + board[2][2]  )
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
player = "P1"
row = 2
col = 2
mark(init_board, player, row, col)
print_board(init_board)
mark(init_board, player, row, col)
