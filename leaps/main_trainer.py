
import sys
sys.path.append("../")
import torch
from leaps.config.config import Config
from module.MicroRTS_Dataset import MicroRTS_Dataset,get_train_test,get_train_test2
from torch.utils.data import Dataset, DataLoader
from logger.stdout_logger import StdoutLogger
from module.test_embedding import leaps_vae_MicroRTS
from module.trainer import Trainer


if __name__ == '__main__':

    if Config.disable_gpu:
        device = torch.device('cpu')
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    StdoutLogger.log('Main', f'Starting trainer for model vae_microRTS')
    StdoutLogger.log('Main', f'device {device}')
    torch_rng = torch.Generator().manual_seed(Config.env_seed)
   
    model = leaps_vae_MicroRTS(device)
    model.to(device)
    train, test = get_train_test(device)
    dataloaderTrain = DataLoader(train,batch_size=Config.data_batch_size, shuffle=True, drop_last=True, generator=torch_rng)
    dataloaderTest = DataLoader(test,batch_size=Config.data_batch_size, shuffle=True, drop_last=True, generator=torch_rng)
   
   
    trainer = Trainer(model)
    trainer.train(dataloaderTrain,dataloaderTest)
    
    
    
  
    StdoutLogger.log('Main', f'Terninou')
