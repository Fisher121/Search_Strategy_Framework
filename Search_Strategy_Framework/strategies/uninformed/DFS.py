from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class DFS(BaseUninformedStrategyClass):
    results = []

    def IsFinal(self, state):
        if state == self.problem.final_state:
            return True

    def run(self, problem):
        self.problem = problem
        visited = [problem.initial_state]
        stack = [problem.initial_state]
        self.DFS(problem.initial_state, visited, stack)
        min_len = 10000000000
        min_state_list = []
        for state_list in self.results:
            if len(state_list) < min_len:
                min_len = len(state_list)
                min_state_list = state_list
        return min_state_list

    def DFS(self, start, visited, stack):
        if self.IsFinal(start):
            self.results.append(stack)
            return True
        visited.append(start)
        for neighbor in self.problem.GenerateNeighbors(start):
            if neighbor not in visited:
                temp_visited = visited.copy()
                temp_visited.append(neighbor)
                temp_stack = stack.copy()
                temp_stack.append(neighbor)
                self.DFS(neighbor, temp_visited.copy(), temp_stack)
