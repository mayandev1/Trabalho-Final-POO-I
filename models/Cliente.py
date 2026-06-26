from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, cpf, telefone, email)

    @classmethod
    def from_dict(cls, dados):
        return cls(dados.get("nome", ""), dados.get("cpf", ""), dados.get("telefone", ""), dados.get("email", ""))
