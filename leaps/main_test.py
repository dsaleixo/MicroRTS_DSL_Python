import torch
from config import Config
from leaps.module.MicroRTS_Dataset import MicroRTS_Dataset,get_train_test,get_train_test2
from torch.utils.data import Dataset, DataLoader
from logger.stdout_logger import StdoutLogger
from leaps.module.test_embedding import leaps_vae_MicroRTS
from leaps.module.trainer import Trainer


if __name__ == '__main__':

    if Config.disable_gpu:
        device = torch.device('cpu')
    else:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


    StdoutLogger.log('Main', f'Starting trainer for model vae_microRTS')
    StdoutLogger.log('Main', f'device {device}')
    torch_rng = torch.Generator().manual_seed(Config.env_seed)
   
    model = leaps_vae_MicroRTS(device)
    train, test = get_train_test2()
    dataloaderTrain = DataLoader(train,batch_size=Config.data_batch_size, shuffle=True, drop_last=True, generator=torch_rng)
    dataloaderTest = DataLoader(test,batch_size=Config.data_batch_size, shuffle=True, drop_last=True, generator=torch_rng)
   
   
    trainer = Trainer(model)
   
    from pathlib import Path

    # 1. Create models directory 
    MODEL_PATH = Path("models")
    MODEL_PATH.mkdir(parents = True,exist_ok = True)
    # 2. Create model save path 
    MODEL_NAME = "01_pytorch_model"
    MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME 
    # 3. Save the model state dict
    
    model.load_state_dict(torch.load(f = MODEL_SAVE_PATH))
    trainer = Trainer(model)
  
    
    
    
    model.eval()
    with torch.inference_mode():
        val_info = trainer._run_epoch(dataloaderTest, 0, False)
        print('Trainer',val_info._asdict())
   
   
   
   
   
    