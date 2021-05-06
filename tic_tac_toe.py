def init_board():
    rowA = ["x", ".", "."]
    rowB = [".", "x", "."]
    rowC = [".", ".", "x"]
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
        user_input = input('Please provide coordindates: ')
        if input[0] == "A" and row == 0:
            valid_user_input = user_input
        elif input[0] == "B" and row == 1:
            valid_user_input = user_input
        else row == 2
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
    #checking line
    while i <= 2:
        if board[i][0] != "." and board[i][0] == board[i][1] == board[i][2]:
            print("has winner line")
            return True
            break
        i+=1
    #checking column
    j=0
    while j <= 2:
        if board[0][j] != "." and board[0][j] == board[1][j] == board[2][j]:
            print("has winner column")
            return True
            break
        j+=1
    #checking crossing
    if board[1][1] != "." and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        print("Has winner cross")
        return True
    
    #else: no winner
    print("Has no winner")
    return False


def is_full(board):
   for i in range(1,10):
       if has_won(board, i):
           return True
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

