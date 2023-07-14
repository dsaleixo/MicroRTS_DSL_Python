from synthesis.baseDSL.almostTerminal.direction import Direction
from synthesis.baseDSL.almostTerminal.n import N
from synthesis.baseDSL.almostTerminal.utype import Utype
from synthesis.baseDSL.baseAction.harvest import Harvest
from synthesis.baseDSL.baseAction.train import Train
from synthesis.extent1DSL.almostTerminal.direction_E1 import Direction_E1
from synthesis.extent1DSL.almostTerminal.n_E1 import N_E1
from synthesis.extent1DSL.almostTerminal.utype_E1 import Utype_E1


class Harvest_E1(Harvest):
    def __init__(self) -> None:
        super.__init__()
        
    def __init__( n : N) -> None:
        super.__init__(utype,n,direc)
        
    def sample(self):
        n = N_E1()
        n.sample()
        self._n = n
     