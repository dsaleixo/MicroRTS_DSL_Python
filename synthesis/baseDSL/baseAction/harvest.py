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


class Harvest(ChildC,Node):
    
    def __init__(self) -> None:
        self._n = None
       
        
    def __init__(self, n : N) -> None:
        self._n = n
        
        
    
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
                    u.getPlayer() != player or automata._core.getAbstractAction(u)!=None:
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
             automata._core.harvest(u, closestResource, closestBase)
        