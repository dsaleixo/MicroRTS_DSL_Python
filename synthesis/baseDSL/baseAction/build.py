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
from synthesis.baseDSL.util.factory import Factory


class Build(ChildC,Node):
    
        
    def __init__(self,utype : Utype= None, n : N= None, direc : Direction= None) -> None:
        self._type =utype
        self._n = n
        self._direc = direc
        self._used = False
        
    
    def translate(self) -> str:
        return "u.build("+self._type.getValue()+","+self._direc.getValue()+","+self._n.getValue()+")"
    
    def translate2(self) -> str:
        return "u.build(|"+self._type.getValue()+"|"+self._direc.getValue()+"|"+self._n.getValue()+"|)"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs + "u.build("+self._type.getValue()+","+self._direc.getValue()+","+self._n.getValue()+")"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        pgs = gs.getPhysicalGameState()
        p = gs.getPlayer(player)
        uType = automata._utt.getUnitType(self._type.getValue())
        
        if not automata._memory._freeUnit[u.getID()] :
            return
         
        if not (uType.name == "Barracks" or uType.name == "Base" ):
            return
        
        if u.getPlayer() != player or \
                    u.getType().name != "Worker" or \
                    automata.resource < uType.cost    :
            return
        
        if automata.countConstrution(uType.name,player,gs) >= int(self._n.getValue()):
            return 
        
        reservedPositions =  java.util.LinkedList()
	
      
        direction = self._direc.converte(gs, player,u)
        if direction==UnitAction.DIRECTION_UP :automata._core.build(u,uType,u.getX(),u.getY()-1)
        elif direction==UnitAction.DIRECTION_DOWN: automata._core.build(u,uType,u.getX(),u.getY()+1)
        elif direction==UnitAction.DIRECTION_LEFT: automata._core.build(u,uType,u.getX()-1,u.getY())
        elif direction==UnitAction.DIRECTION_RIGHT: automata._core.build(u,uType,u.getX()+1,u.getY())
        
        else: automata._core.buildIfNotAlreadyBuilding(u,uType,u.getX(),u.getY(),reservedPositions,p,pgs)
        
        self._used= True
        automata.resource -= uType.cost
        automata._memory._freeUnit[u.getID()] = False
        
        
        
    def load(self, l : list[str], f : Factory):
        s = l.pop(0)
        self._type = f.build_Utype(s)
        s1 = l.pop(0)
        self._direc =  f.build_Direction(s1)
        s2 = l.pop(0)
        self._n = f.build_N(s2)





    def save(self,l : list[str]) -> None:
        l.append("Build")
        l.append(self. _type.getValue())
        l.append(self._direc.getValue())
        l.append(self._n.getValue())
	
            
        
    def clone(self, f : Factory) -> Node:
        return f.build_Build(self._type.clone(f), self._direc.clone(f), self._n.clone(f))
    
    def resert(self, f : Factory) -> None:
        self._used = False
        
    def clear(self,father:Node, f : Factory) -> Node:
        return self._used
   
        
