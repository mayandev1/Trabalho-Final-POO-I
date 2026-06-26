def ler_opcao(mensagem="Escolha uma opção: "):
    return input(mensagem).strip()


def ler_texto(rotulo):
    return input(f"{rotulo}: ").strip()


def ler_sim_nao(rotulo):
    while True:
        valor = input(f"{rotulo} (S/N): ").strip().lower()
        if valor in ("s", "sim"):
            return True
        if valor in ("n", "nao", "não"):
            return False
        print("Digite apenas S ou N.")
