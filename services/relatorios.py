from collections import Counter
from pathlib import Path
import csv
from models import Casa, Apartamento


class Relatorios:
    def __init__(self, imobiliaria):
        self.imobiliaria = imobiliaria

    def media_valor_casas(self):
        casas = [i for i in self.imobiliaria.imoveis if isinstance(i, Casa)]
        return sum(i.valor for i in casas) / len(casas) if casas else 0

    def media_valor_apartamentos(self):
        aps = [i for i in self.imobiliaria.imoveis if isinstance(i, Apartamento)]
        return sum(i.valor for i in aps) / len(aps) if aps else 0

    def quantidade_disponiveis(self):
        return len([i for i in self.imobiliaria.imoveis if i.disponivel])

    def quantidade_negociados(self):
        return len([i for i in self.imobiliaria.imoveis if not i.disponivel])

    def quantidade_por_cidade(self):
        return dict(Counter(i.cidade for i in self.imobiliaria.imoveis))

    def total_taxas_administrativas(self):
        return sum(i.calcular_taxa_administrativa() for i in self.imobiliaria.imoveis)

    def percentual_casas_com_piscina(self):
        casas = [i for i in self.imobiliaria.imoveis if isinstance(i, Casa)]
        if not casas:
            return 0
        com_piscina = [c for c in casas if c.piscina]
        return (len(com_piscina) / len(casas)) * 100

    def quantidade_casas_com_piscina(self):
        return len([i for i in self.imobiliaria.imoveis if isinstance(i, Casa) and i.piscina])

    def quantidade_por_modalidade(self):
        return dict(Counter(i.modalidade for i in self.imobiliaria.imoveis))

    def quantidade_por_ano(self):
        anos = [i.data_cadastro[-4:] for i in self.imobiliaria.imoveis]
        return dict(Counter(anos))

    def gerar_resumo_texto(self):
        linhas = [
            "RELATÓRIO GERAL DA IMOBILIÁRIA",
            "=" * 40,
            f"Clientes cadastrados: {len(self.imobiliaria.clientes)}",
            f"Proprietários cadastrados: {len(self.imobiliaria.proprietarios)}",
            f"Imóveis cadastrados: {len(self.imobiliaria.imoveis)}",
            f"Imóveis disponíveis: {self.quantidade_disponiveis()}",
            f"Imóveis negociados: {self.quantidade_negociados()}",
            f"Média dos valores das casas: R$ {self.media_valor_casas():.2f}",
            f"Média dos valores dos apartamentos: R$ {self.media_valor_apartamentos():.2f}",
            f"Total das taxas administrativas: R$ {self.total_taxas_administrativas():.2f}",
            f"Casas com piscina: {self.quantidade_casas_com_piscina()}",
            f"Percentual de casas com piscina: {self.percentual_casas_com_piscina():.2f}%",
            f"Imóveis por modalidade: {self.quantidade_por_modalidade()}",
            f"Imóveis por cidade: {self.quantidade_por_cidade()}",
            f"Imóveis por ano: {self.quantidade_por_ano()}",
        ]
        return "\n".join(linhas)

    def exportar_txt(self, caminho="exports/relatorio_geral.txt"):
        caminho = Path(caminho)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(self.gerar_resumo_texto(), encoding="utf-8")
        return caminho

    def exportar_csv_imoveis(self, caminho="exports/imoveis.csv"):
        caminho = Path(caminho)
        caminho.parent.mkdir(parents=True, exist_ok=True)
        with caminho.open("w", newline="", encoding="utf-8") as arquivo:
            campos = ["codigo", "tipo", "endereco", "cidade", "modalidade", "valor", "metragem", "data_cadastro", "disponivel", "taxa"]
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
