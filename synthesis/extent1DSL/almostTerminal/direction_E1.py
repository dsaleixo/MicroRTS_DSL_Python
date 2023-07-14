import random

from synthesis.baseDSL.almostTerminal.direction import Direction


class Direction_E1(Direction):
    
    def __init__(self) -> None:
        super.__init__()
        
    def __init__(self,direc) -> None:
        super.__init__(direc)
        
    def sample(self)->None:
        rules = self.rules()
        r = random.randint(len(rules))
        self._direc = rules[r]