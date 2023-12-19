from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer
from synthesis.baseDSL.baseAction.moveToUnit import MoveToUnit
from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.baseDSL.baseMain.node import Node
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy
from synthesis.extent1DSL.almostTerminal.opponentPolicy_E1 import OpponentPolicy_E1
from synthesis.extent1DSL.almostTerminal.targetPlayer_E1 import TargetPlayer_E1

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import Player



class MoveToUnit_E1(MoveToUnit):
    

        
    def __init__(self,op :OpponentPolicy = OpponentPolicy_E1(), tp :TargetPlayer = TargetPlayer_E1()) -> None:
        self._op =op 
        self._tp = tp
        self._used = False
        
    def sample(self):
        op = OpponentPolicy_E1()
        op.sample()
        self._op=op
        tp = TargetPlayer_E1()
        tp.sample()
        self._tp = tp
        
         
    def countNode(self,l : list[Node]):
        l.append(self)
        self._op.countNode(l)
        self._tp.countNode(l)
        
    def mutation(self,bugdet):
        self.sample()