class Imovel:
    def __init__(self, id_imovel, endereco, valor, status="disponivel"):
        self.__id = id_imovel
        self.__endereco = endereco
        self.__valor = valor
        self.__status = status

    @property
    def id(self):
        return self.__id

    @property
    def endereco(self):
        return self.__endereco

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor

    def to_dict(self):
        return {
            "id": self.__id,
            "endereco": self.__endereco,
            "valor": self.__valor,
            "status": self.__status
        }