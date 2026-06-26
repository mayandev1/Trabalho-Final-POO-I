from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, cpf, telefone, email)

    @classmethod
    def from_dict(cls, dados):
        return cls(dados.get("nome", ""), dados.get("cpf", ""), dados.get("telefone", ""), dados.get("email", ""))
    
    @staticmethod
    def deletar_cliente(lista_clientes, cpf):
        for cliente in lista_clientes:
            if cliente.cpf == cpf:
                lista_clientes.remove(cliente)
                return True
        return False
