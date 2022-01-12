from abc import ABC

from problems.Problem import Problem


class Grid(Problem):
    initial_state = (0, 0)
    goal = (5, 5)
    number_of_states = 8
    actions = ([-1, 0], [0, -1], [1, 0], [0, 1])

    world = [
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 0],
    ]

    def GetCost(self,state1,state2):
        return self.costarray[state1][state2]

    def GetAllStates(self):
        return [0, 1, 2, 3, 4, 5, 6, 7]

    def GenerateNeighbors(self, state):
        pass
