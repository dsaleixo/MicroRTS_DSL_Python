from __future__  import annotations
from tkinter import N

from typing import TYPE_CHECKING

from synthesis.baseDSL.util.factory import Factory
if TYPE_CHECKING:
    from synthesis.baseDSL.almostTerminal.direction import Direction
    from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer
    from synthesis.baseDSL.almostTerminal.utype import Utype
    from synthesis.baseDSL.baseAction.build import Build
    from synthesis.baseDSL.baseAction.harvest import Harvest

    from synthesis.baseDSL.baseAction.idle import Idle
    from synthesis.baseDSL.baseAction.moveAway import MoveAway
    from synthesis.baseDSL.baseAction.moveToUnit import MoveToUnit
    from synthesis.baseDSL.baseAction.train import Train

    from synthesis.baseDSL.almostTerminal.opponentPolicy import OpponentPolicy
    from synthesis.baseDSL.baseAction.attack import Attack
    from synthesis.baseDSL.baseMain.S import S, ChildS
    from synthesis.baseDSL.baseMain.for_S import For_S
    from synthesis.baseDSL.baseMain.C import C, ChildC

from abc import ABC, abstractmethod

class Factory_Base(Factory):
    
    def build_S() -> S:
        return S()
    def build_S(childS : ChildS) -> S:
        return S(childS)
    
    def build_for_S() -> For_S:
        return For_S()
    def build_for_S(s : S) -> For_S:
        return For_S(s)
    
    def build_C() -> C:
        return C()
    def build_C(childC : ChildC) -> C:
        return C(childC)
    
   
    
    
    
    
    #actions
    def build_Attack() -> Attack:
        return Attack()
    def build_Attack(op : OpponentPolicy) -> Attack:
        return Attack(op)
    
    def build_Idle() -> Idle:
        return Idle()
    
    def build_Build() -> Build:
        return Build()
    
    def build_Build(utype : Utype, direc:Direction, n: N) -> Build:
        return Build(utype,n, direc)
    	
    def build_Harvest() -> Harvest:
        return Harvest()
    
    def build_Harvest(n : N) -> Harvest:
        return Harvest(n)
    
    def build_MoveAway() -> MoveAway:
        return MoveAway()

    def build_MoveToUnit() -> MoveToUnit:
        return MoveAway()

    def build_MoveToUnit(tp:TargetPlayer, op:OpponentPolicy) -> MoveToUnit:
        return MoveToUnit(tp, op)
	
    def build_Train() -> Train:
        return Train()

    def build_Train( utype : Utype,  direc : Direction,  n : N) -> Train:
        return Train(utype,n,direc)


	# AlmostTerminal
    
    def build_Utype() -> Utype:
        return Utype()
    def build_Utype(value : str) -> Utype:
        return Utype(value)
    
    def build_N() -> N:
        return N()
    def build_N(value : str) -> N:
        return N(value)
        
    def build_Direction() -> Direction:
        return Direction()
    def build_Direction(value : str) -> Direction:
        return Direction(value)


    def build_TargetPlayer() -> TargetPlayer:
        return TargetPlayer()
    def build_TargetPlayer(value : str) -> TargetPlayer:
        return TargetPlayer(value)
    
    def build_OpponentPolicy() -> OpponentPolicy:
        return OpponentPolicy()
    def build_OpponentPolicy(value : str) -> OpponentPolicy:
        return OpponentPolicy(value)
    
