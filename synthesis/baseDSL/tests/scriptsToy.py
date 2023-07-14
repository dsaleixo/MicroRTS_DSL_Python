

from yaml import Node
from synthesis.baseDSL.almostTerminal.direction import Direction
from synthesis.baseDSL.almostTerminal.n import N
from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy
from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer
from synthesis.baseDSL.almostTerminal.utype import Utype
from synthesis.baseDSL.baseAction.attack import Attack
from synthesis.baseDSL.baseAction.build import Build
from synthesis.baseDSL.baseAction.harvest import Harvest
from synthesis.baseDSL.baseAction.idle import Idle
from synthesis.baseDSL.baseAction.moveToUnit import MoveToUnit
from synthesis.baseDSL.baseAction.train import Train
from synthesis.baseDSL.baseMain.C import C
from synthesis.baseDSL.baseMain.S import S
from synthesis.baseDSL.baseMain.S_S import S_S
from synthesis.baseDSL.baseMain.for_S import For_S


class ScriptsToy(object):
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def script0() ->Node:
        op = OpponentPolicy("Closest")
        attack = Attack(op)
        c = C(attack)
        for_s = For_S(S(c))
        return S(for_s)
    
    @staticmethod
    def script1() ->Node:
        op = OpponentPolicy("Closest")
        attack = Attack(op)
        c = C(attack)
        c1= C(Build(Utype("Barracks"),N("3"),Direction("Up")))
        for_s = For_S(
                S(S_S(
                    S(c1),
                    S(c)
                    )
                ))
        return S(for_s)    
    
    @staticmethod
    def script2() ->Node:
        c1 = S(C(Attack(OpponentPolicy("Closest"))))
        c2 = S(C(Build(Utype("Barracks"),N("1"),Direction("Up"))))
        c3 = S(C(Train(Utype("Ranged"),N("3"),Direction("Left"))))
        ss1 = S(S_S(c3,c2))
        ss2 = S(S_S(ss1,c1))
        for_s = For_S(ss2)
        return S(for_s)  
    
    @staticmethod
    def script3() ->Node:
        c1 = S(C(Attack(OpponentPolicy("Closest"))))
        c2 = S(C(Build(Utype("Barracks"),N("1"),Direction("Up"))))
        c3 = S(C(Train(Utype("Ranged"),N("3"),Direction("Left"))))
        c4 = S(C(Harvest(N("2"))))
        ss1 = S(S_S(c3,c2))
        ss2 = S(S_S(c4,c1))
        ss3 = S(S_S(ss1,ss2))
        for_s = For_S(ss3)
        return S(for_s)  
    
    @staticmethod
    def script3() ->Node:
        c1 = S(C(Attack(OpponentPolicy("Closest"))))
        c2 = S(C(Build(Utype("Barracks"),N("1"),Direction("Up"))))
        c3 = S(C(Train(Utype("Worker"),N("4"),Direction("Left"))))
        c4 = S(C(Harvest(N("2"))))
        ss1 = S(S_S(c3,c2))
        ss2 = S(S_S(c4,c1))
        ss3 = S(S_S(ss1,ss2))
        for_s = For_S(ss3)
        return S(for_s)  
    
    @staticmethod
    def script4() ->Node:
        c1 = S(C(MoveToUnit(OpponentPolicy("Closest"),TargetPlayer("Enemy"))))
        c2 = S(C(Build(Utype("Barracks"),N("1"),Direction("Up"))))
        c3 = S(C(Train(Utype("Worker"),N("4"),Direction("Left"))))
        c4 = S(C(Harvest(N("2"))))
        ss1 = S(S_S(c3,c2))
        ss2 = S(S_S(c4,c1))
        ss3 = S(S_S(ss1,ss2))
        for_s = For_S(ss3)
        return S(for_s)  
    
    
    @staticmethod
    def script5() ->Node:
        c1 = S(C(MoveToUnit(OpponentPolicy("Closest"),TargetPlayer("Enemy"))))
        c2 = S(C(Build(Utype("Barracks"),N("1"),Direction("Up"))))
        c3 = S(C(Train(Utype("Worker"),N("4"),Direction("Left"))))
        c4 = S(C(Harvest(N("2"))))
        c5 = S(C(Idle()))
        ss1 = S(S_S(c3,c2))
        ss2 = S(S_S(c4,c1))
        ss3 = S(S_S(ss1,ss2))
        for_s = For_S(S(S_S(c5,ss3)))
        return S(for_s)  