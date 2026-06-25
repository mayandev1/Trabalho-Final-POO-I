import re

class Validacoes:
    @staticmethod
    def validar_cpf(cpf):
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11:
            return False
        
        if cpf == cpf[0] * 11:
            return False
        
        return True
    

    @staticmethod
    def validar_telefone(telefone):
        telefone = re.sub(r'\D', '', telefone)
        return len(telefone) in [10,11]
    
    @staticmethod
    def validar_valor(valor):
        try:
            valor = float(valor)
            return valor > 0
        except:
            return False
        
    @staticmethod
    def validar_id(id_valor):
        return isinstance(id_valor, int) and id_valor > 0