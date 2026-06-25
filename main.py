from models import Cliente, Casa
from services import Imobiliaria, Validacoes

def testar_sistema():

    print("🚀 Iniciando teste da Lopes Imóveis...\n")

    sistema = Imobiliaria()

    # ---------------- TESTE CLIENTE ----------------
    cliente = Cliente(
        1,
        "Ana Teste",
        "12345678901",
        "88999999999",
        "Casa"
    )

    # validações básicas
    print("CPF válido?", Validacoes.validar_cpf(cliente.cpf))

    sistema.adicionar_cliente(cliente)
    print("✔ Cliente adicionado com sucesso!")

    # ---------------- TESTE IMÓVEL ----------------
    casa = Casa(
        1,
        "Centro da Cidade",
        250000,
        3,
        120
    )

    sistema.adicionar_imovel(casa)
    print("✔ Imóvel adicionado com sucesso!")

    # ---------------- RESUMO ----------------
    print("\n📊 RESUMO DO SISTEMA:")
    print(sistema.resumo())

    print("\n🏠 IMÓVEIS CADASTRADOS:")
    print(sistema.listar_imoveis())

    print("\n🎯 TESTE FINALIZADO COM SUCESSO!")

if __name__ == "__main__":
    testar_sistema()