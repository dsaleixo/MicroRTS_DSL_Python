from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player
from synthesis.baseDSL.util.factory import Factory


class Idle(ChildC,Node):
    
    def __init__(self) -> None:
        self._used = False
        pass
        
    
        
    
    def translate(self) -> str:
        return "u.idle()"
    
    def translate2(self) -> str:
        return "u.idle()"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs +"u.idle()"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        
        pgs = gs.getPhysicalGameState()
		
        if u.getPlayer()==player  and automata._memory._freeUnit[u.getID()]  and u.getType().canAttack:
            for  target in pgs.getUnits():
                if target.getPlayer()!=-1 and target.getPlayer()!=u.getPlayer():
                    dx = target.getX()-u.getX()
                    dy = target.getY()-u.getY()
                    d = (dx*dx+dy*dy)**0.5
                    if d<=u.getAttackRange() :
                        self._used = True
                        automata._core.idle(u)
                        automata._memory._freeUnit[u.getID()] = False
                        
                        
    def load(self, l : list[str], f :Factory):
        pass
	

    def save(self, l : list[str]):
        l.append("Idle")
        
    def clone(self, f : Factory) -> Node:
        return f.build_Idle()
    
    def resert(self, f : Factory) -> None:
        self._used = False
        
    def clear(self,father:Node, f : Factory) -> Node:
        return self._used
	
