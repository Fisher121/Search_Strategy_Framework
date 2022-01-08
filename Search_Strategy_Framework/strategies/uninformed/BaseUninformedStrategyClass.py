from abc import ABC, abstractmethod


class BaseUninformedStrategyClass(ABC):
    def __init__(self):
        self.problem = None

    @abstractmethod
    def IsFinal(self, state):
        pass

    @abstractmethod
    def run(self, problem):
        pass


