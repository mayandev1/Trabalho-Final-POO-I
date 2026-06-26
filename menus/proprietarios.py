from utils import cabecalho, pausa, ler_opcao, ler_texto, imprimir_lista, limpar_tela

def menu_proprietarios(imobiliaria):
    while True:
        limpar_tela()
        cabecalho("MENU PROPRIETÁRIOS")
        print("1 - Cadastrar proprietário")
        print("2 - Listar proprietários")
        print("3 - Buscar proprietário por CPF")
        print("0 - Voltar")
        opcao = ler_opcao()

        try:
            if opcao == "1":
                proprietario = imobiliaria.cadastrar_proprietario(
                    ler_texto("Nome"), ler_texto("CPF"), ler_texto("Telefone"), ler_texto("E-mail")
                )
                print(f"Proprietário cadastrado: {proprietario}")
            elif opcao == "2":
                imprimir_lista("PROPRIETÁRIOS CADASTRADOS", imobiliaria.proprietarios)
            elif opcao == "3":
                proprietario = imobiliaria.buscar_proprietario_por_cpf(ler_texto("CPF"))
                print(proprietario if proprietario else "Proprietário não encontrado.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")
        pausa()
