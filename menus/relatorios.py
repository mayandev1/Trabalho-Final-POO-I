from utils import cabecalho, pausa, ler_opcao, limpar_tela
from services import Relatorios

def menu_relatorios(imobiliaria):
    # menu de relatórios
    while True:
        limpar_tela()
        rel = Relatorios(imobiliaria)
        cabecalho("MENU RELATÓRIOS")
        print("=== Exibição ===")
        print(" 1 - Relatório geral completo")
        print(" 2 - Imóveis por cidade")
        print(" 3 - Imóveis por modalidade (venda/aluguel)")
        print(" 4 - Imóveis por tipo (Casa/Apartamento)")
        print(" 5 - Imóveis por ano de cadastro")
        print(" 6 - Disponíveis x Negociados")
        print(" 7 - Casas com piscina")
        print(" 8 - Estatísticas (maior/menor imóvel e taxa)")
        print(" 9 - Histórico de negociações")
        print("10 - Imóveis por proprietário")
        print("")
        print("=== Exportação ===")
        print("11 - Exportar relatório geral (TXT)")
        print("12 - Exportar imóveis (CSV)")
        print("13 - Exportar negociações (CSV)")
        print("")
        print("=== Gráficos ===")
        print("14 - Gerar gráficos (PNG)")
        print(" 0 - Voltar")
        opcao = ler_opcao()

        if opcao == "0":
            break

        try:
            if opcao == "1":
                print(rel.gerar_resumo_texto())

            elif opcao == "2":
                cabecalho("IMÓVEIS POR CIDADE")
                for cidade, qtd in rel.quantidade_por_cidade().items():
                    print(f"  {cidade}: {qtd} imóvel(is)")

            elif opcao == "3":
                cabecalho("IMÓVEIS POR MODALIDADE")
                for mod, qtd in rel.quantidade_por_modalidade().items():
                    print(f"  {mod.title()}: {qtd}")

            elif opcao == "4":
                cabecalho("IMÓVEIS POR TIPO")
                for tipo, qtd in rel.imoveis_por_tipo().items():
                    print(f"  {tipo}: {qtd}")

            elif opcao == "5":
                cabecalho("IMÓVEIS POR ANO DE CADASTRO")
                for ano, qtd in sorted(rel.quantidade_por_ano().items()):
                    print(f"  {ano}: {qtd} imóvel(is)")

            elif opcao == "6":
                cabecalho("DISPONÍVEIS X NEGOCIADOS")
                print(f"  Disponíveis : {rel.quantidade_disponiveis()}")
                print(f"  Negociados  : {rel.quantidade_negociados()}")

            elif opcao == "7":
                cabecalho("CASAS COM PISCINA")
                print(f"  Quantidade  : {rel.quantidade_casas_com_piscina()}")
                print(f"  Percentual  : {rel.percentual_casas_com_piscina():.2f}%")
                import models
                print(f"  (attr classe): {models.Casa.quantidade_com_piscina()}")

            elif opcao == "8":
                cabecalho("ESTATÍSTICAS")
                maior = rel.maior_imovel()
                menor = rel.menor_imovel()
                mt = rel.maior_taxa()
                me = rel.menor_taxa()
                print(f"  Cidade com mais imóveis: {rel.cidade_com_mais_imoveis()}")
                print(f"  Maior imóvel (metragem): {maior}")
                print(f"  Menor imóvel (metragem): {menor}")
                print(f"  Maior taxa adm.        : {mt}")
                print(f"  Menor taxa adm.        : {me}")
                print(f"  Valor total imóveis    : R$ {rel.valor_total_imoveis():.2f}")

            elif opcao == "9":
                cabecalho("HISTÓRICO DE NEGOCIAÇÕES")
                negs = rel.imoveis_negociados_detalhado()
                if not negs:
                    print("  Nenhuma negociação registrada.")
                for n in negs:
                    print(f"  Imóvel {n['codigo_imovel']} | {n['nome_cliente']} | "
                          f"{n['modalidade'].title()} | R$ {n['valor']:.2f} | {n['data']}")

            elif opcao == "10":
                cabecalho("IMÓVEIS POR PROPRIETÁRIO")
                for cpf, qtd in rel.imoveis_por_proprietario().items():
                    prop = imobiliaria.buscar_proprietario_por_cpf(cpf)
                    nome = prop.nome if prop else cpf
                    print(f"  {nome}: {qtd} imóvel(is)")

            elif opcao == "11":
                caminho = rel.exportar_txt()
                print(f"Relatório exportado para: {caminho}")

            elif opcao == "12":
                caminho = rel.exportar_csv_imoveis()
                print(f"CSV de imóveis exportado para: {caminho}")

            elif opcao == "13":
                caminho = rel.exportar_csv_negociacoes()
                print(f"CSV de negociações exportado para: {caminho}")

            elif opcao == "14":
                graficos = rel.gerar_graficos()
                if graficos:
                    print(f"{len(graficos)} gráfico(s) gerado(s) em relatorios/graficos/:")
                    for g in graficos:
                        print(f"  {g}")
                else:
                    print("Nenhum dado disponível para gerar gráficos.")

            else:
                print("Opção inválida.")

        except (ValueError, ImportError) as erro:
            print(f"Erro: {erro}")
        else:
            pass  # operação concluída sem erros
        finally:
            pausa()
