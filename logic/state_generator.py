import random
from models.State import State, PLAYER1, PLAYER2
from logic.terminal import is_terminal, count_disks
from logic.result import result
from logic.actions import get_actions

def generate_state(num: int) -> State:
    if num < 4:
        raise ValueError("Number of disks must be at least 4")
    state = State.initial_state()
    num_of_disks = count_disks(state)
    total_disks = num_of_disks[0] + num_of_disks[1]

    while total_disks < num and not is_terminal(state):
        actions = get_actions(state)
        if not actions:
            opponent = PLAYER1 if state.current_player == PLAYER2 else PLAYER2
            state = State(state.board, opponent)
            continue
        action = random.choice(actions)
        state = result(state, action)
        num_of_disks = count_disks(state)
        total_disks = num_of_disks[0] + num_of_disks[1]
    return state