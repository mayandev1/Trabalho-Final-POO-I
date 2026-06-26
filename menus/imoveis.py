from utils import cabecalho, pausa, ler_opcao, ler_texto, ler_sim_nao, imprimir_lista, limpar_tela
from services import Validacoes


def menu_imoveis(imobiliaria):
    while True:
        limpar_tela()
        cabecalho("MENU IMÓVEIS")
        print("1 - Cadastrar casa")
        print("2 - Cadastrar apartamento")
        print("3 - Listar todos")
        print("4 - Listar disponíveis")
        print("5 - Buscar por código")
        print("6 - Busca avançada")
        print("0 - Voltar")
        opcao = ler_opcao()

        try:
            if opcao == "1":
                casa = imobiliaria.cadastrar_casa(
                    ler_texto("CPF do proprietário"), ler_texto("Endereço"), ler_texto("Cidade"),
                    ler_texto("Modalidade (venda/aluguel)"), ler_texto("Valor"), ler_texto("Metragem"),
                    ler_sim_nao("Possui piscina?")
                )
                print(f"Casa cadastrada com código {casa.codigo}.")
            elif opcao == "2":
                ap = imobiliaria.cadastrar_apartamento(
                    ler_texto("CPF do proprietário"), ler_texto("Endereço"), ler_texto("Cidade"),
                    ler_texto("Modalidade (venda/aluguel)"), ler_texto("Valor"), ler_texto("Metragem"),
                    ler_texto("Andar"), ler_texto("Número do apartamento")
                )
                print(f"Apartamento cadastrado com código {ap.codigo}.")
            elif opcao == "3":
                imprimir_lista("TODOS OS IMÓVEIS", imobiliaria.imoveis)
            elif opcao == "4":
                imprimir_lista("IMÓVEIS DISPONÍVEIS", imobiliaria.listar_imoveis_disponiveis())
            elif opcao == "5":
                imovel = imobiliaria.buscar_imovel_por_codigo(ler_texto("Código"))
                print(imovel if imovel else "Imóvel não encontrado.")
            elif opcao == "6":
                busca_avancada(imobiliaria)
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
        except ValueError as erro:
            print(f"Erro: {erro}")
        pausa()


def busca_avancada(imobiliaria):
    print("Deixe em branco para ignorar o filtro.")
    cidade = ler_texto("Cidade") or None
    tipo = ler_texto("Tipo (Casa/Apartamento)") or None
    modalidade = ler_texto("Modalidade (venda/aluguel)") or None
    status = ler_texto("Disponível? (S/N)")
    ano = ler_texto("Ano de cadastro") or None
    valor_min = ler_texto("Valor mínimo") or None
    valor_max = ler_texto("Valor máximo") or None

    disponivel = None
    if status:
        disponivel = Validacoes.validar_sim_nao(status)

    resultado = imobiliaria.buscar_imoveis(cidade, tipo, modalidade, disponivel, ano, valor_min, valor_max)
    imprimir_lista("RESULTADO DA BUSCA", resultado)
