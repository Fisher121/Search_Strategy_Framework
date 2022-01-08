from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class BFS(BaseUninformedStrategyClass):
    def IsFinal(self, state):
        if state == self.problem.final_state:
            return True

    def run(self, problem):
        self.problem = problem
        result = self.BFS(problem.initial_state)
        return self.RememberPath(result)

    def BFS(self, start):
        visited = [start]
        queue = [start]
        level = {start: 0}
        while queue:
            v = queue.pop(0)

            neighbors = self.problem.GenerateNeighbors(v)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)
                    level[neighbor] = level[v] +1

        return visited, level

    def RememberPath(self, result):
        visited = []
        levels = {}
        k = True
        counter = 0
        for v in result[0]:
            if k:
                visited.append(v)
                levels[v] = result[1][v]
                counter += 1
            if self.IsFinal(v):
                k = False

        path = [visited[counter - 1]]
        last_valid_neighbor = counter-1
        for i in range(counter - 2, -1, -1):
            r = visited[i]
            m = self.problem.GenerateNeighbors(visited[last_valid_neighbor])
            x=levels[visited[i]]
            k=levels[visited[last_valid_neighbor]]
            if visited[i] in self.problem.GenerateNeighbors(visited[last_valid_neighbor]):
                if levels[visited[i]] + 1 == levels[visited[last_valid_neighbor]]:
                    path.append(visited[i])
                    last_valid_neighbor = i
        return path
