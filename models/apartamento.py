from .imovel import Imovel

class Apartamento(Imovel):
    def __init__(self, id_imovel, endereco, valor, andar, elevador=True):
        super().__init__(id_imovel, endereco, valor)
        self.__andar = andar
        self.__elevador = elevador

    @property
    def andar(self):
        return self.__andar

    @property
    def elevador(self):
        return self.__elevador

    def to_dict(self):
        data = super().to_dict()
        data["andar"] = self.__andar
        data["elevador"] = self.__elevador
        data["tipo"] = "Apartamento"
        return data