from utils import cabecalho, pausa, ler_opcao, limpar_tela
from services import Relatorios


def menu_relatorios(imobiliaria):
    while True:
        limpar_tela()
        rel = Relatorios(imobiliaria)
        cabecalho("MENU RELATÓRIOS")
        print("1 - Exibir relatório geral")
        print("2 - Quantidade por cidade")
        print("3 - Quantidade por modalidade")
        print("4 - Exportar relatório TXT")
        print("5 - Exportar imóveis CSV")
        print("0 - Voltar")
        opcao = ler_opcao()

        if opcao == "1":
            print(rel.gerar_resumo_texto())
        elif opcao == "2":
            print(rel.quantidade_por_cidade())
        elif opcao == "3":
            print(rel.quantidade_por_modalidade())
        elif opcao == "4":
            caminho = rel.exportar_txt()
            print(f"Relatório exportado para: {caminho}")
        elif opcao == "5":
            caminho = rel.exportar_csv_imoveis()
            print(f"CSV exportado para: {caminho}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
        pausa()
