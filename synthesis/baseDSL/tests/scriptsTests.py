from synthesis.baseDSL.tests.scriptsToy import ScriptsToy
#
class ScriptsTests(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def test0():
        script = ScriptsToy.script3()
        print(script.translate())
        from synthesis.ai.interpreter import Interpreter
        from ai.abstraction import WorkerRush,LightRush
        from rts.units import UnitTypeTable
        
        ai = Interpreter(UnitTypeTable(2),script)
        #ai0 = WorkerRush()
        ai1 = LightRush(UnitTypeTable(2))


        from playout.simpleMatch import SimpleMatch
        win = SimpleMatch.playout("maps/24x24/basesWorkers24x24A.xml",ai1,ai,7000,True)
        print("win =",win)



        
