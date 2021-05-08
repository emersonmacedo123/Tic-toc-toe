def clean_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def init_board():
    rowA = [".", ".", "."]
    rowB = [".", ".", "."]
    rowC = [".", ".", "."]
    board = [rowA, rowB, rowC]
    return board

def validate_user_input(input):
    valid = 0
    #Check if in board range
    if len(input) == 2:
        if input[0] in ["A", "B", "C"] and input[1] in ["1", "2", "3"]:
            valid = 1
        else:
            print('Coordinates out of range')
    #check if input is quit
    elif input == "QUIT":
        valid = 2
    else:
        print('Please enter valid coordinates')
     
    return valid


def get_move():
    valid_user_input = ''
    row = 0
    col = 0
    while valid_user_input == '':
        user_input = input('Please provide coordindates: ')
        #case valid and not quit
        if validate_user_input(user_input) == 1:
            valid_user_input = user_input
            #converting row to number
            if user_input[0] == "A":
                row = 0
            elif user_input[0] =="B":
                row = 1
            else:
                row = 2
            #converting col to number
            col = int(user_input[1]) -1
        elif validate_user_input(user_input) == 2:
            valid_user_input = user_input
            row = -1
            col = row
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    valid_mark = False
    if board[row][col] == ".":
        if player == "P1":
            board[row][col] = "X"
        else:
            board[row][col] = "0"
        valid_mark = True
    else:
        print("Cell is occupied. Please try again.")
        valid_mark = False
        
    return board, valid_mark



def has_won(board):
    i = 0
    #checking line
    while i <= 2:
        if board[i][0] != "." and board[i][0] == board[i][1] == board[i][2]:
            return True
            break
        i+=1
    #checking column
    j=0
    while j <= 2:
        if board[0][j] != "." and board[0][j] == board[1][j] == board[2][j]:
            return True
            break
        j+=1
    #checking crossing
    if board[1][1] != "." and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return True
    
    #else: no winner
    return False

def is_full(board):
    i = 0
    while i <= 2:
        j = 0
        while j <= 2:
            if board[i][j] == ".":
                return False
            j+=1
        i+=1
    
    return True



def print_board(board):
    print("    1   2   3   ")
    print("A   " + board[0][0] + " | " + board[0][1]  + " | " + board[0][2]  )
    print("  ---+---+---")
    print("B   " + board[1][0] + " | " + board[1][1]  + " | " + board[1][2]  )
    print("  ---+---+---")
    print("C   " + board[2][0] + " | " + board[2][1]  + " | " + board[2][2]  )
    


def print_result(player, winner, tie):
    #proclains winner
    if winner:
        print("Congrats player " + player + "! You won the game :)")
    #proclaims tie 
    elif tie:
        print("...And there's a tie :/ ")
    else:
        pass

def change_player(player):
    new_player = ""
    if player == "P1":
        new_player = "P2"
    elif player == "P2":
        new_player = "P1"
    return new_player 



def tictactoe_game(mode='HUMAN-HUMAN'):
    clean_terminal()
    print("Welcome to Tic-Tac-Toe game.")
    replay = True
    
    while replay == True:
        board = init_board()
        player = "P1" 
        gameContinue = True
        while gameContinue == True:
            print_board(board)
            occupied_check = False
            while occupied_check == False:
                row, col = get_move()
                #if condition QUIT is activated
                if row == -1:
                    print("You decided to quit the game. Thank you.")
                    gameContinue = False
                [board, validity] = mark(board, player, row, col)
                occupied_check = validity
            clean_terminal()
            winner = has_won(board)
            tie = is_full(board)
            if winner == True or is_full(board) == True:
                print_board(board)
                print_result(player, winner, tie)
                gameContinue = False
            else:
                player=change_player(player)
        if gameContinue == False:
            has_won(board) == True #check if its needed
            replay_trigger = input("Game is over. Would you like to play again? (Y/N)")
            clean_terminal()
            if replay_trigger == "Y":
                print("The game will restart.")
            elif replay_trigger == "N":
                print("Game is over. Thank you.")
                replay = False
                
def main_menu():
    tictactoe_game('HUMAN-HUMAN')

if __name__ == '__main__':
    main_menu() 
    