
import random

from synthesis.baseDSL.almostTerminal.utype import Utype
from synthesis.baseDSL.baseMain.node import Node


class Utype_E1(Utype):
    
  
        
    def __init__(self,utype = None) -> None:
        self._type = utype
        
    def sample(self)->None:
        rules = self.rules()
        r = random.randint(0,len(rules) - 1)
        self._type = rules[r]
        
    def countNode(self,l : list[Node]):
        l.append(self)
        
    def mutation(self,bugdet):
        self.sample()