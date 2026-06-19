from models.State import State
from logic.actions import get_actions, PLAYER1, PLAYER2

def is_terminal(state: State) -> bool:
    opponent = PLAYER1 if state.current_player == PLAYER2 else PLAYER2
    opponent_state = State(state.board, opponent)

    return not get_actions(state) and not get_actions(opponent_state)