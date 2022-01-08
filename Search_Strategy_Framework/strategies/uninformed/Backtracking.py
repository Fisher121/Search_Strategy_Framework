from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class Backtracking(BaseUninformedStrategyClass):
    results = []

    def IsFinal(self, state):
        if state == self.problem.initial_state:
            return True

    def run(self, problem):
        self.results = []
        self.problem = problem
        self.BackTrack(problem.final_state, [])
        min_len = 10000000000
        min_state_list = []
        for state_list in self.results:
            if len(state_list) < min_len:
                min_len = len(state_list)
                min_state_list = state_list
        return min_state_list

    def BackTrack(self, state, state_list):
        if self.IsFinal(state):
            state_list.append(state)
            self.results.append(state_list)
            return True

        if state not in state_list:
            candidates = self.problem.GenerateNeighbors(state)
            for candidate in candidates:
                temp_state_list = state_list.copy()
                temp_state_list.append(state)
                self.BackTrack(candidate, temp_state_list)

