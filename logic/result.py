from copy import deepcopy

from logic.actions import get_flippable_positions
from models.State import State, PLAYER1, PLAYER2

def result(state: State, action: tuple[int, int]) -> State:
    new_board = deepcopy(state.board)
    new_board[action[0]][action[1]] = state.current_player

    positions = get_flippable_positions(new_board, action[0], action[1], state.current_player)
    for r, c in positions:
        new_board[r][c] = state.current_player

    return State(new_board, PLAYER1 if state.current_player == PLAYER2 else PLAYER2)