import jpype 
import jpype.imports
from jpype import * 



jpype.startJVM(jpype.getDefaultJVMPath(), classpath= ['jars/*'])

from InterfacePython import Match
from ai.abstraction import WorkerRush,LightRush
from rts import PhysicalGameState
from rts.units import UnitTypeTable

from synthesis.ai.interpreter import Interpreter


ai = LightRush(UnitTypeTable(2))
#ai = Interpreter(UnitTypeTable(2))
#ai0 = WorkerRush()
ai1 = LightRush(UnitTypeTable(2))


from playout.simpleMatch import SimpleMatch
sm = SimpleMatch()
win = sm.playout("maps/24x24/basesWorkers24x24A.xml",ai1,ai,7000,True)
print("win =",win)


jpype.shutdownJVM()
