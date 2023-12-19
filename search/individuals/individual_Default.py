


from search.individuals.individual import Individual
from selfPlay.selfPlay import SelfPlay
from synthesis.mutation.mutation import Mutation


class Individual_Default(Individual):
    
    def __init__(self, mutation: Mutation):
        self._mut = mutation
        
    
   
    def indToProg(self, ind):
        return ind
    
    
    def getNeighborhood(self, ind, n_neighborhood):
        return self._mut.getMutations(ind, n_neighborhood)
    
    
    def progToInd(self,prog):
        return prog
    
    
    def toString(self,ind):
        return ind.translate2()
    
    
    
    
    
    def clone(self,prog,f):
        return prog.clone(f)
    
    
    def evaluate(self,prog,f,sp :SelfPlay):
        
        result = sp.evaluate(prog)
        prog.clear(None,f)
        return result
