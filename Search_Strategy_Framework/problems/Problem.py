from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def GenerateNeighbors(self, state):
        pass

    @abstractmethod
    def GetAllStates(self):
        pass
