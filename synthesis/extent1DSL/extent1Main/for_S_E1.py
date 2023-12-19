from __future__  import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
    from synthesis.extent1DSL.extent1Main.s_E1 import S_E1


from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.baseMain.S import S
from synthesis.baseDSL.baseMain.S import ChildS
import random
from synthesis.baseDSL.baseMain.for_S import For_S




class For_S_E1(For_S):
    
        
    def __init__(self, s : S=None):
        self._s = s
        
    def sample(self):
        from synthesis.extent1DSL.extent1Main.s_E1 import S_E1
        s = S_E1()
        s.sample()
        self._s = s
        
    def countNode(self,l : list[Node]):
        l.append(self)
        self._s.countNode(l)
        