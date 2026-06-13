from models.State import State, EMPTY, PLAYER1, PLAYER2, BOARD_SIZE

DIRECTIONS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

def is_legal_move(state: State, i: int, j: int) -> bool: # (3,5), x
    if state.board[i][j] != EMPTY:
        return False

    opponent = PLAYER1 if state.current_player == PLAYER2 else PLAYER2

    for dr, dc in DIRECTIONS:
        if 0 <= i + dr < BOARD_SIZE and 0 <= j + dc < BOARD_SIZE:
            if state.board[i + dr][j + dc] == opponent:
                current_row = i + dr
                current_col = j + dc
                while 0 <= current_row < BOARD_SIZE and 0 <= current_col < BOARD_SIZE:
                    if state.board[current_row][current_col] == opponent:
                        current_row = current_row + dr
                        current_col = current_col + dc
                    elif state.board[current_row][current_col] == state.current_player:
                        return True
                    else:
                        break
    return False

def get_actions(state: State) -> list[tuple[int, int]]:
    actions = []
    for i, row in enumerate(state.board):
        for j, val in enumerate(row):
            if is_legal_move(state, i, j):
                actions.append((i, j))
    return actions