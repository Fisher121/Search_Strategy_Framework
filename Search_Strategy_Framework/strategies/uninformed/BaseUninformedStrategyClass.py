from abc import ABC, abstractmethod


class BaseUninformedStrategyClass(ABC):

    @abstractmethod
    def IsFinal(self, state):
        pass

    @abstractmethod
    def run(self):
        pass


