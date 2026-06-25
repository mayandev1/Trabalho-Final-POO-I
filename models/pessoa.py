class Pessoa:
    def __init__(self, id_pessoa, nome, cpf, telefone):
        self.__id = id_pessoa
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    @property
    def id(self):
        return self._id
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def cpf(self):
        return self.__cpf
        
    @property
    def telefone(self):
        return self.__telefone
        
    def to_dict(self):
        return{
            "Id" : self.__id,
            "Nome" : self.__nome,
            "CPF" : self.__cpf,
            "Telefone" : self.__telefone
            }