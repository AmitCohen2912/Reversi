from models.State import State
from logic.actions import get_actions

state = State.initial_state()
state.display()

print(get_actions(state))