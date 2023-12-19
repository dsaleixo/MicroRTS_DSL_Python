from __future__  import annotations
from queue import Empty


from typing import TYPE_CHECKING
from synthesis.baseDSL.baseMain.S_S import S_S

from synthesis.baseDSL.util.factory import Factory

from synthesis.baseDSL.almostTerminal.direction import Direction
from synthesis.baseDSL.almostTerminal.targetPlayer import TargetPlayer
from synthesis.baseDSL.almostTerminal.utype import Utype
from synthesis.baseDSL.almostTerminal.n import N
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
        
    def build_S(self,childS : ChildS = None) -> S:
        if childS == None: return S()
        else: return S(childS)

 
    def build_For_S(self,s : S = None) -> For_S:
        if s == None: return For_S()
        else: return For_S(s)
    
    def build_C(self,childC : ChildC= None) -> C:
        if childC == None: return C()
        else: return C(childC)
    
   
    def build_S_S(self,sL: S=None, sR: S=None) -> S_S:
        if sL == None: return S_S()
        else: return S_S(sL,sR)
    
    
    
    #actions
    def build_Attack(self,op : OpponentPolicy=None) -> Attack:
        if op == None: return Attack()
        else: return Attack(op)
    
    def build_Idle(self) -> Idle:
        return Idle()
    
    def build_Empty(self) -> Empty:
        return Empty()
    
    def build_Build(self,utype : Utype=None, direc:Direction=None, n: N=None) -> Build:
        if utype == None: return Build()
        else: return Build(utype,n, direc)
    	

    def build_Harvest(self,n : N=None) -> Harvest:
        if n == None: return Harvest()
        else: return Harvest(n)
    
    def build_MoveAway(self) -> MoveAway:
        return MoveAway()



    def build_MoveToUnit(self,tp:TargetPlayer=None, op:OpponentPolicy=None) -> MoveToUnit:
        if tp == None: return MoveToUnit()
        else: return MoveToUnit(tp, op)
	
 
 
    def build_Train(self, utype : Utype=None,  direc : Direction=None,  n : N=None) -> Train:
        if utype == None: return Train()
        else: return Train(utype,n,direc)


	# AlmostTerminal
    
   
    def build_Utype(self,value : str=None) -> Utype:
        if value == None: return
        return Utype(value)
    
    
    def build_N(self,value : str=None) -> N:
        if value == None: return
        return N(value)
        
   
    def build_Direction(self,value : str=None) -> Direction:
        if value == None: return Direction()
        return Direction(value)


    
    def build_TargetPlayer(self,value : str=None) -> TargetPlayer:
        if value == None: return TargetPlayer()
        return TargetPlayer(value)
    
    
    def build_OpponentPolicy(self,value : str=None) -> OpponentPolicy:
        if value == None: return OpponentPolicy()
        return OpponentPolicy(value)
    
