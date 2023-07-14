
import random

from synthesis.baseDSL.almostTerminal.n import N



class N_E1(N):
    
    def __init__(self):
        super.__init__()
        
        
    def __init__(self,n) -> None:
        super.__init__(n)
        
    def sample(self)->None:
        rules = self.rules()
        r = random.randint(len(rules))
        self._n = rules[r]