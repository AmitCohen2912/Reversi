from models.State import State
from logic.terminal import is_terminal
from logic.actions import get_actions, PLAYER1, PLAYER2
from logic.result import result

def methodical(num_states_to_display: int):
    if num_states_to_display < 0:
        raise ValueError("Number of states to display must be at least 0")
    state = State.initial_state()
    displayed_states = 1

    if num_states_to_display > 0:
        state.display()
        print()

    while not is_terminal(state):
        actions = get_actions(state)
        if not actions:
            opponent = PLAYER1 if state.current_player == PLAYER2 else PLAYER2
            state = State(state.board, opponent)
            continue
        action = actions[0]

        state = result(state, action)
        if displayed_states < num_states_to_display:
            state.display()
            print()
            displayed_states += 1
    print("Final state")
    state.display()