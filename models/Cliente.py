from .pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, id_pessoa, nome, cpf, telefone, interesse):
        super().__init__(id_pessoa, nome, cpf, telefone)
        self.__interesse = interesse

    @property
    def interesse(self):
        return self.__interesse
    
    def to_dict(self):
        data = super().to_dict()
        data["interesse"] = self.__interesse
        data["tipo"] =  "Cliente"
        return data