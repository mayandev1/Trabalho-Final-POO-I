import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def cabecalho(titulo):
    print("=" * 70)
    print(titulo.center(70))
    print("=" * 70)


def pausa():
    input("\nPressione ENTER para continuar...")


def moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def imprimir_lista(titulo, itens):
    cabecalho(titulo)
    if not itens:
        print("Nenhum registro encontrado.")
        return
    for item in itens:
        print(item)
