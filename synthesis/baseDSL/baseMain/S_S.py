from synthesis.baseDSL.baseMain.S import S, ChildS
from synthesis.baseDSL.baseMain.node import Node

from rts import PhysicalGameState
from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState

class S_S(ChildS,Node):
    
    def __init__(self):
        self._sLeft = S()
        self._sRight = S()
        
    def __init__(self, sL : S, sR : S):
        self._sLeft = sL
        self._sRight = sR
        
    def translate(self) -> str:
        return self._sLeft.translate()+" "+self._sRight.translate()
    
    def translate2(self) -> str:
        return self._sLeft.translate2()+"|"+self._sRight.translate2()
   
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs+ self._sLeft.translateIndentation(n_tab)+"\n"+self._sRight.translateIndentation(n_tab)
            
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        self._sLeft.interpret(gs, player, u, automata)
        self._sRight.interpret(gs, player, u, automata)
   
   
   