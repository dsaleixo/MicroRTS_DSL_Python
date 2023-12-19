
import jpype 
import jpype.imports
from jpype import *










if __name__ == '__main__':
    

    jpype.startJVM(jpype.getDefaultJVMPath(), classpath= ['jars/*'])
    from unnamedProject.getIntances.getInstance0 import GetInstance0
    from unnamedProject.model.trainer0 import Trainer0
    from unnamedProject.model.player0 import Player0

    Player0.test()


    jpype.shutdownJVM()
    
    
    