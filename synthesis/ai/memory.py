from __future__  import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from synthesis.ai.interpreter import Interpreter
from rts import GameState
from rts import Player,PhysicalGameState



class Memory:
    
    def __init__(self, gs : GameState, automata :Interpreter):
        self._freeUnit = {}
        pgs = gs.getPhysicalGameState()
        for u2 in pgs.getUnits():
            self._freeUnit[u2.getID()] = automata._core.getAbstractAction(u2) == None