


from playout.simpleMatch import SimpleMatch
from selfPlay.selfPlay import SelfPlay
from synthesis.ai.interpreter import Interpreter
from synthesis.baseDSL.baseMain.for_S import For_S
from synthesis.extent1DSL.extent1Main.empty_E1 import Empty_E1
from synthesis.extent1DSL.extent1Main.s_E1 import S_E1

from rts.units import UnitTypeTable

class SelfPlayDefault(SelfPlay):
    
    def __init__(self,n,map,max_tick,factory):
        self._n = n
        self._progs = []
        self._progs.append(S_E1(Empty_E1()))
        self._n_count = 0
        self._map = map
        self._sm = SimpleMatch()
        self._max_tick = max_tick
        self._f=factory
        
    def getN(self):
        return self._n_count
  
    def update(self, prog):
        if self._n == len(self._progs):
            p = self._progs.pop(0)
        
        p2 = prog.clone(self._f)
        self._progs.append(p2)
        
        
    

    def winToScore(self,player,result):
        if player == result: return 1.0
        if 1 - player == result: return 0.0
        return 0.5

    def evaluate(self, prog):
        a1 = Interpreter(UnitTypeTable(2),For_S(prog))
        score = 0
        for p in self._progs:
            a2 = Interpreter(UnitTypeTable(2),For_S(p))
           
            score += self.winToScore(0,self._sm.playout(self._map,a1,a2,self._max_tick,False) )
            score += self.winToScore(1,self._sm.playout(self._map,a2,a1,self._max_tick,False) )
            self._n_count += 1 
        return score/(2*len(self._progs))
    
    def getBest(self):
        return self._progs[-1].clone(self._f)
    
    def getIndividual(self):
        return self.getBest()
    
 
    def stoppingCriterion(self,score):
        if abs(1.0-score)< 0.001:
            return True
        return False