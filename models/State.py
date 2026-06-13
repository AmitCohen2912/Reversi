from dataclasses import dataclass

EMPTY = '-'
PLAYER1 = 'x'
PLAYER2 = 'o'
BOARD_SIZE = 8

@dataclass
class State:
    board: list[list[str]]
    current_player: str

    @staticmethod
    def initial_state() -> "State":
        board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        board[3][3] = PLAYER1
        board[3][4] = PLAYER2
        board[4][3] = PLAYER2
        board[4][4] = PLAYER1
        return State(board, PLAYER1)

    def display(self):
        for row in self.board:
            for i, value in enumerate(row):
                if i == BOARD_SIZE - 1:
                    print(value)
                else:
                    print(value, end=' ')