import random

board = []

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def choose_first():
    if random.randint(0, 1) == 0:
        return 'p1'
    else:
        return 'p2'

def display_board(board):
    print("\n" * 5)
    print(" " + board[0] + "|" + board[1] + "|" + board[2] + " ")
    print("-------")
    print(" " + board[3] + "|" + board[4] + "|" + board[5] + " ")
    print("-------")
    print(" " + board[6] + "|" + board[7] + "|" + board[8] + " ")

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)-1):
        position = input('Choose your next position: (1-9) ')
    return int(position)-1

def space_check(board, position):
    return board[position] == ' '

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,player):
    if (board[0] == board[1] == board[2]==player) or \
            (board[3] == board[4] == board[5]==player) or \
            (board[6] == board[7] == board[8]==player) or \
            (board[0] == board[3] == board[6]==player) or \
            (board[1] == board[4] == board[7]==player) or \
            (board[2] == board[5] == board[8]==player) or \
            (board[0] == board[4] == board[8]==player) or \
            (board[2] == board[4] == board[6]==player):
        return True
    else:
        return False

def full_board(board):
    if " " in board:
        return False
    else:
        return True

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

''' =========================================================================================================================  '''

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    board = [' '] * 9
    p1_sym, p2_sym = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'p1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, p1_sym, position)

            if win_check(board, p1_sym):
                display_board(board)
                print('Congratulations! You Player 1 have won the game!')
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'p2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, p2_sym, position)

            if win_check(board, p2_sym):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'p1'

    if not replay():
        break




