"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                x_count += 1
            elif cell == 'O':
                o_count += 1
    if (x_count - o_count == 0):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for x_index, row in enumerate(board):
        for y_index, cell in enumerate(row):
            if (cell is None):
                moves.add((x_index,y_index))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise Exception('move not allowed!')
    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player(board) #
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(len(board)):
        row = set([board[x][0],board[x][1],board[x][2]])
        if len(row) == 1 and board[x][0] is not None:
            return board[x][0]
    
    for y in range(len(board)):
        column = set([board[0][y],board[1][y],board[2][y]])
        if len(column) == 1 and board[0][y] is not None:
            return board[0][y]
    
    diagonol_1 = set([board[0][2],board[1][1],board[2][0]])
    diagonal_2 = set([board[0][0],board[1][1],board[2][2]])

    if (len(diagonol_1) == 1 and board[0][2] is not None):
        return board[0][2] 
    if (len(diagonal_2) == 1 and board[0][0] is not None):
        return board[0][0] 
    #if no winner return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board): #
        return None

    if player(board) == X:
        value = float('-inf')
        move = None

        for action in actions(board):
            min_v = min_value(result(board, action))
            if value < min_v:
                move = action
                value = min_v
        return move
    else:
        value = float('inf')
        move = None

        for action in actions(board):
            max_v = max_value(result(board, action))
            if value > max_v:
                move = action
                value = max_v
        return move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v

    ### buggy solution below
    """
    if player(board) == "X":
        max_value(board)
    else:
        print("min valueing")
        min_value(board)
    
    def max_value(board):
            # check if there is a winner or if there are no moves left
            if terminal(board):
                return utility(board)
            v = float('-inf')
            global move
            for action in actions(board):
                min_v = min_value(result(board,action))
                if v < min_v: #
                    move = action
                v = max(v, min_v) 
            return v


    def min_value(board):
            if terminal(board):
                return utility(board)
            v = float('inf')
            global move
            for action in actions(board):
                max_v = max_value(result(board,action))
                if v > max_v: #
                    move = action
                v = min(v, max_v) 
            return v
    return move
    """
    ###
