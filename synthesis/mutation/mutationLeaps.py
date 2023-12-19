

import torch
from synthesis.baseDSL.baseMain.node import Node
from synthesis.mutation.mutation import Mutation
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
import random

class MutationLaps(Mutation):
    
    def __init__(self,sigma):
        self._sigma = sigma
    
    
    def getMutations(self, vector, n_mutation) -> list[Node]:
        l = []
        for _ in range(n_mutation):
            l.append(vector + torch.rand_like(vector)*self._sigma)
           
        return l