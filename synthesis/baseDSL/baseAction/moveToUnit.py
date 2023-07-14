from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer
from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player



class MoveToUnit(ChildC,Node):
    
    def __init__(self) -> None:
        self._op =None
        self._tp = None
        
    def __init__(self,op :OpponentPolicy, tp :TargetPlayer) -> None:
        self._op =op 
        self._tp = tp
        
    
    def translate(self) -> str:
        return "u.moveToUnit("+self._tp.getValue()+","+self._op.getValue()+")"
    
    def translate2(self) -> str:
        return "u.moveToUnit(|"+self._tp.getValue()+"|"+self._op.getValue()+"|)"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs +"u.moveToUnit("+self._tp.getValue(),",",self._op.getValue()+")"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        jogador =-1
        if self._tp.getValue() =="Ally":jogador=1-player
        else: jogador = player
        p = gs.getPlayer(jogador)
        pgs = gs.getPhysicalGameState() 
		
        if u.getType().canMove and u.getPlayer()==player and \
                            automata._core.getAbstractAction(u)==None :
            u2 = self._op.getUnit(gs, p, u, automata)
            if u2!=None :
                pf =  automata._core.pf   
                move = pf.findPathToPositionInRange2(u, u2.getX() + u2.getY() * pgs.getWidth(),1, gs )
                if move!=None:
                    automata._core.move(u, move.m_a, move.m_b)
			
         
	
   
        
