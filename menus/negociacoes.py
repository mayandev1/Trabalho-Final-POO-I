from utils import cabecalho, pausa, ler_opcao, ler_texto, limpar_tela


def menu_negociacoes(imobiliaria):
    while True:
        limpar_tela()
        cabecalho("MENU NEGOCIAÇÕES")
        print("1 - Realizar negociação")
        print("2 - Listar histórico")
        print("0 - Voltar")
        opcao = ler_opcao()

        try:
            if opcao == "1":
                negociacao = imobiliaria.realizar_negociacao(ler_texto("Código do imóvel"), ler_texto("CPF do cliente"))
                print("Negociação realizada com sucesso!")
                print(negociacao)
            elif opcao == "2":
                if not imobiliaria.negociacoes:
                    print("Nenhuma negociação registrada.")
                for n in imobiliaria.negociacoes:
                    print(f"Imóvel {n['codigo_imovel']} | Cliente: {n['nome_cliente']} | {n['modalidade']} | R$ {n['valor']:.2f} | {n['data']}")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")
        pausa()
