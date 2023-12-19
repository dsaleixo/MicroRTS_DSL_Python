

import torch
from torch.utils.data import Dataset
import numpy as np
import math
from leaps.config.config import Config

from  leaps.module.tolkerinze import Tokenization
from sklearn.model_selection import train_test_split


def get_train_test(device ):
    arq = open("./module/Scripts.txt","r")
    programs = []
    for l in arq.readlines():
    
        script = l.rstrip("\n")
        list_token = Tokenization.script_to_int(script)
        list_token+=[Tokenization.symbol_to_tokens('<pad>') for _ in range(Config.data_max_program_len-len(list_token))]
        programs.append( torch.tensor(list_token, dtype =torch.long,device=device))
    arq.close()
    train,test = train_test_split(programs,train_size=1000,test_size=400,random_state=42)
    #train,test = train_test_split(programs,test_size=0.15,random_state=42)
    Dataset_train = MicroRTS_Dataset(train)
    Dataset_test = MicroRTS_Dataset(test)
    return Dataset_train,Dataset_test


def get_train_test2(device):
    s0 ="for(Unit u){|u.train(|Worker|EnemyDir|15|)|u.build(|Light|EnemyDir|9|)|u.train(|Light|Up|10|)|u.train(|Ranged|Right|20|)|u.train(|Barracks|EnemyDir|3|)|}endFor"
    s1 ="for(Unit u){|u.build(|Ranged|Up|2|)|u.train(|Base|Right|2|)|u.build(|Ranged|Up|20|)|u.train(|Heavy|Down|100|)|u.train(|Worker|Right|20|)|}endFor"
    s2 ="for(Unit u){|u.train(|Ranged|Right|0|)|u.build(|Worker|Up|9|)|u.build(|Light|Up|0|)|u.train(|Light|Down|3|)|u.harvest(|50|)|}endFor"
    s3 = "for(Unit u){|u.train(|Barracks|Left|5|)|u.train(|Heavy|Down|1|)|u.train(|Light|EnemyDir|8|)|}endFor"
    progs = [s0,s1,s2,s3]
    lista_tensores = []
    for prog in progs:
        list_token = Tokenization.script_to_int(prog)
        list_token+=[Tokenization.symbol_to_tokens('<pad>') for _ in range(Config.data_max_program_len-len(list_token))]
        lista_tensores.append( torch.tensor(list_token, dtype =torch.long,device=device))
        
    #train,test = train_test_split(programs,test_size=0.25,random_state=42)
    Dataset_train = MicroRTS_Dataset(lista_tensores)
    Dataset_test = MicroRTS_Dataset(lista_tensores)
    return Dataset_train,Dataset_test

    
class MicroRTS_Dataset(Dataset):

    def __init__(self,data):
        
        arq = open("./module/Scripts.txt","r")
        
        self.input_program = torch.stack( [torch.tensor(x) for x in  data])
        
       
        self.n_samples = self.input_program.shape[0]
        print(self.input_program.shape)

    def __getitem__(self,index):
        return self.input_program[index]
    
    def __len__(self):
        return self.n_samples


if __name__== '__main__':
    dataset = MicroRTS_Dataset()
    print(len(dataset))
