from models.State import State
from logic.actions import get_actions, PLAYER1, PLAYER2

def is_terminal(state: State) -> bool:
    opponent = PLAYER1 if state.current_player == PLAYER2 else PLAYER2
    opponent_state = State(state.board, opponent)

    return not get_actions(state) and not get_actions(opponent_state)

def count_disks(state: State) -> tuple[int, int]:
    player1 = 0
    player2 = 0
    for row in state.board:
        for val in row:
            if val == PLAYER1:
                player1 += 1
            if val == PLAYER2:
                player2 += 1
    return player1, player2