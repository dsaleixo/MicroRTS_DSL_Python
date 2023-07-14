import random
from synthesis.baseDSL.baseAction.attack import Attack 

from synthesis.baseDSL.baseMain.C import C, ChildC
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class C_E1(C):

    def __init__(self):
        super.__init__()
        
    def __init__(self, childC : ChildC):
        super.__init__(childC)
        
    def sample(self):
        f = Factory_E1()
        rules = self.rules(f)
        r = random.randint(len(self.rules()))
        action = rules[r]
        action.sample()
        self._childC = action
        
        

