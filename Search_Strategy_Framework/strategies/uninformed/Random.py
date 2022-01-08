from random import seed, random

from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class Random(BaseUninformedStrategyClass):
    def IsFinal(self, state):
        if state == self.problem.final_state:
            return True

    def run(self, problem):
        self.problem = problem
        return self.Random()

    def IsValid(self,path):
        if len(path) < 2:
            return False
        for i in range(1,len(path)):
            if path[i-1] not in self.problem.GenerateNeighbors(path[i]):
                return False
        return True

    def Random(self):
        path = []
        states = self.problem.GetAllStates()
        states.remove(self.problem.initial_state)
        states.remove(self.problem.final_state)
        while not self.IsValid(path):
            path = [self.problem.initial_state]
            number_of_nodes = int(random()*100000) % len(states)
            temp_states = states.copy()
            for i in range(0, number_of_nodes):
                state = temp_states[(int(random() * 10000) % number_of_nodes)]
                path.append(state)
                temp_states.remove(state)
                number_of_nodes -=1
            path.append(self.problem.final_state)

        return path

