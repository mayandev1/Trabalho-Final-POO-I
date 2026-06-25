from .imovel import Imovel

class Casa(Imovel):
    def __init__(self, id_imovel, endereco, valor, quartos, area):
        super().__init__(id_imovel, endereco, valor)
        self.__quartos = quartos
        self.__area = area

    @property
    def quartos(self):
        return self.__quartos
    
    @property
    def area(self):
        return self.__area
    
    def to_dict(self):
        data = super().to_dict()
        data["quartos"] = self.__quartos
        data["area"] = self.__area
        data["tipo"] = "Casa"
        return data