import torch
from unnamedProject.getIntances.getInstance0 import GetInstance0

from unnamedProject.model.model0 import Model0

from InterfacePython import Match
from rts import UnitAction;
from rts.units import Unit;
from rts import GameState
from rts.units import UnitTypeTable
from ai.abstraction import HeavyRush
from rts import PlayerAction

class Player0:
    
    def __init__(self):
        self.model = Model0()
        self.model.load_state_dict(torch.load("./unnamedProject/model/models/model0.pt"))
        
    def crateAction(self,i :int, u : Unit)->UnitAction:
        if i==0:
            return UnitAction(0,10)
        elif i<5:
            return UnitAction(1,i-1)
        else:
            x,y =  GetInstance0.label_action[i]
            
            
            return UnitAction(5,u.getX()-x,u.getY()-y)
        
        
    def getAction(self,player : int, gs : GameState) -> PlayerAction:
        pa = PlayerAction()
        pgs = pgs = gs.getPhysicalGameState()
        for u in pgs.getUnits():
            if u.getPlayer()==0 and gs.getActionAssignment(u)==None:
                input = GetInstance0.StateToInput(gs).unsqueeze(dim=0)
                output = self.model(input)
                a = self.crateAction(output.argmax().item(),u)
                pa.addUnitAction(u,a)
    
                
        
        return pa
        
    def reset(self,utt : UnitTypeTable ):
        pass
    
    @staticmethod
    def test():
       
        path = "maps/newMaps/map0.xml"
        max_tick = 3000
        show_scream = True
        mch = Match(path, show_scream)
        ai0 = Player0()
        
        ai1 = HeavyRush(mch.getUTT())
        
        ai0.reset(mch.getUTT())
        ai1.reset(mch.getUTT())
        
        gameover = False
        
        while (not gameover) and mch.getGS().getTime()<max_tick:
            pa0= ai0.getAction(0, mch.getGS())
            pa1 =ai1.getAction(1, mch.getGS())  
            mch.SetActions(pa0)
            mch.SetActions(pa1)
            gameover = mch.run()
        mch.run()
        print("win = ",mch.getGS().winner())