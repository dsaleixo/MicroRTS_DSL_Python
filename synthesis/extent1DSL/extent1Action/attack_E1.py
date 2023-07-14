


from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy
from synthesis.baseDSL.baseAction.attack import Attack
from synthesis.extent1DSL.almostTerminal.opponentPolicy_E1 import OpponentPolicy_E1


class Attack_E1(Attack):
    def __init__(self) -> None:
        super.__init__()
        
    def __init__(self,op :OpponentPolicy) -> None:
        self._op =op 
        
    def sample(self):
        op=OpponentPolicy_E1()
        op.sample()
        self._op = op
        