from datetime import datetime


class Imovel:
    _proximo_codigo = 1

    def __init__(self, proprietario_cpf, endereco, cidade, modalidade, valor, metragem,
                 data_cadastro=None, disponivel=True, cliente_cpf=None, codigo=None):
        if codigo is None:
            self.codigo = Imovel._proximo_codigo
            Imovel._proximo_codigo += 1
        else:
            self.codigo = int(codigo)
            if self.codigo >= Imovel._proximo_codigo:
                Imovel._proximo_codigo = self.codigo + 1

        self.proprietario_cpf = proprietario_cpf
        self.endereco = endereco
        self.cidade = cidade
        self.modalidade = modalidade.lower()
        self.valor = float(valor)
        self.metragem = float(metragem)
        self.data_cadastro = data_cadastro or datetime.now().strftime("%d/%m/%Y")
        self.disponivel = disponivel
        self.cliente_cpf = cliente_cpf

    def calcular_taxa_administrativa(self):
        raise NotImplementedError("Método deve ser sobrescrito nas subclasses.")

    def negociar(self, cliente_cpf):
        if not self.disponivel:
            raise ValueError("Este imóvel já foi negociado.")
        self.disponivel = False
        self.cliente_cpf = cliente_cpf

    def to_dict_base(self):
        return {
            "codigo": self.codigo,
            "proprietario_cpf": self.proprietario_cpf,
            "endereco": self.endereco,
            "cidade": self.cidade,
            "modalidade": self.modalidade,
            "valor": self.valor,
            "metragem": self.metragem,
            "data_cadastro": self.data_cadastro,
            "disponivel": self.disponivel,
            "cliente_cpf": self.cliente_cpf
        }

    def __str__(self):
        status = "Disponível" if self.disponivel else "Negociado"
        return (f"Código: {self.codigo} | {self.__class__.__name__} | {self.endereco}, {self.cidade} | "
                f"{self.modalidade.title()} | R$ {self.valor:.2f} | {self.metragem:.2f} m² | {status}")
