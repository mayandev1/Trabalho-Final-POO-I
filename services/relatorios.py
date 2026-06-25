class Relatorios:

    @staticmethod
    def resumo_geral(dados):
        return {
            "total_clientes": len(dados["Clientes"]),
            "total_proprietarios": len(dados["Proprietarios"]),
            "total_imoveis": len(dados["Imoveis"]),
            "total_negociacoes": len(dados.get("Negociacoes", []))
        }

    @staticmethod
    def imoveis_disponiveis(dados):
        return [
            i for i in dados["Imoveis"]
            if i.get("status") == "disponivel"
        ]

    @staticmethod
    def imoveis_indisponiveis(dados):
        return [
            i for i in dados["Imoveis"]
            if i.get("status") != "disponivel"
        ]

    @staticmethod
    def valor_total_imoveis(dados):
        return sum(i.get("valor", 0) for i in dados["Imoveis"])

    @staticmethod
    def imoveis_por_tipo(dados, tipo):
        return [
            i for i in dados["Imoveis"]
            if i.get("tipo") == tipo
        ]