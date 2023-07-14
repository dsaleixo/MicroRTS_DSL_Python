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


from synthesis.baseDSL.util.factory import Factory


class Factory_E1(Factory):
    
    def build_S() -> S:
        raise Exception('Unimplemented method: build_S')
    def build_S(childS : ChildS) -> S:
        raise Exception('Unimplemented method: build_S')
    
    def build_for_S() -> For_S:
        raise Exception('Unimplemented method: For_S')
    def build_for_S(s : S) -> For_S:
        raise Exception('Unimplemented method: For_S')
    
    def build_C() -> C:
        raise Exception('Unimplemented method: build_C')
    def build_C(childC : ChildC) -> C:
        raise Exception('Unimplemented method: build_C')
    
   
    
    
    
    
    #actions
    def build_Attack() -> Attack:
        raise Exception('Unimplemented method: Attack')
    def build_Attack(op : OpponentPolicy) -> Attack:
        raise Exception('Unimplemented method: Attack') 
    
    def build_Idle() -> Idle:
        raise Exception('Unimplemented method: Idle')
    
    def build_Build() -> Build:
        raise Exception('Unimplemented method: Build')
    
    def build_Build(utype : Utype, direc:Direction, n: N) -> Build:
        raise Exception('Unimplemented method: Build')
    	
    def build_Harvest() -> Harvest:
        raise Exception('Unimplemented method: Harvest')
    
    def build_Harvest(n : N) -> Harvest:
        raise Exception('Unimplemented method: Harvest')
    
    def build_MoveAway() -> MoveAway:
        raise Exception('Unimplemented method: MoveAway')

    def build_MoveToUnit() -> MoveToUnit:
        raise Exception('Unimplemented method: MoveToUnit')

    def build_MoveToUnit(tp:TargetPlayer, op:OpponentPolicy) -> MoveToUnit:
        raise Exception('Unimplemented method: MoveToUnit')
	
    def build_Train() -> Train:
        raise Exception('Unimplemented method: Train')

    def build_Train( utype : Utype,  direc : Direction,  n : N) -> Train:
        raise Exception('Unimplemented method: Train')


	# AlmostTerminal
    
    def build_Utype() -> Utype:
        raise Exception('Unimplemented method: Utype') 
    def build_Utype(value : str) -> Utype:
        raise Exception('Unimplemented method: Utype')
    
    def build_N() -> N:
        raise Exception('Unimplemented method: N')
    def build_N(value : str) -> N:
        raise Exception('Unimplemented method: N')
        
    def build_Direction() -> Direction:
        raise Exception('Unimplemented method: Direction')
    def build_Direction(value : str) -> Direction:
        raise Exception('Unimplemented method: Direction')


    def build_TargetPlayer() -> TargetPlayer:
        raise Exception('Unimplemented method: Direction')
    def build_TargetPlayer(value : str) -> TargetPlayer:
        raise Exception('Unimplemented method: Direction')
    
    def build_OpponentPolicy() -> OpponentPolicy:
        raise Exception('Unimplemented method: Direction')
    def build_OpponentPolicy(value : str) -> OpponentPolicy:
        raise Exception('Unimplemented method: Direction')
    