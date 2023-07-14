



class Tokenization:

   

    table_symbol_int = {"for(Unit u){":0,"}endFor":1,
                        "u.attack(":2,"u.build(":3,"u.harvest(":4,"u.idle()":5,"u.moveAway()":6,"u.moveToUnit(":7,"u.train(":8,
                        "Strongest":9,"Weakest":10,"Closest":11,"Farthest":12,"LessHealthy":13,"MostHealthy":14,
                        "0":15,"1":16,"2":17,"3":18,"4":19,"5":20,"6":21,"7":22,"8":23,"9":24,"10":25,"15":26,"20":27,"25":28,"50":29,"100":30,
                        "Right":31,"Left":32,"Up":33,"Down":34,"EnemyDir":35,
                        "Base":36,"Barracks":37,"Worker":38,"Ranged":39,"Light":40,"Heavy":41,
                        "Enemy":42,"Ally":43,
                        ")":44,'<pad>':45
                        
                        }
    
    table_int_symbol = {}
    for key, value in table_symbol_int.items():
        table_int_symbol[value]=key

    
    @staticmethod
    def tableSize() -> int:
        return len(Tokenization.table_symbol_int)


    @staticmethod
    def symbol_to_tokens(s:str) -> int:
        if s in Tokenization.table_symbol_int:
            return Tokenization.table_symbol_int[s]
        else:
            print("erro")
            return -1

    

    @staticmethod
    def script_to_int(script:str) -> list[int]:
        symbols = script.split("|")
        list = []
        for s in symbols:
            resp = Tokenization.symbol_to_tokens(s)
            list.append(resp)
        return list
        

    @staticmethod
    def  int_to_symbol(i:int) -> str:
        if i in Tokenization.table_int_symbol:
            return Tokenization.table_int_symbol[i]
        else:
            return "erro"

    @staticmethod
    def  ints_to_symbols(ints:list[int]) -> list[str]:
        list = []
        for i in ints:
            list.append(Tokenization.int_to_symbol(i))
        return list

    @staticmethod
    def  ints_to_script(ints:list[int]) -> str:
        list = Tokenization.ints_to_symbols(ints)
        script =Tokenization.symbols_to_scrit(list)
        return script

    @staticmethod
    def symbols_to_scrit(symbol_list : list[str]) -> str:
        s=""
        for sl in symbol_list:
            if s=="":
                s+=sl
            elif sl=="<pad>":
                return s
            else:
                s+="|"+sl

        return s
    



def test0():
    s = "for(Unit u){|u.train(|Barracks|EnemyDir|20|)|u.train(|Ranged|EnemyDir|7|)|u.build(|Ranged|EnemyDir|20|)|u.build(|Ranged|Right|100|)|}endFor"
    print(Tokenization.script_to_int(s))

def test1():
    arq = open("./Scripts.txt","r")
    for l in arq.readlines():
        l=l.rstrip("\n")
        print(Tokenization.script_to_int(l))
    arq.close()

def test2():
    arq = open("./Scripts.txt","r")
    for l in arq.readlines():
        l=l.rstrip("\n")
        symbols = l.split("|")
        script =  Tokenization.symbols_to_scrit(symbols);
        if script != l:
            print("erro")
            print(l)
            print(script)
            arq.close()
            return

    
    arq.close()


def test3():
    arq = open("./Scripts.txt","r")
    for l in arq.readlines():
        l=l.rstrip("\n")
        ints =  Tokenization.script_to_int(l)
        script = Tokenization.ints_to_script(ints)

        if script != l:
            print("erro")
            print(l)
            print(script)
            arq.close()
            return

    
    arq.close()


if __name__== '__main__':
    test3()
   