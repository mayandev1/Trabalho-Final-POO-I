from .imovel import Imovel


class Apartamento(Imovel):
    def __init__(self, proprietario_cpf, endereco, cidade, modalidade, valor, metragem,
                 andar, numero_apartamento, data_cadastro=None, disponivel=True, cliente_cpf=None, codigo=None):
        super().__init__(proprietario_cpf, endereco, cidade, modalidade, valor, metragem,
                         data_cadastro, disponivel, cliente_cpf, codigo)
        self.andar = int(andar)
        self.numero_apartamento = str(numero_apartamento)

    def calcular_taxa_administrativa(self):
        if self.metragem <= 50:
            return self.metragem * 0.08
        return self.metragem * 0.10

    def to_dict(self):
        dados = self.to_dict_base()
        dados.update({"tipo": "apartamento", "andar": self.andar, "numero_apartamento": self.numero_apartamento})
        return dados

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados.get("proprietario_cpf", ""), dados.get("endereco", ""), dados.get("cidade", ""),
            dados.get("modalidade", "venda"), dados.get("valor", 0), dados.get("metragem", 0),
            dados.get("andar", 0), dados.get("numero_apartamento", ""), dados.get("data_cadastro"),
            dados.get("disponivel", True), dados.get("cliente_cpf"), dados.get("codigo")
        )
