from synthesis.baseDSL.almostTerminal.almostTerminal import AlmostTerminal

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player



class N(AlmostTerminal):
    
    def __init__(self) -> None:
        self._n = None
        
    def __init__(self,n) -> None:
        self._n = n
    
    
    def rules(self):#->list[str]:
        return ["0",
		        "1",
		        "2",
		        "3",
		        "4",
                "5",
		        "6",
		        "7",
		        "8",
                "9",
                "10",
		        "15",
		        "20",
                "25",
		        "50",
		        "100"]
    
  
    
    def setValue(self, s :str)->None:
        self._n=s
    
    def getValue(self)->str:
        return self._n
	
    def translate(self)->str:
        return self._n