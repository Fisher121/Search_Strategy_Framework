from strategies.uninformed.BaseUninformedStrategyClass import BaseUninformedStrategyClass


class BDS(BaseUninformedStrategyClass):
    def IsFinal(self, state):
        pass

    def run(self, problem):
        self.problem = problem
        return self.BDS()

    def BDS(self):
        startq = [self.problem.initial_state]
        endq = [self.problem.final_state]
        parent = {}
        visited = {}
        visited[self.problem.initial_state] = 1
        visited[self.problem.final_state] = 2
        while startq and endq:
            stv = startq.pop(0)
            start_neighbors = self.problem.GenerateNeighbors(stv)
            for v in start_neighbors:
                if v not in visited:
                    visited[v] = 1
                    startq.append(v)
                    parent[v] = stv
                if visited[v] == 2:
                    return self.RestorePath(v, stv, parent)

            etv = endq.pop(0)
            end_neighbors = self.problem.GenerateNeighbors(etv)
            for v in end_neighbors:
                if v not in visited:
                    visited[v] = 2
                    endq.append(v)
                    parent[v] = etv
                if visited[v] == 1:
                    return self.RestorePath(v, etv, parent)

    def RestorePath(self,intersection1, intersection2, parentarray):
        first_half = [intersection1]
        while parentarray[intersection1] in parentarray:
            first_half.insert(0, parentarray[intersection1])
            intersection1 = parentarray[intersection1]
        first_half.insert(0,parentarray[intersection1])

        second_half = [intersection2]
        while parentarray[intersection1] in parentarray:
            second_half.append(parentarray[intersection2])
            intersection2 = parentarray[intersection2]
        second_half.append(parentarray[intersection2])
        first_half.extend(second_half)
        return first_half
