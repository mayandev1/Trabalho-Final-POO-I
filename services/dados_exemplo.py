# services/dados_exemplo.py

import json
from pathlib import Path

from models import Cliente, Proprietario, Casa, Apartamento


def carregar_dados_exemplo(imobiliaria):
    """
    Carrega os dados de exemplo a partir do arquivo
    data/dados_exemplo.json.
    """

    caminho = Path(__file__).resolve().parent.parent / "data" / "dados_exemplo.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    imobiliaria.clientes.clear()
    imobiliaria.proprietarios.clear()
    imobiliaria.imoveis.clear()
    imobiliaria.negociacoes.clear()

    # Clientes ----------------
    for cliente in dados["clientes"]:
        imobiliaria.clientes.append(
            Cliente(
                cliente["nome"],
                cliente["cpf"],
                cliente["telefone"],
                cliente["email"]
            )
        )

    # Proprietários
    for proprietario in dados["proprietarios"]:
        imobiliaria.proprietarios.append(
            Proprietario(
                proprietario["nome"],
                proprietario["cpf"],
                proprietario["telefone"],
                proprietario["email"]
            )
        )

    # Imóveis 
    for imovel in dados["imoveis"]:

        proprietario = next(
            p for p in imobiliaria.proprietarios
            if p.cpf == imovel["proprietario_cpf"]
        )

        cliente = None

        if imovel["cliente_cpf"] is not None:
            cliente = next(
                c for c in imobiliaria.clientes
                if c.cpf == imovel["cliente_cpf"]
            )

        if imovel["tipo"] == "casa":

            novo = Casa(
                proprietario,
                imovel["endereco"],
                imovel["cidade"],
                imovel["modalidade"],
                imovel["valor"],
                imovel["metragem"],
                imovel["data_cadastro"],
                imovel["piscina"]
            )

        else:

            novo = Apartamento(
                proprietario,
                imovel["endereco"],
                imovel["cidade"],
                imovel["modalidade"],
                imovel["valor"],
                imovel["metragem"],
                imovel["data_cadastro"],
                imovel["andar"],
                imovel["numero_apartamento"]
            )

        novo.codigo = imovel["codigo"]
        novo.disponivel = imovel["disponivel"]
        novo.cliente = cliente

        imobiliaria.imoveis.append(novo)

    # Negociações 
    imobiliaria.negociacoes = dados["negociacoes"]