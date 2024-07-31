"""
Tic Tac Toe Player
"""

import math

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


def player(board) -> str:
    """
    Returns player who has the next turn on a board.
    """
    
    
    # In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    # Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    raise NotImplementedError


def actions(board) -> tuple:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # Return any move if terminal board provided
    # Each action is a tuple (x, y) legal move
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # If action not valid raise an error.
    # Make a deep copy of the board so that minimax doesn't changes the board.
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Should return x if x has won and o if o has won
    # If tie return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # Shoud return True if someone won or the game is over
    # Otherwise return false
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    # Returns 1 if X won. returns -1 if O wins, and return 0 if draw
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    # should return (i, j) which is one of the allowable actions, & if multiple moves are optimal return any
    # if Terminal board return None
    raise NotImplementedError
