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
    xnum=0
    onum=0
    for row in board:
        for column in row:
            if column == "X":
                xnum+=1
            elif column == "O":
                onum+=1
    if xnum > onum:
        return "O"
    return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                res.add((i, j))
    return res



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    validActions = actions(board)
    if action not in validActions:
        raise NameError("Move Invalid")
    i,j = action
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal Check
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]

    
    # Vertical Check
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] and  board[0][col]  == board[2][col] :
            return board[0][col]

    # Left Diagonal
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Right Diagonal
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for column in row:
            if column is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #if terminal state, return value
    if terminal(board):
        return None
    pl = player(board)
    # if Max player
    if pl == X:
        bestAction = None
        bestScore = -math.inf
        for action in actions(board):
            score = minValue(result(board,action))
            if score > bestScore:
                bestScore = score
                bestAction = action
        return bestAction
    else:
        bestAction = None
        bestScore = math.inf
        for action in actions(board):
            score = maxValue(result(board,action))
            if score < bestScore:
                bestScore = score
                bestAction = action
        return bestAction


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v,maxValue(result(board, action)))
    return v
