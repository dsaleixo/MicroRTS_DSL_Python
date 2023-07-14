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


class Build(ChildC,Node):
    
    def __init__(self) -> None:
        self._type =None
        self._n = None
        self._direc = None
        
    def __init__(self,utype : Utype, n : N, direc : Direction) -> None:
        self._type =utype
        self._n = n
        self._direc = direc
        
    
    def translate(self) -> str:
        return "u.build("+self._type.getValue()+","+self._direc.getValue()+","+self._n.getValue()+")"
    
    def translate2(self) -> str:
        return "u.build(|"+self._type+"|"+self._direc.getValue()+"|"+self._n.getValue()+"|)"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs + "u.build("+self._type.getValue()+","+self._direc.getValue()+","+self._n.getValue()+")"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        pgs = gs.getPhysicalGameState()
        p = gs.getPlayer(player)
        uType = automata._utt.getUnitType(self._type.getValue())
        
        if not (uType.name == "Barracks" or uType.name == "Base" or \
                automata._core.getAbstractAction(u)!=None):
            return
        
        if u.getPlayer() != player or \
                    u.getType().name != "Worker" or \
                    automata.resource < uType.cost or \
                    automata.countConstrution(uType.name,player,gs) >= int(self._n.getValue())   :
            return
        
        
        
        reservedPositions =  java.util.LinkedList()
	
      
        direction = self._direc.converte(gs, player,u)
        if direction==UnitAction.DIRECTION_UP :automata._core.build(u,uType,u.getX(),u.getY()-1)
        elif direction==UnitAction.DIRECTION_DOWN: automata._core.build(u,uType,u.getX(),u.getY()+1)
        elif direction==UnitAction.DIRECTION_LEFT: automata._core.build(u,uType,u.getX()-1,u.getY())
        elif direction==UnitAction.DIRECTION_RIGHT: automata._core.build(u,uType,u.getX()+1,u.getY())
        
        else: automata._core.buildIfNotAlreadyBuilding(u,uType,u.getX(),u.getY(),reservedPositions,p,pgs)
    
        
        automata.resource -= uType.cost
            
        
	
   
        
