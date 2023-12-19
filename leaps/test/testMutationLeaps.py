import torch
from leaps.module.build_ast import BuildAst

from leaps.module.test_embedding import leaps_vae_MicroRTS
from leaps.module.tolkerinze import Tokenization
from synthesis.baseDSL.util.factory_Base import Factory_Base


class TestMutationLeaps():
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def test0():
        
        if torch.cuda.is_available():
            device = torch.device('cpu')
        else:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        model = leaps_vae_MicroRTS(device)
        z = torch.randn((1,128))
        #print(z)
        prog = model.decode_vector(z)
        print(prog)
        script = Tokenization.ints_to_script(prog[0])
        print(script)
        
    @staticmethod
    def test1():
    
        if torch.cuda.is_available():
            device = torch.device('cpu')
        else:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        model = leaps_vae_MicroRTS(device)
        params = torch.load("leaps/models/01_pytorch_model", map_location=device)
        model.load_state_dict(params, strict=False)
        prog = "for(Unit u){|u.build(|Ranged|Left|4|)|u.idle()|u.train(|Ranged|Up|25|)|u.harvest(|20|)|u.harvest(|25|)|u.idle()|u.harvest(|4|)|u.moveAway()|u.idle()|u.idle()|}endFor"
        list_token = Tokenization.script_to_int(prog)
        list_token+=[Tokenization.symbol_to_tokens('<pad>') for _ in range(70)]
        tensor = torch.tensor(list_token, dtype =torch.long,device=device)
        
        
        print(prog)
        model.eval()
        with torch.inference_mode():
            z = model.encode_program(tensor)
            
            prog = model.decode_vector(z)
            script = Tokenization.ints_to_script(prog[0])
            b_ast = BuildAst(Factory_Base())
            ast = b_ast.build(script)
            print(ast.translate())
            
    @staticmethod
    def test2():
    
        if torch.cuda.is_available():
            device = torch.device('cpu')
        else:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        
        model = leaps_vae_MicroRTS(device)
        params = torch.load("leaps/models/01_pytorch_model", map_location=device)
        model.load_state_dict(params, strict=False)
        prog = "for(Unit u){|u.build(|Ranged|Left|4|)|u.idle()|u.train(|Ranged|Up|25|)|u.harvest(|20|)|u.harvest(|25|)|u.idle()|u.harvest(|4|)|u.moveAway()|u.idle()|u.idle()|}endFor"
        list_token = Tokenization.script_to_int(prog)
        list_token+=[Tokenization.symbol_to_tokens('<pad>') for _ in range(70)]
        tensor = torch.tensor(list_token, dtype =torch.long,device=device)
        
        model.eval()
        with torch.inference_mode():
            z = model.encode_program(tensor)
            print(prog)
            print()
            print()
            
            for _ in range(5):
                novo = z + torch.rand_like(z)*1.0
                prog = model.decode_vector(novo)
                script = Tokenization.ints_to_script(prog[0])
                b_ast = BuildAst(Factory_Base())
                ast = b_ast.build(script)
                print(ast.translate2())
                print()
                