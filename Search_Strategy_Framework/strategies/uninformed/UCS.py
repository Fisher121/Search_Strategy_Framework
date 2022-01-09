from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class UCS(BaseUninformedStrategyClass):
    def IsFinal(self, state):
        if state == self.problem.final_state:
            return True

    def run(self, problem):
        self.problem = problem
        return self.UCS()

    def ComputeCosts(self, arr):
        if arr is None:
            return 100000000
        state_array = arr.copy()
        total = 0
        prev_state = state_array.pop(0)
        for state in state_array:
            c = self.problem.GetCost(prev_state, state)
            if c != 0:
                total += c
            else:
                total += 1000000

            prev_state = state
        return total

    def UCS(self):
        node = self.problem.initial_state
        frontier = [(node, [node])]
        visited = {node : 0}
        solution = None
        while frontier and self.ComputeCosts(frontier[0][1]) < self.ComputeCosts(solution):
            parent = frontier.pop(0)
            for neighbor in self.problem.GenerateNeighbors(parent[0]):
                if neighbor not in visited or self.ComputeCosts(parent[1] + [neighbor]) < visited[neighbor]:
                    if not self.IsFinal(neighbor):
                        visited[neighbor] = self.ComputeCosts(parent[1] + [neighbor])
                        frontier.append((neighbor, parent[1] + [neighbor]))
                    if self.IsFinal(neighbor) and self.ComputeCosts(parent[1] + [neighbor]) < self.ComputeCosts(solution):
                        solution = parent[1] + [neighbor]
        return solution
