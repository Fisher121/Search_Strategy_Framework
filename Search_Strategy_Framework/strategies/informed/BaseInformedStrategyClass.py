from abc import ABC, abstractmethod


class BaseInformedStrategyClass(ABC):
    @abstractmethod
    def run(self, scoreFunction):
        pass

    @abstractmethod
    def score(self, state1, state2):
        pass
