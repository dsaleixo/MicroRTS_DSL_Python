from abc import ABC, abstractmethod

from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.baseMain.noTerminal import NoTerminal
from synthesis.baseDSL.util.factory import Factory
from synthesis.ai.interpreter import Interpreter

from rts.units import Unit
from rts import GameState


class ChildC(Node,ABC):
    pass
    

class C(Node,NoTerminal):

    def __init__(self):
        self._childC = None
        
    def __init__(self, childC : ChildC):
        self._childC = childC
        
    def translate2(self) -> str:
        return self._childC.translate2()
   
  
    def translate(self) -> str:
        return "C" if self._childC == None else self._childC.translate()
    
   
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs+"C" if self._childC == None else self._childC.translateIndentation(int)
            
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        self._childC.interpret(gs,player,u,automata)
   
   
   
    def getRule(self)->Node:
        return self._childC
    
    
    def setRule(self, node : Node)->None:
        if  issubclass(node,ChildC):
            self._childC = node
    
    
    def rules(f: Factory) :#->list[Node]
        return [f.build_Attack(),f.build_Build(),f.build_Train(),
                f.build_Idle(),f.build_MoveAway(),f.build_MoveToUnit(),
                f.build_Harvest()]