import json
import os

ARQ = "data/banco.json"

class Persistencia:
    @staticmethod
    def carregar():
        if not os.path.exists(ARQ):
            return{
                "Clientes" : [],
                "Proprietarios" : [],
                "Imoveis" : [],
                "Negociacoes" : []
            }
        
        with open(ARQ, "r", encoding="utf-8") as f:
            return json.load(f)
    
    @staticmethod
    def salvar(dados):
        with open(ARQ, "w", encoding="utf-8") as f:
            json.dump(dados, f,indent=4, ensure_ascii=False)