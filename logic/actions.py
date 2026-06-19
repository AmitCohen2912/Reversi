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

def get_flippable_positions(board: list[list[str]], row: int, col: int, current_player: str) -> list[tuple[int, int]]:
    opponent = PLAYER1 if current_player == PLAYER2 else PLAYER2
    positions = []
    for dr, dc in DIRECTIONS:
        if 0 <= row + dr < BOARD_SIZE and 0 <= col + dc < BOARD_SIZE:
            if board[row + dr][col + dc] == opponent:
                current_row = row + dr
                current_col = col + dc
                while 0 <= current_row < BOARD_SIZE and 0 <= current_col < BOARD_SIZE:
                    if board[current_row][current_col] == opponent:
                        current_row = current_row + dr
                        current_col = current_col + dc
                    elif board[current_row][current_col] == EMPTY:
                        break
                    else:
                        current_row = row + dr
                        current_col = col + dc
                        while board[current_row][current_col] == opponent:
                            positions.append((current_row, current_col))
                            current_row = current_row + dr
                            current_col = current_col + dc
                        break
    return positions

def is_legal_move(state: State, i: int, j: int) -> bool:
    if state.board[i][j] != EMPTY:
        return False

    return len(get_flippable_positions(state.board, i, j, state.current_player)) > 0

def get_actions(state: State) -> list[tuple[int, int]]:
    actions = []
    for i, row in enumerate(state.board):
        for j, val in enumerate(row):
            if is_legal_move(state, i, j):
                actions.append((i, j))
    return actions