from abc import ABC

from problems.Problem import Problem


class ClassicGraphSearchProblem(Problem):
    initial_state = 0
    final_state = 5
    neighbors = [
        [1, 6],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 7],
        [0, 7],
        [6, 5], ]

    def GenerateNeighbors(self, state):
        return self.neighbors[state]

    def GetAllStates(self):
        return [0, 1, 2, 3, 4, 5, 6, 7]
