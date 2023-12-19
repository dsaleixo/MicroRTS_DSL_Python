from typing import Annotated

class Config:
    """Class that handles the project global configuration.
    """

    experiment_name: Annotated[str, 'Name of the model, used for saving output.'] = 'program_vae_microRTS_0'

    disable_gpu: Annotated[bool, 'Disable GPU, even if available. Useful for debugging.'] = False

   
    trainer_prog_loss_coef: Annotated[float, 'Weight of program classification loss.'] = 1.0
    trainer_latent_loss_coef: Annotated[float, 'Weight of VAE KL Divergence Loss.'] = 0.1
    env_seed: Annotated[int, 'Seed for random environment generation.'] = 1
    
    model_hidden_size: Annotated[int, 'Number of dimensions in VAE hidden unit.'] = 128
    model_name: Annotated[str, 'Class name of the VAE model.'] = 'LeapsVAE'
    
    data_max_program_len: Annotated[int, 'Maximum program length in number of tokens.'] = 70
    embedding_dim:  Annotated[int, 'embedding_dim:.'] = 46
    data_batch_size: Annotated[int, 'Batch size used in VAE training.'] = 256
    trainer_num_epochs: Annotated[int, 'trainer_num_epochs.'] = 10000000
    trainer_optim_lr: Annotated[float, 'Adam optimizer learning rate.'] = 5e-4
    