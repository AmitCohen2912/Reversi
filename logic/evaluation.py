from math import inf

from models.State import State
from logic.terminal import count_disks
from logic.actions import get_actions, PLAYER1, PLAYER2
from logic.result import result

def evaluate(state: State) -> float:
    player1_disks, player2_disks = count_disks(state)

    return (player1_disks - player2_disks) / (player1_disks + player2_disks)

def choose_best_action(state: State) -> tuple[int, int] | None:
    actions = get_actions(state)
    if not actions:
        return None
    best_action = None
    if state.current_player == PLAYER1:
        best_value = -inf
    else:
        best_value = inf

    for action in actions:
        new_state = result(state, action)
        new_value = evaluate(new_state)

        if state.current_player == PLAYER1 and new_value > best_value:
            best_action = action
            best_value = new_value
        elif state.current_player == PLAYER2 and new_value < best_value:
            best_action = action
            best_value = new_value
    return best_action