

from synthesis.baseDSL.almostTerminal.almostTerminal import AlmostTerminal

from synthesis.ai.interpreter import Interpreter
from rts.units import Unit
from rts import GameState
from rts import UnitAction
from rts import PhysicalGameState



class Direction(AlmostTerminal):
    
    def __init__(self) -> None:
        self._direc = None
        
    def __init__(self,direc) -> None:
        self._direc = direc
    
    
    def rules(self):#->list[str]:
        return ["Right",
		        "Left",
                "Up",
                "Down",
		        "EnemyDir"]
    
   
    
    def setValue(self, s :str)->None:
        self._direc=s
    
    def getValue(self)->str:
        return self._direc
	
    def translate(self)->str:
        return self._direc
    
    
    
    def converte(self,gs : GameState, player:int, u : Unit) -> int :
        x = u.getX()
        y = u.getY()
        if self._direc == "Right" and gs.free(x+1,y):return UnitAction.DIRECTION_RIGHT
        if self._direc == "Left" and gs.free(x-1,y):return UnitAction.DIRECTION_LEFT
        if self._direc == "Up" and gs.free(x,y-1):return UnitAction.DIRECTION_UP
        if self._direc == "Down" and gs.free(x,y+1):return UnitAction.DIRECTION_DOWN
        
        if self._direc == "EnemyDir" :
            pgs = gs.getPhysicalGameState()
            best_direction = -1
            best_score = -1
	        
            if y>0 and gs.free(x,y-1): 
                score = self.score(x,y-1, player, pgs)
                if score<best_score or best_direction==-1 :
                    best_score = score
                    best_direction = UnitAction.DIRECTION_UP  
	            
            if x<pgs.getWidth()-1 and gs.free(x+1,y):
                score = self.score(x+1,y, player, pgs)
                if score<best_score or best_direction==-1 :
                    best_score = score
                    best_direction = UnitAction.DIRECTION_RIGHT;            
	            
            if y<pgs.getHeight()-1 and gs.free(x,y+1) :
                score = self.score(x,y+1, player, pgs)
                if score<best_score or best_direction==-1 :
                    best_score = score
                    best_direction = UnitAction.DIRECTION_DOWN
	    
            if x>0 and gs.free(x-1,y): 
                score = self.score(x-1,y, player, pgs)
                if score<best_score or best_direction==-1:
                    best_score = score
                    best_direction = UnitAction.DIRECTION_LEFT
            return best_direction
        return -1
	
 
 
    def score(self, x:int, y: int, player: int, pgs: PhysicalGameState) -> int:
        distance = 0
        first = True
        #score is minus distance to closest resource
        for u in pgs.getUnits():
            if u.getPlayer()==1-player:
                dx = abs(u.getX() - x) 
                dy = abs(u.getY() - y)
                d = dx*dx +dy*dy
                if  first or d<distance :
                    distance = d
                    first = False
        return distance
	    
