
class Problem:

    def __init__(self, state, initial_state):
        self.state = state
        self.initial_state = initial_state

    def is_goal(self):
        return self.state.cube.is_correct()
