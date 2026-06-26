def carregar_dados_exemplo(imobiliaria):
    imobiliaria.clientes.clear()
    imobiliaria.proprietarios.clear()
    imobiliaria.imoveis.clear()
    imobiliaria.negociacoes.clear()

    p1 = imobiliaria.cadastrar_proprietario("Carlos Silva", "11122233344", "89999990000", "carlos@email.com")
    p2 = imobiliaria.cadastrar_proprietario("Ana Souza", "22233344455", "89988887777", "ana@email.com")

    c1 = imobiliaria.cadastrar_cliente("João Lima", "33344455566", "89977776666", "joao@email.com")
    imobiliaria.cadastrar_cliente("Mariana Costa", "44455566677", "89966665555", "mariana@email.com")

    casa = imobiliaria.cadastrar_casa(p1.cpf, "Rua A, 100", "Picos", "venda", 250000, 280, True, "10/01/2026")
    imobiliaria.cadastrar_casa(p2.cpf, "Rua B, 200", "Picos", "aluguel", 1200, 180, False, "15/02/2026")
    imobiliaria.cadastrar_apartamento(p1.cpf, "Av. Central, 300", "Teresina", "venda", 320000, 70, 5, "502", "20/03/2026")
    imobiliaria.cadastrar_apartamento(p2.cpf, "Rua das Flores, 50", "Picos", "aluguel", 900, 45, 2, "203", "05/04/2026")

    imobiliaria.realizar_negociacao(casa.codigo, c1.cpf)
