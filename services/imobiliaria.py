from .persistencia import Persistencia

class Imobiliaria:
    def __init__(self, nome="Lopes Imóveis"):
        self.__nome = nome
        self.__dados = Persistencia.carregar()

    @property
    def nome(self):
        return self.__nome
    
    def adicionar_cliente(self, cliente):
        self.__dados["Clientes"].append(cliente.to_dict())
        Persistencia.salvar(self.__dados)

    def adicionar_proprietario(self, prop):
        self.__dados["Proprietarios"].append(prop.to_dict())
        Persistencia.salvar(self.__dados)

    def adicionar_imovel(self, imovel):
        self.__dados["Imoveis"].append(imovel.to_dict())
        Persistencia.salvar(self.__dados)

    def listar_imoveis(self):
        return self.__dados["Imoveis"]
    
    def listar_disponiveis(self):
        return [i for i in self.__dados["Imoveis"] if i["status"] == "disponivel"]
    
    def resumo(self):
        return{
            "imobiliaria" : self.__nome,
            "clientes" : len(self.__dados["Clientes"]),
            "proprietarios" : len(self.__dados["Proprietarios"]),
            "imoveis": len(self.__dados["Imoveis"])
        }