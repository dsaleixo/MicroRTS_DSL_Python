import jpype 
import jpype.imports
from jpype import *






if __name__ == '__main__':
    jpype.startJVM(jpype.getDefaultJVMPath(), classpath= ['jars/*'])
    from leaps.test.testMutationLeaps import TestMutationLeaps 
    
    TestMutationLeaps.test2()
    
    jpype.shutdownJVM()