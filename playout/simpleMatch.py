
from InterfacePython import Match

class SimpleMatch:
    
    def playout(path,ai0,ai1,max_tick,show_scream):
        mch = Match(path, show_scream)
        ai0.reset(mch.getUTT())
        ai1.reset(mch.getUTT())
        
        gameover = False
        
        while (not gameover) and mch.getGS().getTime()<max_tick:
            pa0= ai0.getAction(0, mch.getGS())
            pa1 =ai1.getAction(1, mch.getGS())
            #mch.SetActions(pa0)
            mch.SetActions(pa1)
            gameover = mch.run()
            
        return mch.getGS().winner()