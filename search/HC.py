


from search.individuals.individual import Individual
from selfPlay.selfPlay import SelfPlay
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
from synthesis.mutation.mutation import Mutation
import time

class HC:
    
    def __init__(self):
        self._f = Factory_E1()
        pass
    
    
    def run(self, prog, sp : SelfPlay, ind_handler : Individual,n_neighborhood:int, max_time : int):
        
        log = ""
        ind = ind_handler.progToInd(prog)
        start_time = time.time()
        pp = ind_handler.indToProg(ind)
        
        score_current = ind_handler.evaluate(ind,self._f,sp)
        time_eval = time.time() - start_time
        log +="actual\t"+str(time_eval)+"\t"+str(time_eval)+"\t"+str(sp.getN())+"\t"+ind_handler.toString(ind)+"\n"
        while True:
            mutations = ind_handler.getNeighborhood(ind,n_neighborhood)
            best_score_neighborhood = ind_handler.evaluate(mutations[0],self._f,sp)
            best_ind_neighborhood = mutations[0]
            for i  in  range(1,n_neighborhood):
                start_time2 = time.time()
                result = ind_handler.evaluate(mutations[i],self._f,sp)
                time_eval2 = time.time() - start_time2
                time_eval3 = time.time() - start_time
                log+="actual\t"+str(time_eval3)+"\t"+str(time_eval2)+"\t"+str(sp.getN())+"\t"+str(result)+"\t"+ind_handler.toString(mutations[i])+"\n"
                time_eval = time.time() - start_time
                if result > best_score_neighborhood:
                    best_score_neighborhood = result
                    best_ind_neighborhood = mutations[i]
                    
            
            if best_score_neighborhood > score_current:
                
                log+="actual2\t"+str(best_score_neighborhood)+"\n"
                score_current = best_score_neighborhood
                ind = best_ind_neighborhood
            
            
            end_time = time.time()
            
            
            if end_time - start_time > max_time or sp.stoppingCriterion(score_current):
                break
        
        return ind_handler.indToProg(ind), score_current, log
        