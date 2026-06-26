from datetime import datetime
from models import Cliente, Proprietario, Casa, Apartamento
from .validacoes import Validacoes


class Imobiliaria:
    def __init__(self):
        self.clientes = []
        self.proprietarios = []
        self.imoveis = []
        self.negociacoes = []

    def cadastrar_cliente(self, nome, cpf, telefone, email):
        cpf = Validacoes.validar_cpf(cpf)
        if self.buscar_cliente_por_cpf(cpf):
            raise ValueError("Já existe cliente com este CPF.")
        cliente = Cliente(
            Validacoes.campo_obrigatorio(nome, "nome"), cpf,
            Validacoes.validar_telefone(telefone), Validacoes.validar_email(email)
        )
        self.clientes.append(cliente)
        return cliente

    def cadastrar_proprietario(self, nome, cpf, telefone, email):
        cpf = Validacoes.validar_cpf(cpf)
        if self.buscar_proprietario_por_cpf(cpf):
            raise ValueError("Já existe proprietário com este CPF.")
        proprietario = Proprietario(
            Validacoes.campo_obrigatorio(nome, "nome"), cpf,
            Validacoes.validar_telefone(telefone), Validacoes.validar_email(email)
        )
        self.proprietarios.append(proprietario)
        return proprietario

    def cadastrar_casa(self, proprietario_cpf, endereco, cidade, modalidade, valor, metragem, piscina, data_cadastro=None):
        proprietario_cpf = Validacoes.validar_cpf(proprietario_cpf)
        if not self.buscar_proprietario_por_cpf(proprietario_cpf):
            raise ValueError("Proprietário não encontrado.")
        endereco = Validacoes.campo_obrigatorio(endereco, "endereço")
        cidade = Validacoes.campo_obrigatorio(cidade, "cidade")
        self._validar_imovel_duplicado(endereco, cidade)
        casa = Casa(
            proprietario_cpf, endereco, cidade,
            Validacoes.validar_modalidade(modalidade),
            Validacoes.validar_float(valor, "valor"),
            Validacoes.validar_float(metragem, "metragem"),
            bool(piscina), data_cadastro or datetime.now().strftime("%d/%m/%Y")
        )
        self.imoveis.append(casa)
        return casa

    def cadastrar_apartamento(self, proprietario_cpf, endereco, cidade, modalidade, valor, metragem, andar, numero_apartamento, data_cadastro=None):
        proprietario_cpf = Validacoes.validar_cpf(proprietario_cpf)
        if not self.buscar_proprietario_por_cpf(proprietario_cpf):
            raise ValueError("Proprietário não encontrado.")
        endereco = Validacoes.campo_obrigatorio(endereco, "endereço")
        cidade = Validacoes.campo_obrigatorio(cidade, "cidade")
        self._validar_imovel_duplicado(endereco, cidade)
        ap = Apartamento(
            proprietario_cpf, endereco, cidade,
            Validacoes.validar_modalidade(modalidade),
            Validacoes.validar_float(valor, "valor"),
            Validacoes.validar_float(metragem, "metragem"),
            Validacoes.validar_int(andar, "andar"),
            Validacoes.campo_obrigatorio(numero_apartamento, "número do apartamento"),
            data_cadastro or datetime.now().strftime("%d/%m/%Y")
        )
        self.imoveis.append(ap)
        return ap

    def realizar_negociacao(self, codigo_imovel, cpf_cliente):
        imovel = self.buscar_imovel_por_codigo(codigo_imovel)
        if not imovel:
            raise ValueError("Imóvel não encontrado.")
        cliente = self.buscar_cliente_por_cpf(cpf_cliente)
        if not cliente:
            raise ValueError("Cliente não encontrado.")
        imovel.negociar(cliente.cpf)
        negociacao = {
            "codigo_imovel": imovel.codigo,
            "cpf_cliente": cliente.cpf,
            "nome_cliente": cliente.nome,
            "modalidade": imovel.modalidade,
            "valor": imovel.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.negociacoes.append(negociacao)
        return negociacao

    def buscar_cliente_por_cpf(self, cpf):
        cpf = ''.join(ch for ch in str(cpf) if ch.isdigit())
        return next((c for c in self.clientes if c.cpf == cpf), None)

    def buscar_proprietario_por_cpf(self, cpf):
        cpf = ''.join(ch for ch in str(cpf) if ch.isdigit())
        return next((p for p in self.proprietarios if p.cpf == cpf), None)

    def buscar_imovel_por_codigo(self, codigo):
        try:
            codigo = int(codigo)
        except ValueError:
            return None
        return next((i for i in self.imoveis if i.codigo == codigo), None)

    def listar_imoveis_disponiveis(self):
        return [i for i in self.imoveis if i.disponivel]

    def listar_imoveis_negociados(self):
        return [i for i in self.imoveis if not i.disponivel]

    def buscar_imoveis(self, cidade=None, tipo=None, modalidade=None, disponivel=None, ano=None, valor_min=None, valor_max=None):
        resultado = self.imoveis
        if cidade:
            resultado = [i for i in resultado if i.cidade.lower() == cidade.lower()]
        if tipo:
            resultado = [i for i in resultado if i.__class__.__name__.lower() == tipo.lower()]
        if modalidade:
            resultado = [i for i in resultado if i.modalidade.lower() == modalidade.lower()]
        if disponivel is not None:
            resultado = [i for i in resultado if i.disponivel == disponivel]
        if ano:
            resultado = [i for i in resultado if i.data_cadastro.endswith(str(ano))]
        if valor_min is not None:
            resultado = [i for i in resultado if i.valor >= float(valor_min)]
        if valor_max is not None:
            resultado = [i for i in resultado if i.valor <= float(valor_max)]
        return resultado

    def _validar_imovel_duplicado(self, endereco, cidade):
        for imovel in self.imoveis:
            if imovel.endereco.strip().lower() == endereco.strip().lower() and imovel.cidade.strip().lower() == cidade.strip().lower():
                raise ValueError("Imóvel duplicado: já existe imóvel com o mesmo endereço e cidade.")

    def to_dict(self):
        return {
            "clientes": [c.to_dict() for c in self.clientes],
            "proprietarios": [p.to_dict() for p in self.proprietarios],
            "imoveis": [i.to_dict() for i in self.imoveis],
            "negociacoes": self.negociacoes
        }

    @classmethod
    def from_dict(cls, dados):
        from models import Imovel, Casa
        Imovel._proximo_codigo = 1
        Casa.total_com_piscina = 0
        obj = cls()
        obj.clientes = [Cliente.from_dict(c) for c in dados.get("clientes", [])]
        obj.proprietarios = [Proprietario.from_dict(p) for p in dados.get("proprietarios", [])]
        for item in dados.get("imoveis", []):
            if item.get("tipo") == "casa":
                obj.imoveis.append(Casa.from_dict(item))
            elif item.get("tipo") == "apartamento":
                obj.imoveis.append(Apartamento.from_dict(item))
        obj.negociacoes = dados.get("negociacoes", [])
        return obj
