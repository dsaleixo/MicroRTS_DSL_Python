
import time

import torch
from leaps.module.test_embedding import leaps_vae_MicroRTS
from logger.stdout_logger import StdoutLogger
from search.HC import HC
from search.SA import SA
from search.individuals.individual_Default import Individual_Default
from search.individuals.individual_Leaps import Individual_Leaps
from selfPlay.selfPlayDefault import SelfPlayDefault
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1
from synthesis.mutation.mutation import Mutation
from synthesis.mutation.mutation1 import Mutation1
from synthesis.mutation.mutation0 import Mutation0
from synthesis.mutation.mutationLeaps import MutationLaps


class MainSynthesis():
    
    def setMap(self):
        if self._opMap == "0": 
            self._map = "maps/24x24/basesWorkers24x24A.xml"
            self._time = 2000
            self.max_tick = 6000
        if self._opMap == "1": 
            self._map = "maps/32x32/basesWorkers32x32A.xml"
            self._time = 2000
            self.max_tick = 6000
        if self._opMap == "2": 
            self._map = "maps/BroodWar/(4)BloodBath.scmB.xml" 
            self._time = 4000
            self.max_tick = 15000
    
    def __init__(self,args):
        self._opMap = args[0]
        self._opSearch = args[1]
        self._opIndividual= args[2]
        self._opSelfPlay = args[3]
        id_test = args[0] +"_"+ args[1] +"_"+ args[2] + "_"+args[3] + "_"+args[4]
        StdoutLogger.init_logger(id_test)
        StdoutLogger.log("id_conf",id_test)
        
        self.setMap()
        self.setIndividual()
        self.setSearch()
        self.setSelfplay()
    
    

    

    def setIndividual(self) -> Mutation:
        if self._opIndividual == "0": self._ind = Individual_Default( Mutation0())
        if self._opIndividual == "1": self._ind = Individual_Default( Mutation1())
        if self._opIndividual == "2":
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            model = leaps_vae_MicroRTS(device)
            params = torch.load("leaps/models/01_pytorch_model", map_location=device)
            model.load_state_dict(params, strict=False)
            self._ind = Individual_Leaps( model,MutationLaps(0.5),False)
        if self._opIndividual == "3":
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            model = leaps_vae_MicroRTS(device)
            params = torch.load("leaps/models/01_pytorch_model", map_location=device)
            model.load_state_dict(params, strict=False)
            self._ind = Individual_Leaps( model,MutationLaps(0.5),True)
    
    def setSearch(self):
        if self._opSearch == "0": self._search = HC()
        if self._opSearch == "1": self._search = SA(2000,0.9,0.5)
    def setSelfplay(self):
        if self._opSelfPlay == "0": self._selfPlay = SelfPlayDefault(1,self._map,
                                                           self.max_tick,
                                                           Factory_E1()
                                                           ) #IBR
        if self._opSelfPlay == "1": self._selfPlay =  SelfPlayDefault(1000,self._map,
                                                           self.max_tick,
                                                           Factory_E1()
                                                           ) # Ficticious


    
        
        
    def run(self):
        start_time = time.time()
        while True:
            
            prog = self._selfPlay.getIndividual()
            r1 = self._selfPlay.evaluate(prog)
            prog_result, r0, log = self._search.run(prog,self._selfPlay,self._ind,5,self._time)
            
            
            
            
            if r0 > r1:
                time_eval = time.time() - start_time
                log +="Camp\t"+str(time_eval)+"\t"+str(self._selfPlay.getN())+"\t"+prog_result.translate()+"\n"
                self._selfPlay.update(prog_result)
            
            
            
            StdoutLogger.log("search",log)

        
    @staticmethod
    def execute(args):
        main = MainSynthesis(args)
        main.run()
        



   

        