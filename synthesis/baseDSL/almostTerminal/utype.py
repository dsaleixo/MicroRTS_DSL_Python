from synthesis.baseDSL.almostTerminal.almostTerminal import AlmostTerminal

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player



class Utype(AlmostTerminal):
    
    def __init__(self) -> None:
        self._type = None
        
    def __init__(self,utype) -> None:
        self._type = utype
    
    
    def rules(self):#->list[str]:
        return ["Base",
		        "Barracks",
                "Worker",
                "Ranged",
                "Light",
		        "Heavy"]
    
   
    
    def setValue(self, s :str)->None:
        self._type=s
    
    def getValue(self)->str:
        return self._type
	
    def translate(self)->str:
        return self._type