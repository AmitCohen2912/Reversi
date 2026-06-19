from models.State import State
from logic.actions import get_actions
from logic.result import result
from logic.terminal import is_terminal
from models.State import State, EMPTY, PLAYER1, PLAYER2, BOARD_SIZE

# state = State.initial_state()
# state.display()
# print(is_terminal(state))

# print(get_actions(state))
#
# result(state, get_actions(state)[0]).display()


# board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
# board[2][3] = PLAYER1
# board[3][3] = PLAYER1
# board[3][4] = PLAYER2
# board[3][5] = PLAYER2
# board[4][3] = PLAYER2
# board[4][4] = PLAYER2
# board[5][2] = PLAYER2
#
# state = State(board, PLAYER1)
# state.display()
#
# print(get_actions(state))
#
# result(state, get_actions(state)[0]).display()

# board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
# board[1][3] = PLAYER1
# board[2][3] = PLAYER2
#
# board[3][1] = PLAYER1
# board[3][2] = PLAYER2
#
# board[5][3] = PLAYER1
# board[4][3] = PLAYER2
#
# board[3][5] = PLAYER1
# board[3][4] = PLAYER2
#
# state = State(board, PLAYER1)
#
# state.display()
#
# print(get_actions(state))
#
# result(state, get_actions(state)[0]).display()

# board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
# board[0][3] = PLAYER1
#
# board[0][1] = PLAYER2
# board[0][2] = PLAYER2
#
# state = State(board, PLAYER1)
# state.display()
# print(get_actions(state))
#
# result(state, get_actions(state)[0]).display()

# board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
# board[0][0] = PLAYER1
#
# board[0][1] = PLAYER2
# board[0][2] = PLAYER2
# board[0][3] = PLAYER2
#
# state = State(board, PLAYER1)
# state.display()
#
# print(get_actions(state))
#
# result(state, get_actions(state)[0]).display()


# board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
# board[3][3] = PLAYER1
#
# board[1][1] = PLAYER2
# board[2][2] = PLAYER2
#
# state = State(board, PLAYER1)
#
# state.display()
# print(get_actions(state))
#
# result(state,get_actions(state)[0]).display()

# board = [[PLAYER1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
#
# state = State(board, PLAYER1)
#
# state.display()
# print(is_terminal(state))

# board = [[EMPTY for _ in range(BOARD_SIZE)]
#          for _ in range(BOARD_SIZE)]
#
# state = State(board, PLAYER1)
#
# state.display()
# print(is_terminal(state))

# board = [[PLAYER1 for _ in range(BOARD_SIZE)]
#          for _ in range(BOARD_SIZE)]
#
# board[0][0] = EMPTY
# board[0][1] = PLAYER2
#
# state = State(board, PLAYER1)
#
# state.display()
# print(get_actions(state))
# print(is_terminal(state))

# board = [[PLAYER1 for _ in range(BOARD_SIZE)]
#          for _ in range(BOARD_SIZE)]
#
# board[3][3] = EMPTY
# board[3][4] = PLAYER2
# board[3][5] = PLAYER2
#
# state = State(board, PLAYER2)
#
# state.display()
# print("Current:", get_actions(state))
# print("Terminal:", is_terminal(state))

# board = [[PLAYER1 for _ in range(BOARD_SIZE)]
#          for _ in range(BOARD_SIZE)]
#
# board[0][0] = EMPTY
# board[7][7] = EMPTY
#
# state = State(board, PLAYER1)
#
# state.display()
# print(is_terminal(state))