

from synthesis.baseDSL.baseAction.moveAway import MoveAway
from synthesis.baseDSL.baseMain.node import Node


class MoveAway_E1(MoveAway):
    def __init__(self) -> None:
        self._used = False
        pass
    
    def sample(self):
        pass
    
         
    def countNode(self,l : list[Node]):
        pass
    
    def mutation(self,bugdet):
        self.sample()