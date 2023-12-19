from synthesis.baseDSL.baseMain.empty import Empty
from synthesis.baseDSL.baseMain.node import Node


class Empty_E1(Empty):
    def __init__(self) -> None:
        self._used = False
        pass
    
    def sample(self,bugdet):
        pass
    
         
    def countNode(self,l : list[Node]):
        pass
    
    def mutation(self,bugdet):
        pass