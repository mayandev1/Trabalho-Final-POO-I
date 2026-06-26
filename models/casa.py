from .imovel import Imovel


class Casa(Imovel):
    total_com_piscina = 0

    def __init__(self, proprietario_cpf, endereco, cidade, modalidade, valor, metragem,
                 piscina=False, data_cadastro=None, disponivel=True, cliente_cpf=None, codigo=None):
        super().__init__(proprietario_cpf, endereco, cidade, modalidade, valor, metragem,
                         data_cadastro, disponivel, cliente_cpf, codigo)
        self.piscina = bool(piscina)
        if self.piscina:
            Casa.total_com_piscina += 1

    def calcular_taxa_administrativa(self):
        if self.metragem <= 300:
            return self.metragem * 0.10
        return self.metragem * 0.20

    @classmethod
    def quantidade_com_piscina(cls):
        return cls.total_com_piscina

    def to_dict(self):
        dados = self.to_dict_base()
        dados.update({"tipo": "casa", "piscina": self.piscina})
        return dados

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados.get("proprietario_cpf", ""), dados.get("endereco", ""), dados.get("cidade", ""),
            dados.get("modalidade", "venda"), dados.get("valor", 0), dados.get("metragem", 0),
            dados.get("piscina", False), dados.get("data_cadastro"), dados.get("disponivel", True),
            dados.get("cliente_cpf"), dados.get("codigo")
        )
