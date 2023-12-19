

class SyntaxCheckerMicroRTS:

    Rules = {
    "N" :["0","1","2","3","4","5","6","7","8","9","10","15","20","25","50","100"],
    "OpponentPolicy" : ["Strongest","Weakest","Closest","Farthest","LessHealthy","MostHealthy"],
    "Type" : ["Base","Barracks","Worker","Ranged","Light","Heavy"],
    "TargetPlayer" : ["Enemy","Ally"],
    "Direction" : ["Right","Left","Up","Down","EnemyDir"],
    "Begin" : ["for(Unit u){"],
    "Comand" : ["u.attack(","u.build(","u.harvest(","u.idle()","u.moveAway()","u.moveToUnit(","u.train(","}endFor"],
    "EndComand" : [")"],
    "End" : ["<pad>"]
    }

    def __init__(self) -> None:
        self.stack = []
        self.cont =0

    def process0(self,lastSymbol:str)->bool:

        if  lastSymbol == None:
            self.stack.append("Begin")
            return True
        elif lastSymbol in SyntaxCheckerMicroRTS.Rules[self.stack[-1]]:
            self.stack.pop()
            return True
        
        return False
    

    def processComand(self,lastSymbol:str)->None:
        if "u.attack(" == lastSymbol:
            self.stack.append("EndComand")
            self.stack.append("OpponentPolicy")
            
        elif "u.build(" == lastSymbol:
            self.stack.append("EndComand")
            self.stack.append("N")
            self.stack.append("Direction")
            self.stack.append("Type")
        elif "u.harvest(" == lastSymbol:
            self.stack.append("EndComand")
            self.stack.append("N")
            
        elif "u.idle()" == lastSymbol:
            self.stack.append("Comand")
        elif "u.moveAway()" == lastSymbol:
            self.stack.append("Comand")
        elif "u.moveToUnit(" == lastSymbol:
            self.stack.append("EndComand")
            self.stack.append("OpponentPolicy")
            self.stack.append("TargetPlayer")
            
            
        elif "u.train(" == lastSymbol:
            self.stack.append("EndComand")
            self.stack.append("N")
            self.stack.append("Direction")
            self.stack.append("Type")
        
        elif "}endFor" == lastSymbol:
            self.stack.append("End")
        
        
        
        
        


    def process1(self,lastSymbol:str)->None:
        if lastSymbol == None:
            return
        elif "for(Unit u){" == lastSymbol:
            self.stack.append("Comand")
        elif  "<pad>"== lastSymbol:
            self.stack.append("End")
        elif  ")"== lastSymbol:
            self.stack.append("Comand")
        elif lastSymbol in SyntaxCheckerMicroRTS.Rules["Comand"]:
            self.processComand(lastSymbol)
        
        

    def Valid_Next_Symblo(self,lastSymbol:str):#->list[str]:
        #print(lastSymbol,self.stack)
        self.cont+=1
        if not self.process0(lastSymbol):
            print("Erro0",lastSymbol,self.stack)
            return None
        
        self.process1(lastSymbol)
        
        return self.next_option()
    
    def next_option(self):#->list[str]:
        if self.cont >53 and self.stack[-1] =="Comand":
            return ["}endFor"]
        else:
            return SyntaxCheckerMicroRTS.Rules[self.stack[-1]]
    

     

def test0():
    arq = open("./Scripts.txt","r")
    cont=0
    for l in arq.readlines():

        l=l.rstrip("\n")
        #l ="for(Unit u){|u.build(|Light|Up|6|)|u.build(|Worker|Up|2|)|u.train(|Barracks|Left|2|)|u.moveAway()|u.train(|Base|EnemyDir|0|)|}endFor"
        symbols = l.split("|")

        #print(symbols) 
        Checker =SyntaxCheckerMicroRTS()
        Checker.Valid_Next_Symblo(None)
        for s in symbols:
            if Checker.Valid_Next_Symblo(s) == None:
                print(l)
                return
        cont+=1             
        if cont>=1 and False :
            return
            
def test1():
    import random
    from  tolkerinze import Tokenization
    for i in range(100):
      
        symbol = None
        Checker =SyntaxCheckerMicroRTS()
        list = []
        while symbol != "<pad>":
            ops= Checker.Valid_Next_Symblo(symbol) 
            x = random.randint(0,len(ops)-1)
          
            symbol =  ops[x]
            list.append(symbol)
        script = Tokenization.symbols_to_scrit(list)
        Checker =SyntaxCheckerMicroRTS()
        Checker.Valid_Next_Symblo(None)
        print(i,script)
        print()
        for s in list:
            
            if Checker.Valid_Next_Symblo(s) == None:
                print(list)
                return

def test2():
   
    l ="for(Unit u){|u.moveAway()|u.train(|Base|Down|4|)|u.moveAway()|u.harvest(|100|)|u.moveToUnit(|Ally|MostHealthy|)|u.train(|Base|EnemyDir|10|)|u.harvest(|100|)|u.build(|Ranged|Right|100|)|}endFor"
    symbols = l.split("|")

    Checker =SyntaxCheckerMicroRTS()
    Checker.Valid_Next_Symblo(None)
    for s in symbols:
        if Checker.Valid_Next_Symblo(s) == None:
            print(l)
            return
        return




