import numpy as np
import torch
from torch import nn

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from leaps.module.tolkerinze import Tokenization
from leaps.module.syntax_checker_microRTS import SyntaxCheckerMicroRTS
from leaps.config.config import Config

def init(module, weight_init, bias_init, gain=1.):
    weight_init(module.weight.data, gain=gain)
    bias_init(module.bias.data)
    return module

def init_gru(module: torch.nn.GRU):
    for name, param in module.named_parameters():
        if 'bias' in name:
            nn.init.constant_(param, 0)
        elif 'weight' in name:
            nn.init.orthogonal_(param)


class leaps_vae_MicroRTS(nn.Module):
    
    def __init__(self,device):
        super().__init__()
        self.cont=0
        self.device = device
        self.max_program_length = Config.data_max_program_len
        self.num_program_tokens = Tokenization.tableSize() 
        
        self.init_ = lambda m: init(m, nn.init.orthogonal_, lambda x: nn.init.
                                    constant_(x, 0), nn.init.calculate_gain('relu'))
        
        
        #encode
        self.token_encoder = nn.Embedding(self.num_program_tokens, Config.embedding_dim,device=device)
        
        
        
        # Z
        self.hidden_size = Config.model_hidden_size
        self.encoder_gru = nn.GRU(Config.embedding_dim, self.hidden_size,device=device)

        
        
        #decoder
        self.decoder_gru = nn.GRU(self.hidden_size + Config.embedding_dim, self.hidden_size,device=device)
        self.decoder_mlp = nn.Sequential(
            self.init_(nn.Linear(2 * self.hidden_size + Config.embedding_dim, self.hidden_size)),
            nn.Tanh(), self.init_(nn.Linear(self.hidden_size, self.num_program_tokens))
        )
        self.softmax = nn.LogSoftmax(dim=-1)
        
         # Encoder VAE utils
        self.encoder_mu = torch.nn.Linear(self.hidden_size, self.hidden_size)
        self.encoder_log_sigma = torch.nn.Linear(self.hidden_size, self.hidden_size)
       
      
        
        
        
    def get_syntax_mask(self, batch_size: int, current_tokens: torch.Tensor, grammar_state: list, first:bool):
       
        out_of_syntax_mask = torch.zeros((batch_size, self.num_program_tokens), dtype=torch.float32, device=self.device)
        out_of_syntax_mask[:,:]=-torch.finfo(torch.float32).max 
       
        for i in range (batch_size):
            if first:
                resp =grammar_state[i].Valid_Next_Symblo(None)
            else:
                resp =grammar_state[i].Valid_Next_Symblo(Tokenization.table_int_symbol[current_tokens[i].item()])
            for x in resp:
              
                out_of_syntax_mask[i][Tokenization.table_symbol_int[x]]=0
       # print(out_of_syntax_mask)
        return out_of_syntax_mask
    
    def get_latent_loss(self):
        mean_sq = self.z_mu * self.z_mu
        stddev_sq = self.z_sigma * self.z_sigma
        return 0.5 * torch.mean(mean_sq + stddev_sq - torch.log(stddev_sq) - 1)

    def forward(self,X:torch.Tensor,prog_teacher_enforcing) -> torch.Tensor:
        self.cont+=1
        prog_mask = (X != 45)
        z = self.encode(X,prog_mask)
        return  self.decode(z,X,prog_mask,prog_teacher_enforcing)
        



    def encode(self,X:torch.Tensor,prog_mask: torch.Tensor):
     
        progs_len = prog_mask.squeeze(-1).sum(dim=-1).cpu()
        
        enc_progs = self.token_encoder(X)
        
        
        packed_inputs = nn.utils.rnn.pack_padded_sequence(
            enc_progs, progs_len, batch_first=True, enforce_sorted=False)
        
        _, enc_hidden_state = self.encoder_gru(packed_inputs)
        enc_hidden_state = enc_hidden_state.squeeze(0)
    
        return self.sample_latent_vector(enc_hidden_state)
    
    def sample_latent_vector(self, enc_hidden_state: torch.Tensor) -> torch.Tensor:
        # Sampling z with reperameterization trick
        mu = self.encoder_mu(enc_hidden_state)
        log_sigma = self.encoder_log_sigma(enc_hidden_state)
        sigma = torch.exp(log_sigma)
        std_z = torch.randn(sigma.size(), device=self.device)
        
        z = mu + sigma * std_z
        
        self.z_mu = mu
        self.z_sigma = sigma
        
        return z
    
    def decode(self, z: torch.Tensor, progs: torch.Tensor, progs_mask: torch.Tensor,
               prog_teacher_enforcing = True):
        
        
        
        
        batch_size, _ = z.shape
        #print(z.shape)
        gru_hidden_state = z.unsqueeze(0)
        # Initialize tokens as DEFs
        current_tokens = torch.zeros((batch_size), dtype=torch.long, device=self.device)
        
        grammar_state = [SyntaxCheckerMicroRTS()
                         for _ in range(batch_size)]
        
        pred_progs = []
        pred_progs_logits = []
        
        for i in range(0, self.max_program_length):
        
            token_embedding = self.token_encoder(current_tokens)
            gru_inputs = torch.cat((token_embedding, z), dim=-1)
            gru_inputs = gru_inputs.unsqueeze(0)
            
            gru_output, gru_hidden_state = self.decoder_gru(gru_inputs, gru_hidden_state)
       
            mlp_input = torch.cat([gru_output.squeeze(0), token_embedding, z], dim=1)
            
            pred_token_logits = self.decoder_mlp(mlp_input)
            
            syntax_mask = self.get_syntax_mask(batch_size, current_tokens, grammar_state,i==0)
            
            pred_token_logits += syntax_mask
            
            pred_tokens = self.softmax(pred_token_logits).argmax(dim=-1)
            
            
            pred_progs.append(pred_tokens)
            pred_progs_logits.append(pred_token_logits)
         
            if prog_teacher_enforcing :
                
                # Enforce next token with ground truth
                #current_tokens = pred_tokens.view(batch_size)
                current_tokens = progs[:, i].view(batch_size)
               
            else:
                # Pass current prediction to next iteration
                
                current_tokens = pred_tokens.view(batch_size)
        '''    
        for b in range(batch_size):
            for t in pred_progs:
                s =Tokenization.table_int_symbol[t[b].item()]
                if s != "<pad>":
                    print(s,end= " ")
                else:
                    break
            print()
            print()
        '''
        pred_progs = torch.stack(pred_progs, dim=1)
        pred_progs_logits = torch.stack(pred_progs_logits, dim=1)
        pred_progs_masks = (pred_progs != self.num_program_tokens - 1)
        
        
    
        return pred_progs, pred_progs_logits, pred_progs_masks
        
        
    def encode_program(self, prog: torch.Tensor):
        if prog.dim() == 1:
            prog = prog.unsqueeze(0)
        
        prog_mask = (prog != 45)
        
        z = self.encode(prog, prog_mask)
        
        return z
    
    def decode_vector(self, z: torch.Tensor):
        if z.dim() == 1:
            z = z.unsqueeze(0)
        pred_progs, _, pred_progs_masks = self.decode(z, None,None,False)
        pred_progs_tokens = []
        for prog, prog_mask in zip(pred_progs, pred_progs_masks):
            pred_progs_tokens.append(prog[prog_mask].cpu().numpy().tolist())
        
        return pred_progs_tokens
    
def test0():
    lvmRTS = leaps_vae_MicroRTS()
   
    s0 ="for(Unit u){|u.train(|Worker|EnemyDir|15|)|u.build(|Light|EnemyDir|9|)|u.train(|Light|Up|10|)|u.train(|Ranged|Right|20|)|u.train(|Barracks|EnemyDir|3|)|}endFor"
    s1 ="for(Unit u){|u.build(|Ranged|Up|2|)|u.train(|Base|Right|2|)|u.build(|Ranged|Up|20|)|u.train(|Heavy|Down|100|)|u.train(|Worker|Right|20|)|}endFor"
    s2 ="for(Unit u){|u.train(|Ranged|Right|0|)|u.build(|Worker|Up|9|)|u.build(|Light|Up|0|)|u.train(|Light|Down|3|)|u.harvest(|50|)|}endFor"
    s3 = "for(Unit u){|u.train(|Barracks|Left|5|)|u.train(|Heavy|Down|1|)|u.train(|Light|EnemyDir|8|)|}endFor"
    progs = [s0,s1,s2,s3]
    lista_tensores = []
    for prog in progs:
        list_token = Tokenization.script_to_int(prog)
        list_token+=[Tokenization.symbol_to_tokens('<pad>') for _ in range(Config.data_max_program_len-len(list_token))]
        lista_tensores.append( torch.tensor(list_token, dtype =torch.int))
        
    tensores = torch.stack(lista_tensores)
    
   
  
    lvmRTS.eval()
    with torch.inference_mode():
        print(tensores.shape)
        lvmRTS(tensores)
       
   
if __name__== '__main__':
    test0()