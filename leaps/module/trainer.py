import numpy as np
import torch
from torch import nn
from typing import NamedTuple
from torch.utils.data import DataLoader,Dataset
import sys
from logger.stdout_logger import StdoutLogger
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from pathlib import Path

from leaps.module.tolkerinze import Tokenization
from leaps.module.MicroRTS_Dataset import MicroRTS_Dataset
from leaps.module.test_embedding import leaps_vae_MicroRTS
from config.config import Config

class EpochReturn(NamedTuple):
    
    mean_total_loss: float
    mean_progs_loss: float
    mean_latent_loss: float
    mean_progs_t_accuracy: float
    mean_progs_s_accuracy: float
   
  

class Trainer:
    
    def __init__(self, model: leaps_vae_MicroRTS):
        self.model = model
        self.latent_loss_coef = Config.trainer_latent_loss_coef
        self.prog_loss_coef = Config.trainer_prog_loss_coef
        self.num_epochs = Config.trainer_num_epochs
        self.device = self.model.device
        self.optimizer = torch.optim.Adam(
            filter(lambda p: p.requires_grad, self.model.parameters()),
            lr=Config.trainer_optim_lr
        )
        self.scheduler = torch.optim.lr_scheduler.StepLR(
            self.optimizer, step_size=10, gamma=.95
        )
        self.loss_fn = nn.CrossEntropyLoss(reduction='mean')
         # 1. Create models directory 
        MODEL_PATH = Path("models")
        MODEL_PATH.mkdir(parents = True,exist_ok = True)
        # 2. Create model save path 
        MODEL_NAME = "01_pytorch_model"
        self.MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME 
     
     
    def get_latent_loss(self):
        mean_sq = self.z_mu * self.z_mu
        stddev_sq = self.z_sigma * self.z_sigma
        return 0.5 * torch.mean(mean_sq + stddev_sq - torch.log(stddev_sq) - 1)
     
    def _run_batch(self, batch: list, training = True) -> list:
        if training:
            self.model.train()
            torch.set_grad_enabled(True) # prob not needed
        else:
            self.model.eval()
            torch.set_grad_enabled(False) # prob not needed
       
       
        progs = batch
        
        
        output = self.model(progs,training)
        
        pred_progs, pred_progs_logits, pred_progs_masks = output    
        progs_masks = (progs != 45)   
    
        
        if type(progs) == torch.Tensor:
            # Skip first token in ground truth sequences
            progs = progs[:, :].contiguous()
            progs_masks = progs_masks[:, :].contiguous()

            # Flatten everything for loss calculation
            progs_flat = progs.view(-1, 1)
            progs_masks_flat = progs_masks.view(-1, 1)
        
        if pred_progs is not None:
            pred_progs_logits = pred_progs_logits.view(-1, pred_progs_logits.shape[-1])
            pred_progs_masks_flat = pred_progs_masks.view(-1, 1)
            # We combine masks here to penalize predictions that are larger than ground truth
            
            progs_masks_flat_combined = torch.max(progs_masks_flat, pred_progs_masks_flat).squeeze()
            
       
        if training:
            self.optimizer.zero_grad()
                       
         # Calculate classification loss only on tokens in mask
        zero_tensor = torch.tensor([0.0], device=self.device, requires_grad=False)
        progs_loss = zero_tensor
        
        
        
        if pred_progs is not None:
            progs_loss = self.loss_fn(pred_progs_logits[progs_masks_flat_combined],
                                    progs_flat[progs_masks_flat_combined].view(-1))

        #print("ww",progs_flat[progs_masks_flat_combined].view(-1).shape)
        #print("tt",pred_progs_logits[progs_masks_flat_combined].shape)
        #print(progs_loss)
        #print(progs_flat)
        #print(progs.shape)
        
        latent_loss = self.model.get_latent_loss()
        
        total_loss = self.prog_loss_coef * progs_loss + self.latent_loss_coef * latent_loss         
            
            
            
        if training:
            total_loss.backward()
            self.optimizer.step()
            
        with torch.no_grad():
         
            if pred_progs is not None:
                progs_masks_combined = torch.max(progs_masks, pred_progs_masks)
                progs_t_accuracy = (pred_progs[progs_masks_combined] == progs[progs_masks_combined]).float().mean()
                progs_s_accuracy = (progs == pred_progs).min(dim=1).values.float().mean()
             
               
                            
        return [
            total_loss.detach().cpu().numpy().item(),
            progs_loss.detach().cpu().numpy().item(),
   
            latent_loss.detach().cpu().numpy().item(),
            progs_t_accuracy.detach().cpu().numpy().item(),
            progs_s_accuracy.detach().cpu().numpy().item(),
           
        ]                    
        
       
    def _run_epoch(self, dataloader: DataLoader, epoch: int, training = True) -> EpochReturn:
        batch_info_list = np.zeros((len(dataloader), 5))
        
        for batch_idx, batch in enumerate(dataloader):
            batch_info = self._run_batch(batch, training)
            batch_info_list[batch_idx] = batch_info
        
        epoch_info_list = np.mean(batch_info_list, axis=0)
        
        return EpochReturn(*epoch_info_list.tolist())
       
       
        
    def train(self, train_dataloader: DataLoader, val_dataloader: DataLoader):
        if val_dataloader is not None:
            validation_key = 'mean_total_loss'
            best_val_return = np.inf
        
        
        pp=1
        for epoch in range(1, self.num_epochs + 1):
            if epoch%pp==0:
                StdoutLogger.log('Trainer', f'Training epoch {epoch}.')
            
            train_info = self._run_epoch(train_dataloader, epoch, True)
            if epoch%pp==0:
                StdoutLogger.log('TrainerResult', train_info._asdict())
            
 
            if val_dataloader is not None :
                if epoch%pp==0:
                    StdoutLogger.log('Test',f'Validation epoch {epoch}.')
                val_info = self._run_epoch(val_dataloader, epoch, False)
                if epoch%pp==0:
                    StdoutLogger.log('ValidationResult',val_info._asdict())
                
                val_return = val_info._asdict()[validation_key]
 
                if val_return < best_val_return:
                    best_val_return = val_return
                    print('Trainer',f'New best validation {validation_key}: {best_val_return}')
                    torch.save(obj = self.model.state_dict(),f = self.MODEL_SAVE_PATH)

def test0():
    DM = MicroRTS_Dataset()
    model = leaps_vae_MicroRTS()
    trainer = Trainer(model)
    dataloader = DataLoader(DM, batch_size=4)
    
    trainer.train(dataloader,dataloader)
  
    model.eval()

    with torch.inference_mode():
        for batch_idx, batch in enumerate(dataloader):
            output = model(batch)
            print("resposta")
            pred_progs, pred_progs_logits, pred_progs_masks = output  
            print(pred_progs.shape)
            for b in range(len(batch)):
                print(b)
                print("inp = ",Tokenization.ints_to_script(DM[b].tolist()))
                print("out = ", Tokenization.ints_to_script(pred_progs[b].tolist()))
                
                print()
                print()
                    
                    
                    
if __name__== '__main__':
    test0()