from abc import ABC, abstractmethod

from synthesis.baseDSL.baseMain.node import Node

class Mutation(ABC):
    @abstractmethod
    def getMutations(self,prog, n_mutation) -> list[Node]:
        pass
    
    