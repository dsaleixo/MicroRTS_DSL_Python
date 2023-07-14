from abc import ABC, abstractmethod
from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState



class Node(ABC):
    @abstractmethod
    def translate(self) -> str:
        pass
    
    @abstractmethod
    def  translateIndentation(self,n_tab:int) ->str:
        pass
    
    @abstractmethod
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        pass
	
    @classmethod
    def getName(cls)->str:
        return cls.__name__
        

	