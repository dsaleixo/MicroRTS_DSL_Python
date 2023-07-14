
import jpype 
import jpype.imports
from jpype import * 



if __name__ == '__main__':
    

    jpype.startJVM(jpype.getDefaultJVMPath(), classpath= ['jars/*'])
    from synthesis.baseDSL.tests.scriptsTests import ScriptsTests
    from InterfacePython import Match
    from ai.abstraction import WorkerRush,LightRush
    from rts import PhysicalGameState
    from rts.units import UnitTypeTable

  

    ScriptsTests.test0()




    jpype.shutdownJVM()
    
    
    