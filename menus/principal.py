from services import Persistencia, carregar_dados_exemplo
from utils import cabecalho, pausa, ler_opcao, limpar_tela
from .clientes import menu_clientes
from .proprietarios import menu_proprietarios
from .imoveis import menu_imoveis
from .negociacoes import menu_negociacoes
from .relatorios import menu_relatorios


class MenuPrincipal:
    def __init__(self):
        self.imobiliaria = Persistencia.carregar_dados()

    def executar(self):
        while True:
            limpar_tela()
            cabecalho("SISTEMA DE GERENCIAMENTO DE IMÓVEIS")
            print("1 - Clientes")
            print("2 - Proprietários")
            print("3 - Imóveis")
            print("4 - Negociações")
            print("5 - Relatórios")
            print("6 - Carregar dados de exemplo")
            print("7 - Salvar dados")
            print("0 - Sair")
            opcao = ler_opcao()

            if opcao == "1":
                menu_clientes(self.imobiliaria)
            elif opcao == "2":
                menu_proprietarios(self.imobiliaria)
            elif opcao == "3":
                menu_imoveis(self.imobiliaria)
            elif opcao == "4":
                menu_negociacoes(self.imobiliaria)
            elif opcao == "5":
                menu_relatorios(self.imobiliaria)
            elif opcao == "6":
                confirmar = input("Isso vai apagar os dados atuais. Digite SIM para confirmar: ")
                if confirmar == "SIM":
                    carregar_dados_exemplo(self.imobiliaria)
                    Persistencia.salvar_dados(self.imobiliaria)
                    print("Dados de exemplo carregados e salvos.")
                else:
                    print("Operação cancelada.")
                pausa()
            elif opcao == "7":
                Persistencia.salvar_dados(self.imobiliaria)
                print("Dados salvos com sucesso.")
                pausa()
            elif opcao == "0":
                Persistencia.salvar_dados(self.imobiliaria)
                print("Dados salvos. Sistema encerrado.")
                break
            else:
                print("Opção inválida.")
                pausa()
