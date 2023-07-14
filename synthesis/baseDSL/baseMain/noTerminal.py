
from abc import ABC, abstractmethod
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.util.factory import Factory

class NoTerminal(ABC):
    
    @abstractmethod
    def getRule(self)->Node:
        pass
    
    @abstractmethod
    def setRule(self, node : Node)->None:
        pass
    
    @abstractmethod
    def rules(f: Factory) :#->list[Node]
        pass