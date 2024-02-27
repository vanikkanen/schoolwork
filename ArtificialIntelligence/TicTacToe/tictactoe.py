"""
Tic Tac Toe Player
"""
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

    # check for initial state
    if board == initial_state():
        return X

    # count the done actions
    x_actions = 0
    o_actions = 0
    for row in board:
        for col in row:
            if col == X:
                x_actions += 1
            elif col == O:
                o_actions += 1

    # return the player with less amount of actions
    if x_actions > o_actions:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise ValueError("Not possible action")

    # do the action to the new_board and return it
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking rows and columns
    for i in range(3):
        # check row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        # check col
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # no winners found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return actions(board) == set() or winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action


def value(board):
    if terminal(board):
        return utility(board), None
    elif player(board) == X:
        return max_value(board)
    else:
        return min_value(board)


def max_value(board):

    if terminal(board):
        return utility(board), None

    v = float("-inf")
    best_action = None
    for action in actions(board):
        new_v, _ = value(result(board, action))
        result_v = max(v, new_v)
        if result_v > v:
            v = result_v
            best_action = action
    return v, best_action


def min_value(board):

    if terminal(board):
        return utility(board), None

    v = float("inf")
    best_action = None
    for action in actions(board):
        new_v, _ = value(result(board, action))
        result_v = min(v, new_v)
        if result_v < v:
            v = result_v
            best_action = action
    return v, best_action
