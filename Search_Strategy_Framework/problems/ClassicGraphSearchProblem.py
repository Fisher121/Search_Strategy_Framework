from abc import ABC

from problems.Problem import Problem


class ClassicGraphSearchProblem(Problem):
    initial_state = 0
    final_state = 5
    number_of_states = 8
    neighbors = [
        [1, 6],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 7],
        [0, 7],
        [6, 5], ]
    costarray = [
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 1, 10, 0],
    ]

    def GenerateNeighbors(self, state):
        return self.neighbors[state]

    def GetAllStates(self):
        return [0, 1, 2, 3, 4, 5, 6, 7]

    def GetCost(self,state1,state2):
        return self.costarray[state1][state2]