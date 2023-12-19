
import torch
from leaps.module.build_ast import BuildAst
from leaps.module.tolkerinze import Tokenization
from search.individuals.individual import Individual

from selfPlay.selfPlay import SelfPlay
from synthesis.baseDSL.baseMain.for_S import For_S
from synthesis.baseDSL.util.factory_Base import Factory_Base


class Individual_Leaps(Individual):
    
    def __init__(self, model, mutation, clean):
        self._model = model
        self._mutation  = mutation
        self._build_ast = BuildAst(Factory_Base())
        self._clean = clean
        
        
    def indToProg(self, z):
        self._model.eval()
        with torch.inference_mode():
            
            prog = self._model.decode_vector(z)
          
            script = Tokenization.ints_to_script(prog[0])
            ast = self._build_ast.build(script)
            return ast._s
    
    
    def getNeighborhood(self, ind, n_neighborhood):
        return self._mutation.getMutations(ind, n_neighborhood)
    
    
    def progToInd(self,prog):
        
        self._model.eval()
        with torch.inference_mode():
            ss = prog.translate2()
            
            fo = For_S(prog)
            ss = fo.translate2()
            
            list_token = Tokenization.script_to_int(ss)
            list_token+=[Tokenization.symbol_to_tokens('<pad>') for _ in range(70)]
            tensor = torch.tensor(list_token, dtype =torch.long)
            z =self._model.encode_program(tensor)
            return z[0]
    
    
    def toString(self,ind):
        prog = self.indToProg(ind)
        return prog.translate2()
    
    
    
    
    
    def clone(self,tensor,f):
        return tensor.clone()
    
    
    def evaluate(self,ind,f,sp :SelfPlay):
        prog = self.indToProg(ind)
        result = sp.evaluate(prog)
        if self._clean:
            prog.clear(None,f)
        ind = self.progToInd(prog)
        return result
        
    
        
    
    