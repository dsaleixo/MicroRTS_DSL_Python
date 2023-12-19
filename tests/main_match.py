from ai.abstraction import WorkerRush,LightRush
from playout.simpleMatch import SimpleMatch
from rts.units import UnitTypeTable
from synthesis.ai.interpreter import Interpreter
from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
from synthesis.baseDSL.util.factory_Base import Factory_Base


class MainMatch():

    def __init__(self, args):
        self._s0 = ScriptsToy.script3()
        self._s1 = ScriptsToy.script5()
        self._ai0 = Interpreter(UnitTypeTable(2),self._s0 )
        self._ai1 =  Interpreter(UnitTypeTable(2),self._s1 )
        self._map = "maps/24x24/basesWorkers24x24A.xml"
        self._maxTick = 2000
        self._showScream= True

    def run(self):
        from playout.simpleMatch import SimpleMatch
        sm = SimpleMatch()
        print(self._s0.translate())
        print(self._s1.translate())
        win = sm.playout(self._map,self._ai0,self._ai1,self._maxTick,self._showScream)
        print("win =",win)
        self._s0.clear(None,Factory_Base())
        print(self._s0.translate())
        self._s1.clear(None,Factory_Base())
        print(self._s1.translate())


    @staticmethod
    def execute(args):
        main = MainMatch(args)
        main.run()