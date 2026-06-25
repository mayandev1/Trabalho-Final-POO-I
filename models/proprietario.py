from .pessoa import Pessoa

class Proprietario(Pessoa):
    def __init__(self, id_pessoa, nome, cpf, telefone):
        super().__init__(id_pessoa, nome, cpf, telefone)

    def to_dict(self):
        data = super().to.dict()
        data["tipo"] = "Proprietario"
        return data