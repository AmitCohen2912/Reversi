from models.State import State
from logic.terminal import count_disks
def utility(state: State) -> float:
    player1_disks, player2_disks = count_disks(state)
    return (player1_disks - player2_disks) / (player1_disks + player2_disks)