import random
from tkinter import N
from synthesis.baseDSL.almostTerminal.direction import Direction
from synthesis.baseDSL.almostTerminal.utype import Utype

from synthesis.baseDSL.baseAction.build import Build
from synthesis.extent1DSL.almostTerminal.direction_E1 import Direction_E1
from synthesis.extent1DSL.almostTerminal.n_E1 import N_E1
from synthesis.extent1DSL.almostTerminal.utype_E1 import Utype_E1


class Build_E1(Build):
    def __init__(self) -> None:
        super.__init__()
        
    def __init__(self,utype : Utype, n : N, direc : Direction) -> None:
        super.__init__(utype,n,direc)
        
    def sample(self):
        n = N_E1()
        n.sample()
        self._n = n
        utype = Utype_E1()
        utype.sample()
        self._type = utype
        direc = Direction_E1()
        direc.sample()
        self._direc = direc