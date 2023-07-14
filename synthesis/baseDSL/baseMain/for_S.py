from synthesis.baseDSL.baseMain.S import S, ChildS
from synthesis.baseDSL.baseMain.node import Node

from rts import PhysicalGameState
from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState

class For_S(ChildS,Node):
    
    def __init__(self):
        self._s = S()
        
    def __init__(self, s : S):
        self._s = s
        
    def translate(self) -> str:
        return "for(Unit u){" +self._s.translate()+"}"
    
    def translate2(self) -> str:
        return "for(Unit u){|" +self._s.translate2()+"|}endFor"
   
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs+ "for(Unit u){\n" + \
            self._s.translateIndentation(n_tab+1)+"\n"+\
				tabs+"}"
            
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits():	
            if u2.getPlayer()==player and automata._core.getAbstractAction(u2)==None :
                self._s.interpret(gs, player,u2, automata)
   
   
   