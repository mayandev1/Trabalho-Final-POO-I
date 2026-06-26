from .pessoa import Pessoa


class Proprietario(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, cpf, telefone, email)

    @classmethod
    def from_dict(cls, dados):
        return cls(dados.get("nome", ""), dados.get("cpf", ""), dados.get("telefone", ""), dados.get("email", ""))

    @staticmethod
    def deletar_proprietario(lista_proprietarios, cpf):
        for proprietario in lista_proprietarios:
            if proprietario.cpf == cpf:
                lista_proprietarios.remove(proprietario)
                return True
        return False