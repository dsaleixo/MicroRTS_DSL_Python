from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player


class Attack(ChildC,Node):
    
    def __init__(self) -> None:
        self._op =None
        
    def __init__(self,op :OpponentPolicy) -> None:
        self._op =op 
        
    
    def translate(self) -> str:
        return "u.attack("+self._op.getValue()+")"
    
    def translate2(self) -> str:
        return "u.attack(|"+self._op.getValue()+"|)"
    
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs +"u.attack("+self._op.getValue()+")"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        p = gs.getPlayer(player)
        if not u.getType().canAttack:
            return 
	    
        if   u.getPlayer() == player  and automata._core.getAbstractAction(u)==None :
           
            target = self._op.getUnit(gs, p, u, automata)
         
            automata._core.attack(u, target)
         
	
   
        
