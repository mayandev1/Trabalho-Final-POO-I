from utils import cabecalho, pausa, ler_opcao, ler_texto, imprimir_lista, limpar_tela

def menu_clientes(imobiliaria):
    while True:
        limpar_tela()
        cabecalho("MENU CLIENTES")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente por CPF")
        print("4 - Remover cliente")
        print("0 - Voltar")
        opcao = ler_opcao()

        try:
            if opcao == "1":
                cliente = imobiliaria.cadastrar_cliente(
                    ler_texto("Nome"), ler_texto("CPF"), ler_texto("Telefone"), ler_texto("E-mail")
                )
                print(f"Cliente cadastrado: {cliente}")
            elif opcao == "2":
                imprimir_lista("CLIENTES CADASTRADOS", imobiliaria.clientes)
            elif opcao == "3":
                cliente = imobiliaria.buscar_cliente_por_cpf(ler_texto("CPF"))
                print(cliente if cliente else "Cliente não encontrado.")
            elif opcao == "4":
                cpf = ler_texto("CPF do cliente")
                if cliente.deletar_cliente(imobiliaria.clientes, cpf):
                    print("Cliente removido com sucesso!")
                else:
                    print("Cliente não encontrado.")
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")
        pausa()
