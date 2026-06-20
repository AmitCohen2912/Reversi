import sys
from cli.display_all_actions import display_all_actions
from cli.methodical import methodical
from logic.utility import utility
from logic.actions import PLAYER1, PLAYER2, EMPTY, BOARD_SIZE
from models.State import State
from logic.state_generator import generate_state
from logic.terminal import count_disks
from logic.evaluation import evaluate, choose_best_action
from logic.actions import get_actions
from cli.heuristic_game import heuristic_game

# state1 = generate_state(10)
# state2 = generate_state(20)
#
# state1.display()
# player1_disks, player2_disks = count_disks(state1)
# best_action = choose_best_action(state1)
# print(get_actions(state1))
# print(f"Player 1: {player1_disks} disks. Player 2: {player2_disks} disks. Evaluation: {evaluate(state1)}."
#       f"Best action: {best_action}")
#
# print('\n\n')
# state2.display()
# player1_disks, player2_disks = count_disks(state2)
# best_action = choose_best_action(state2)
# print(get_actions(state2))
# print(f"Player 1: {player1_disks} disks. Player 2: {player2_disks} disks. Evaluation: {evaluate(state2)}."
#       f"Best action: {best_action}")


if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage:")
        print("python3 Reversi.py --displayAllActions <num>")
        print("python3 Reversi.py --methodical <num>")
        print("python3 Reversi.py --heuristic")
        sys.exit(1)
    command = sys.argv[1]
    if command == "--heuristic":
        heuristic_game()
        sys.exit(0)
    try:
        num = int(sys.argv[2])
    except ValueError:
        print("Second argument must be an integer.")
        sys.exit(1)

    if command == "--displayAllActions":
        try:
            display_all_actions(num)
        except ValueError as e:
            print(e)

    elif command == "--methodical":
        try:
            methodical(num)
        except ValueError as e:
            print(e)
    else:
        print("Invalid command")