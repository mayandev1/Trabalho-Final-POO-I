from collections import Counter
from pathlib import Path
import csv
from models import Casa, Apartamento

class Relatorios:
    def __init__(self, imobiliaria):
        self.imobiliaria = imobiliaria

    # Relatórios básicos

    def media_valor_casas(self) -> float:
       # Retorna a média dos valores das casas cadastradas
        casas = [i for i in self.imobiliaria.imoveis if isinstance(i, Casa)]
        return sum(i.valor for i in casas) / len(casas) if casas else 0

    def media_valor_apartamentos(self) -> float:
        # Retorna a média dos valores dos apartamentos cadastrados
        aps = [i for i in self.imobiliaria.imoveis if isinstance(i, Apartamento)]
        return sum(i.valor for i in aps) / len(aps) if aps else 0

    def quantidade_disponiveis(self) -> int:
        # Retorna a quantidade de imóveis disponíveis
        return len([i for i in self.imobiliaria.imoveis if i.disponivel])

    def quantidade_negociados(self) -> int:
        # Retorna a quantidade de imóveis negociados
        return len([i for i in self.imobiliaria.imoveis if not i.disponivel])

    def quantidade_por_cidade(self) -> dict:
        # Retorna a quantidade de imóveis por cidade
        return dict(Counter(i.cidade for i in self.imobiliaria.imoveis))

    def total_taxas_administrativas(self) -> float:
        # Retorna o total de todas as taxas administrativas
        return sum(i.calcular_taxa_administrativa() for i in self.imobiliaria.imoveis)

    def percentual_casas_com_piscina(self) -> float:
       # Retorna o percentual de casas que possuem piscina
        casas = [i for i in self.imobiliaria.imoveis if isinstance(i, Casa)]
        if not casas:
            return 0
        com_piscina = [c for c in casas if c.piscina]
        return (len(com_piscina) / len(casas)) * 100

    def quantidade_casas_com_piscina(self) -> int:
        # Retorna a quantidade de casas com piscina
        return len([i for i in self.imobiliaria.imoveis if isinstance(i, Casa) and i.piscina])

    def quantidade_por_modalidade(self) -> dict:
        # Retorna a quantidade de imóveis por modalidade (venda/aluguel)
        return dict(Counter(i.modalidade for i in self.imobiliaria.imoveis))

    def quantidade_por_ano(self) -> dict:
        # Retorna a quantidade de imóveis cadastrados por ano
        anos = [i.data_cadastro[-4:] for i in self.imobiliaria.imoveis]
        return dict(Counter(anos))

    #  Relatórios adicionais 
    def imoveis_por_tipo(self) -> dict:
        # Retorna a quantidade de imóveis por tipo (Casa/Apartamento)
        return dict(Counter(i.__class__.__name__ for i in self.imobiliaria.imoveis))

    def maior_imovel(self):
        # Retorna o imóvel com maior metragem
        return max(self.imobiliaria.imoveis, key=lambda i: i.metragem, default=None)

    def menor_imovel(self):
        # Retorna o imóvel com menor metragem
        return min(self.imobiliaria.imoveis, key=lambda i: i.metragem, default=None)

    def cidade_com_mais_imoveis(self) -> str:
        # Retorna a cidade que possui mais imóveis cadastrados
        contagem = self.quantidade_por_cidade()
        return max(contagem, key=contagem.get, default="Nenhuma")

    def maior_taxa(self):
        # Retorna o imóvel com maior taxa administrativa
        return max(self.imobiliaria.imoveis, key=lambda i: i.calcular_taxa_administrativa(), default=None)

    def menor_taxa(self):
        # Retorna o imóvel com menor taxa administrativa
        return min(self.imobiliaria.imoveis, key=lambda i: i.calcular_taxa_administrativa(), default=None)

    def imoveis_negociados_detalhado(self) -> list:
        # Retorna o histórico completo de negociações
        return self.imobiliaria.negociacoes

    def valor_total_imoveis(self) -> float:
        # Retorna o somatório do valor de todos os imóveis
        return sum(i.valor for i in self.imobiliaria.imoveis)

    def imoveis_por_proprietario(self) -> dict:
        # Retorna a quantidade de imóveis por CPF do proprietário
        return dict(Counter(i.proprietario_cpf for i in self.imobiliaria.imoveis))

    # Resumo geral

    def gerar_resumo_texto(self) -> str:
        # Gera texto com resumo geral da imobiliária
        maior = self.maior_imovel()
        menor = self.menor_imovel()
        mt = self.maior_taxa()
        me = self.menor_taxa()
        linhas = [
            "RELATÓRIO GERAL DA IMOBILIÁRIA",
            "=" * 50,
            f"Clientes cadastrados      : {len(self.imobiliaria.clientes)}",
            f"Proprietários cadastrados : {len(self.imobiliaria.proprietarios)}",
            f"Imóveis cadastrados       : {len(self.imobiliaria.imoveis)}",
            f"Imóveis disponíveis       : {self.quantidade_disponiveis()}",
            f"Imóveis negociados        : {self.quantidade_negociados()}",
            f"Média dos valores (casas) : R$ {self.media_valor_casas():.2f}",
            f"Média dos valores (apts)  : R$ {self.media_valor_apartamentos():.2f}",
            f"Valor total dos imóveis   : R$ {self.valor_total_imoveis():.2f}",
            f"Total das taxas administ. : R$ {self.total_taxas_administrativas():.2f}",
            f"Casas com piscina         : {self.quantidade_casas_com_piscina()}",
            f"Percentual c/ piscina     : {self.percentual_casas_com_piscina():.2f}%",
            f"Por modalidade            : {self.quantidade_por_modalidade()}",
            f"Por cidade                : {self.quantidade_por_cidade()}",
            f"Por tipo                  : {self.imoveis_por_tipo()}",
            f"Por ano de cadastro       : {self.quantidade_por_ano()}",
            f"Cidade com mais imóveis   : {self.cidade_com_mais_imoveis()}",
            f"Maior imóvel (metragem)   : {maior}",
            f"Menor imóvel (metragem)   : {menor}",
            f"Maior taxa administrativa : {mt}",
            f"Menor taxa administrativa : {me}",
        ]
        return "\n".join(linhas)

    # Exportações

    def exportar_txt(self, caminho: str = "exports/relatorio_geral.txt") -> Path:
        # Exporta o relatório geral para um arquivo TXT
        caminho = Path(caminho)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(self.gerar_resumo_texto(), encoding="utf-8")
        return caminho

    def exportar_csv_imoveis(self, caminho: str = "exports/imoveis.csv") -> Path:
        # Exporta os imóveis para um arquivo CSV
        caminho = Path(caminho)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        campos = ["codigo", "tipo", "endereco", "cidade", "modalidade",
                  "valor", "metragem", "data_cadastro", "disponivel", "taxa"]
        with caminho.open("w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            for imovel in self.imobiliaria.imoveis:
                escritor.writerow({
                    "codigo": imovel.codigo,
                    "tipo": imovel.__class__.__name__,
                    "endereco": imovel.endereco,
                    "cidade": imovel.cidade,
                    "modalidade": imovel.modalidade,
                    "valor": imovel.valor,
                    "metragem": imovel.metragem,
                    "data_cadastro": imovel.data_cadastro,
                    "disponivel": "Sim" if imovel.disponivel else "Não",
                    "taxa": imovel.calcular_taxa_administrativa()
                })
        return caminho

    def exportar_csv_negociacoes(self, caminho: str = "exports/negociacoes.csv") -> Path:
        # Exporta o histórico de negociações para um arquivo CSV
        caminho = Path(caminho)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        campos = ["codigo_imovel", "cpf_cliente", "nome_cliente", "modalidade", "valor", "data"]
        with caminho.open("w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            for neg in self.imobiliaria.negociacoes:
                escritor.writerow(neg)
        return caminho

    # Gráficos

    def gerar_graficos(self, pasta: str = "relatorios/graficos") -> list:
       
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            raise ImportError("matplotlib não instalado. Execute: pip install matplotlib")

        pasta = Path(pasta)
        pasta.mkdir(parents=True, exist_ok=True)
        gerados = []

        def _salvar(fig, nome):
            caminho = pasta / nome
            fig.savefig(caminho, bbox_inches="tight")
            plt.close(fig)
            gerados.append(caminho)

        # 1. Imóveis por cidade
        por_cidade = self.quantidade_por_cidade()
        if por_cidade:
            fig, ax = plt.subplots()
            ax.bar(por_cidade.keys(), por_cidade.values(), color="#4c72b0")
            ax.set_title("Imóveis por Cidade")
            ax.set_xlabel("Cidade")
            ax.set_ylabel("Quantidade")
            _salvar(fig, "imoveis_por_cidade.png")

        # 2. Disponíveis x Negociados
        disp = self.quantidade_disponiveis()
        neg = self.quantidade_negociados()
        if disp + neg > 0:
            fig, ax = plt.subplots()
            ax.pie([disp, neg], labels=["Disponíveis", "Negociados"],
                   autopct="%1.1f%%", colors=["#2ecc71", "#e74c3c"])
            ax.set_title("Disponíveis x Negociados")
            _salvar(fig, "disponiveis_vs_negociados.png")

        # 3. Casas com piscina
        casas_total = len([i for i in self.imobiliaria.imoveis if isinstance(i, Casa)])
        com_piscina = self.quantidade_casas_com_piscina()
        sem_piscina = casas_total - com_piscina
        if casas_total > 0:
            fig, ax = plt.subplots()
            ax.pie([com_piscina, sem_piscina], labels=["Com piscina", "Sem piscina"],
                   autopct="%1.1f%%", colors=["#3498db", "#bdc3c7"])
            ax.set_title("Casas com Piscina")
            _salvar(fig, "casas_com_piscina.png")

        # 4. Venda x Aluguel
        por_modalidade = self.quantidade_por_modalidade()
        if por_modalidade:
            fig, ax = plt.subplots()
            ax.bar(por_modalidade.keys(), por_modalidade.values(), color=["#e67e22", "#9b59b6"])
            ax.set_title("Imóveis por Modalidade")
            ax.set_xlabel("Modalidade")
            ax.set_ylabel("Quantidade")
            _salvar(fig, "venda_vs_aluguel.png")

        # 5. Valor médio por tipo
        media_casa = self.media_valor_casas()
        media_ap = self.media_valor_apartamentos()
        if media_casa > 0 or media_ap > 0:
            fig, ax = plt.subplots()
            ax.bar(["Casa", "Apartamento"], [media_casa, media_ap], color=["#1abc9c", "#e74c3c"])
            ax.set_title("Valor Médio por Tipo de Imóvel")
            ax.set_xlabel("Tipo")
            ax.set_ylabel("Valor Médio (R$)")
            _salvar(fig, "valor_medio_por_tipo.png")

        return gerados
