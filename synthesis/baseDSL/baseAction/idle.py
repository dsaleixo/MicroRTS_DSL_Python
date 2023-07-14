from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player


class Idle(ChildC,Node):
    
    def __init__(self) -> None:
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
		
        if u.getPlayer()==player  and automata._core.getAbstractAction(u)==None and u.getType().canAttack:
            for  target in pgs.getUnits():
                if target.getPlayer()!=-1 and target.getPlayer()!=u.getPlayer():
                    dx = target.getX()-u.getX()
                    dy = target.getY()-u.getY()
                    d = (dx*dx+dy*dy)**0.5
                    if d<=u.getAttackRange() :
                        automata._core.idle(u)
