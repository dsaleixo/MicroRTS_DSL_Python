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


class Harvest(ChildC,Node):
    
 
       
        
    def __init__(self, n : N=None) -> None:
        self._n = n
        self._used = False
        
        
    
    def translate(self) -> str:
        return "u.harvest("+self._n.getValue()+")"
    
    def translate2(self) -> str:
        return "u.harvest(|"+self._n.getValue()+"|)"
    
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs + "u.harvest("+self._n.getValue()+")"
        
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        
        pgs = gs.getPhysicalGameState()
        p = gs.getPlayer(player)
		
        if  (not u.getType().canHarvest) or \
                    u.getPlayer() != player or  not automata._memory._freeUnit[u.getID()] :
            return
		
        if automata.countHarvester(player,gs) >= int(self._n.getValue()):
            return
        
        closestBase = None
        closestResource = None
        closestDistance = 0
        for  u2 in pgs.getUnits():
            if u2.getType().isResource:
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestResource == None or d < closestDistance: 
                    closestResource = u2
                    closestDistance = d
           
        closestDistance = 0
        for u2 in pgs.getUnits() :
            if u2.getType().isStockpile and u2.getPlayer()==p.getID():
                d = abs(u2.getX() - u.getX()) + abs(u2.getY() - u.getY())
                if closestBase == None or d < closestDistance:
                    closestBase = u2
                    closestDistance = d
            
        if closestResource != None and closestBase != None:
            self._used = True
            automata._core.harvest(u, closestResource, closestBase)
            automata._memory._freeUnit[u.getID()] = False
        
        
    def load(self,l : list[str], f : Factory)->None:
        s = l.pop(0)
        self._n =  f.build_N(s)


    def save(self,l : list[str]) -> None:
        l.append("Harvest")
        l.append(self._n.getValue())
		
  
    def clone(self, f : Factory) -> Node:
        return f.build_Harvest( self._n.clone(f))
    
    def resert(self, f : Factory) -> None:
        self._used = False
        
    def clear(self,father:Node, f : Factory) -> Node:
        return self._used