from models.State import State
from logic.terminal import is_terminal, count_disks
from logic.actions import get_actions, PLAYER1, PLAYER2
from logic.evaluation import choose_best_action, evaluate
from logic.result import result

def heuristic_game():
    state = State.initial_state()
    while not is_terminal(state):
        actions = get_actions(state)
        if not actions:
            opponent = PLAYER1 if state.current_player == PLAYER2 else PLAYER2
            state = State(state.board, opponent)
            continue
        action = choose_best_action(state)
        state = result(state, action)
    print(f"Final state")
    state.display()
    print(f"Evaluation: {evaluate(state)}")
    payer1_disks, payer2_disks = count_disks(state)
    print(f"Player 1: {payer1_disks} disks, Player 2: {payer2_disks} disks, Total: "
          f"{payer1_disks+payer2_disks} disks")