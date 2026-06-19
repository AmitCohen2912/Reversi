from logic.state_generator import generate_state
from logic.actions import get_actions, PLAYER1, PLAYER2
from logic.result import result
from logic.terminal import count_disks

def display_all_actions(num: int):
    state = generate_state(num)
    print("State 0")
    state.display()
    actions = get_actions(state)
    print()
    for i, action in enumerate(actions, start=1):
        print(f"State {i}, Player {1 if state.current_player == PLAYER1 else 2} moved, Action {action}")
        new_state = result(state, action)
        new_state.display()
        player1_disks, player2_disks = count_disks(new_state)
        total_disks = player1_disks + player2_disks
        print(f"Result - Player 1: {player1_disks} disks, Player 2: {player2_disks} disks, Total:"
              f" {total_disks} disks")
        if i < len(actions):
            print()