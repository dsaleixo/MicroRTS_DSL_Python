from synthesis.baseDSL.almostTerminal.almostTerminal import AlmostTerminal

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player



class TargetPlayer(AlmostTerminal):
    
    def __init__(self) -> None:
        self._tp = None
        
    def __init__(self,tp) -> None:
        self._tp = tp
    
    
    def rules(self):#->list[str]:
        return ["Ally",
		        "Enemy"]
    
   
    
    def setValue(self, s :str)->None:
        self._tp=s
    
    def getValue(self)->str:
        return self._tp
	
    def translate(self)->str:
        return self._tp