
import random

from synthesis.baseDSL.almostTerminal.utype import Utype


class Utype_E1(Utype):
    
    def __init__(self) -> None:
        super.__init__()
        
    def __init__(self,utype) -> None:
        super.__init__(utype)
        
    def sample(self)->None:
        rules = self.rules()
        r = random.randint(len(rules))
        self._type = rules[r]