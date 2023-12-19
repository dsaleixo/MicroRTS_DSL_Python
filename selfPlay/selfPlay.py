from abc import ABC, abstractmethod

class SelfPlay(ABC):
    @abstractmethod
    def update(self, prog):
        pass
    
    @abstractmethod
    def getN(self):
        pass
    
    @abstractmethod
    def evaluate(self, prog):
        pass
    
    @abstractmethod
    def getBest(self):
        pass
    
    @abstractmethod
    def getIndividual(self):
        pass
    
    @abstractmethod
    def stoppingCriterion(score):
        pass