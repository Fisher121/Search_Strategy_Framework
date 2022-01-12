from strategies.informed.BaseInformedStrategyClass import BaseInformedStrategyClass


class A_Star(BaseInformedStrategyClass):

    def isFinal(self):
        pass

    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.cost = 0

    def run(self, problem):
        self.problem = problem

    def __lt__(self, other):
        return self.cost < other.cost

    def score(self, start, current, final):
        g = abs(current[0] - start[0]) + abs(current[1] - start[1])
        h = abs(current[0] - final[0]) + abs(current[1] - final[1])
        return g + h

    def good_neighbor(self,queue,neighbour):
        for node in queue:
            if(neighbour == node and self.neighbor.f >= node.f):
                return False
        return True

    def a_star(self, space, start, final):
        queue = []
        visited = []
        queue.append(start)
        while len(queue) > 0:
            queue.sort()
            current_node = queue.pop(0)
            visited.append(current_node)
            if current_node == final:
                path = []
                while current_node is not start:
                    path.append(current_node)
                    current_node = current_node.parrent
                    return path[::-1]

            if self.good_neighbor(queue, self.neighbour):
                queue.append(self.neighbor)

