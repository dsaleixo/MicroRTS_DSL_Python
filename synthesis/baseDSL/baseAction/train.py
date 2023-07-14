from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.almostTerminal.utype import Utype
from synthesis.baseDSL.almostTerminal.direction import Direction
from synthesis.baseDSL.almostTerminal.n import N

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player

from rts import UnitAction
import java


class Train(ChildC,Node):
    
    def __init__(self) -> None:
        self._type =None
        self._n = None
        self._direc = None
        
    def __init__(self,utype : Utype, n : N, direc : Direction) -> None:
        self._type =utype
        self._n = n
        self._direc = direc
        
    
    def translate(self) -> str:
        return "u.train("+self._type.getValue()+","+self._direc.getValue()+","+self._n.getValue()+")"
    
    def translate2(self) -> str:
        return "u.train(|"+self._type.getValue()+"|"+self._direc.getValue()+"|"+self._n.getValue()+"|)"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs + "u.train("+self._type.getValue()+","+self._direc.getValue()+","+self._n.getValue()+")"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        uType = automata._utt.getUnitType(self._type.getValue())
		
   
        if  u.getPlayer() == player and u.getType().name.equals("Base")  and uType.name=="Worker" and automata._core.getAbstractAction(u)==None :
                            
            
            if automata.resource >= uType.cost and automata.countTrain(uType.name,player,gs) < int(self._n.getValue())  :
                automata._core.train(u, uType,self._direc.converte(gs,player,u))
                automata.resource -= uType.cost
               
	
        if  u.getPlayer() == player and u.getType().name == "Barracks"  and \
                            (uType.name=="Light"  or uType.name.equals("Heavy")  or uType.name=="Ranged") and automata._core.getAbstractAction(u)==None :
            
            if automata.resource >= uType.cost and automata.countTrain(uType.name,player,gs) < int(self._n.getValue())  :                                     
                automata._core.train(u, uType,self._direc.converte(gs,player,u))
                automata.resource -= uType.cost
	     
        
	
   
        
