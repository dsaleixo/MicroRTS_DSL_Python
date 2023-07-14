
import random

from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer


class TargetPlayer_E1(TargetPlayer):
    
    def __init__(self) -> None:
        super.__init__()
        
    def __init__(self,tp) -> None:
        super.__init__(tp)
        
    def sample(self)->None:
        rules = self.rules()
        r = random.randint(len(rules))
        self._tp = rules[r]
    
    