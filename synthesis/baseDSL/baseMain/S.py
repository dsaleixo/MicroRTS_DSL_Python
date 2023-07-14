from abc import ABC, abstractmethod

from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.baseMain.noTerminal import NoTerminal
from synthesis.baseDSL.util.factory import Factory
from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState


class ChildS(Node,ABC):
    pass
    

class S(Node,NoTerminal):

    def __init__(self):
        self._childS = None
        
    def __init__(self, childS : ChildS):
        self._childS = childS
        
   
   
  
    def translate(self) -> str:
        return "S" if self._childS == None else self._childS.translate()
    
    
    def translate2(self) -> str:
        return self._childS.translate2()
   
    def  translateIndentation(self,n_tab:int) ->str:
        tabs = ""
        for _ in range(n_tab):
            tabs+="\t"
        return tabs+"S" if self._childS == None else self._childS.translateIndentation(n_tab)
            
    
    
    def interpret(self,gs : GameState, player:int, u : Unit, automata :Interpreter) -> None:
        self._childS.interpret( gs,player,u,automata)
   
   
   
    def getRule(self)->Node:
        return self._childS
    
    
    def setRule(self, node : Node)->None:
        if  issubclass(node,ChildS):
            self._childS = node
    
    
    def rules(f: Factory) :#->list[Node]
        return [f.build_for_S(),
                f.build_C()]
        
    
    