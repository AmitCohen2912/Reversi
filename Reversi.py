import sys
from cli.display_all_actions import display_all_actions
from cli.methodical import methodical

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage:")
        print("python3 Reversi.py --displayAllActions <num>")
        print("python3 Reversi.py --methodical <num>")
        sys.exit(1)
    command = sys.argv[1]
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