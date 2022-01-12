from strategies.informed.BaseInformedStrategyClass import BaseInformedStrategyClass


class GBF(BaseInformedStrategyClass):
    queue = []
    visited = []
    actions = ([-1, 0], [0, -1], [1, 0], [0, 1])

    def isFinal(self):
        pass

    def run(self, problem):
        self.problem = problem
        return self.BFS(self.problem.initial_state, self.problem.goal)

    def __lt__(self, other):
        return self.cost < other.cost

    def score(self, current, target):
        return abs(current[0] - target[0]) + (current[1] - target[1])

    def get_neighbours(self, node):
        neighbours = []
        for action in self.actions:
            x = node[0] + action[1]
            y = node[1] + action[0]
            neighbours.append([x, y])
        return neighbours

    def getPath(self, node):
        current_node = node
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = current_node
        return path

    def BFS(self, start, target):
        queue = []
        visited = []
        queue.append(start)
        while len(queue) > 0:
            queue.sort()
            current_node = queue.pop(0)
            if current_node == target:
                return self.getPath(current_node)
            visited.append(current_node)
            for neighbour in self.get_neighbours(current_node):
                if neighbour in visited:
                    continue
                if neighbour not in queue:
                    queue.append(neighbour)
                    better_node = queue.pop(queue.index(neighbour))
                    if self.score(neighbour, target) < self.score(better_node, target):
                        queue.append(neighbour)
                    else:
                        queue.append(better_node)
