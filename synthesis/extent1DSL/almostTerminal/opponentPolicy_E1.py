import random


from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy


class OpponentPolicy_E1(OpponentPolicy):
    
    def __init__(self) -> None:
        super.__init__()
        
    def __init__(self,op) -> None:
        super.__init__(op)
        
    def sample(self):
        rules = self.rules()
        r = random.randint(len(rules))
        self._op = rules[r]