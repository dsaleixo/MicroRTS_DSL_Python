
from synthesis.baseDSL.util.factory import Factory
from synthesis.extent1DSL.util.Factory_E1 import Factory_E1


class BuildAst:
    
    def __init__(self, f : Factory):
        self._f = f
        
    

    
    def processSymbol(self, symbol,l):
        if "u.attack(" ==  symbol[0]:
            op = symbol[1]
            attack = self._f.build_Attack(self._f.build_OpponentPolicy(op))
            symbol.pop(0)
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(attack)))
            return
            
        elif "u.build(" ==  symbol[0]:
            n  = self._f.build_N(symbol[3])
            direc = self._f.build_Direction(symbol[2])
            u_type = self._f.build_Utype(symbol[1])
            build = self._f.build_Build(u_type,direc,n)
            symbol.pop(0)
            symbol.pop(0)
            symbol.pop(0)
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(build)))
            return 
            
        elif "u.harvest(" ==  symbol[0]:
            n  = self._f.build_N(symbol[1])
            harvest = self._f.build_Harvest(n)
            symbol.pop(0)
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(harvest)))
            return
            
        elif "u.idle()" ==  symbol[0]:
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(self._f.build_Idle())))
            return
        elif "u.moveAway()" ==  symbol[0]:
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(self._f.build_MoveAway())))
            return
        elif "u.moveToUnit(" ==  symbol[0]:
            
            op = self._f.build_OpponentPolicy(symbol[1])
            tp = self._f.build_TargetPlayer(symbol[2])
            symbol.pop(0)
            symbol.pop(0)
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(self._f.build_MoveToUnit(op,tp))))
            return
        
            
        elif "u.train(" ==  symbol[0]:
            n  = self._f.build_N(symbol[3])
            direc = self._f.build_Direction(symbol[2])
            u_type = self._f.build_Utype(symbol[1])
            train = self._f.build_Train(u_type,direc,n)
            symbol.pop(0)
            symbol.pop(0)
            symbol.pop(0)
            symbol.pop(0)
            l.append(self._f.build_S(self._f.build_C(train)))
            return 
        symbol.pop(0)


    def step2(self, l):
        s = l.pop(0)
     
        while len(l) !=0:
            s1= l.pop(0)
          
            s = self._f.build_S(self._f.build_S_S(s,s1))
        return self._f.build_For_S(s)
    
    def build(self, prog : str):
        l = []
        symbols = prog.split("|")
        while len(symbols) != 0:
            self.processSymbol(symbols,l)
        
        return self.step2(l)
       
def test0():
    arq = open("./leaps/module/Scripts.txt","r")
    cont=0
    ast_b = BuildAst(Factory_E1())
    for l in arq.readlines():

        l=l.rstrip("\n")
        #l ="for(Unit u){|u.build(|Light|Up|6|)|u.build(|Worker|Up|2|)|u.train(|Barracks|Left|2|)|u.moveAway()|u.train(|Base|EnemyDir|0|)|}endFor"
        ast  = ast_b.build(l)
        if ast.translate2()!=l:
            print(l)
            print(ast.translate2())
            return 
        cont+=1             
        if cont>=1  and False:
            return     
    print("Fim")     

            
            