
# Sample TicTacToe Game
# Author: MKC


def display_board(board):
    '''
    Prints out the TicTacToe board
    TicTacToe Game here uses numpad key mapping
    e.g.
        X | O | X
        O | X | O
        X | O | X
    '''
    print(board[7],'|',board[8],'|',board[9])
    print(board[4],'|',board[5],'|',board[6])
    print(board[1],'|',board[2],'|',board[3])


def player_input():
    '''
    Assigns the player's markers as 'X' or 'O'
    e.g.
    player_input()
    Player 1: Do you want to be X or O? x
    ('X', 'O')
    '''
    marker = ''
    while True:
        marker = input('\nPlayer 1: Do you want to be X or O? ').upper()
        if marker == 'X' or marker == 'O':
            break

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    '''
    Assigns a marker ('X' or 'O') to a desired position (number 1-9) in the board
    '''
    board[position] = marker


def win_check(board, mark):
    '''
    Checks to see if that mark has won in the board
    '''
    indices        = {idx for idx, item in enumerate(board) if item == mark}
    horizontal_win = {1,2,3} <= indices or {4,5,6} <= indices or {7,8,9} <= indices
    vertical_win   = {1,4,7} <= indices or {2,5,8} <= indices or {3,6,9} <= indices
    diagonal_win   = {1,5,9} <= indices or {3,5,7} <= indices
    return horizontal_win or vertical_win or diagonal_win


import random
def choose_first():
    '''
     Decide randomly which player goes first
    '''
    return random.randint(1,2)


def space_check(board, position):
    '''
    Checks whether a space on the board is freely available
    Note: '#' is used as placeholder for empty spaces
    '''
    return board[position] != 'X' and board[position] != 'O'

def full_board_check(board):
    '''
    Returns True if board is full, otherwise False
    '''
    return all([ item == 'O' or item == 'X' for item in board[1:]])

def player_choice(board):
    '''
    Takes in a player input
    '''
    while True:
        position = input("\nEnter your move (number 1-9): ")
        try:
            position = int(position)
        except ValueError:
            print('Please input a valid number! Try again!')
            continue
        if 0 < position < 10 and space_check(board, position):
            return position
        else:
            print('Valid range is (number 1-9) and should be blank. Try again!')

def replay():
    reply = input("Continue? (Y or Yes; else any response to exit): ")
    return reply.upper() == 'Y' or reply.upper() == 'YES'



print('Welcome to Tic Tac Toe!')

while True:
    # Blank lines
    print('\n'*5)

    # Initialize the board
    board = list(range(10))
    print('Initial Board:')
    display_board(board)

    # Player1 chooses the markers
    marker = player_input()
    print(f'Player 1: {marker[0]}')
    print(f'Player 2: {marker[1]}')

    # Randomly choose who goes first
    current_player = choose_first()
    print(f'\nPlayer {current_player} goes first...')

    # Game loop
    while True:
        print('\n'*5)
        mark = marker[current_player-1]
        print(f"Player {current_player}'s turn; Marker-{mark}:\n")
        display_board(board)
        position = player_choice(board)
        place_marker(board, mark, position)
        display_board(board)

        if win_check(board, mark):
            print('\nCongratulations!!!')
            print(f"Player {current_player} wins!\n")
            break

        if full_board_check(board):
            print("\nIt's a draw!")
            break

        # Update current player
        current_player = 2 if current_player == 1 else 1

    if not replay():
        break
