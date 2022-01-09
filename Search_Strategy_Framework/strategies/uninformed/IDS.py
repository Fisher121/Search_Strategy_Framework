from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class IDS(BaseUninformedStrategyClass):
    solution = {}

    def IsFinal(self, state):
        pass

    def run(self, problem):
        self.problem = problem
        return self.IDS()

    def IDS(self):
        for depth in range(0, self.problem.number_of_states):
            parent = {}
            visited = [self.problem.initial_state]
            if self.DFS(self.problem.initial_state, self.problem.final_state, depth, parent, visited):
                return self.RestorePath(self.solution)
        return None

    def DFS(self, root, goal, depth, parent, visited):
        if root == goal:
            if not self.solution:
                self.solution = parent.copy()
            return True
        if depth == 0:
            return False
        for neighbor in self.problem.GenerateNeighbors(root):
            if neighbor not in visited:
                temp_parent = parent.copy()
                temp_parent[neighbor] = root
                visited.append(neighbor)
                if self.DFS(neighbor, goal, depth-1, temp_parent, visited):
                    parent = temp_parent
                    return True
        return False

    def RestorePath(self, parent):
        root = self.problem.final_state
        path = [self.problem.final_state]
        while parent[root] in parent:
            path.append(parent[root])
            root = parent[root]
        path.append(parent[root])
        return path