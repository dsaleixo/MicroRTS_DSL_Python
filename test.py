
import jpype 
import jpype.imports
from jpype import *




if __name__ == '__main__':
    

    jpype.startJVM(jpype.getDefaultJVMPath(), classpath= ['jars/*'])
    from synthesis.baseDSL.tests.scriptsTests import ScriptsTests
    from synthesis.extent1DSL.tests.sampleMutation import SampleMutation 
    from tests.main_synthises import MainSynthesis
    from tests.main_match import MainMatch
    from InterfacePython import Match
    from ai.abstraction import WorkerRush,LightRush
    from rts import PhysicalGameState
    from rts.units import UnitTypeTable

  
    #ScriptsTests.test0( )
    #SampleMutation.test2()
    import sys
    args = sys.argv[1:]
    
    m = MainMatch(args)
    m.run()




    jpype.shutdownJVM()
    
    
    