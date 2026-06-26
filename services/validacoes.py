from datetime import datetime


class Validacoes:
    @staticmethod
    def campo_obrigatorio(valor, nome_campo):
        if valor is None or str(valor).strip() == "":
            raise ValueError(f"O campo {nome_campo} é obrigatório.")
        return str(valor).strip()

    @staticmethod
    def validar_cpf(cpf):
        cpf = Validacoes.campo_obrigatorio(cpf, "CPF")
        numeros = ''.join(ch for ch in cpf if ch.isdigit())
        if len(numeros) != 11:
            raise ValueError("CPF deve conter 11 números.")
        return numeros

    @staticmethod
    def validar_email(email):
        email = Validacoes.campo_obrigatorio(email, "e-mail")
        if "@" not in email or "." not in email:
            raise ValueError("E-mail inválido.")
        return email

    @staticmethod
    def validar_telefone(telefone):
        telefone = Validacoes.campo_obrigatorio(telefone, "telefone")
        numeros = ''.join(ch for ch in telefone if ch.isdigit())
        if len(numeros) < 8:
            raise ValueError("Telefone inválido.")
        return telefone

    @staticmethod
    def validar_float(valor, nome_campo):
        try:
            numero = float(str(valor).replace(",", "."))
        except ValueError as exc:
            raise ValueError(f"{nome_campo} deve ser numérico.") from exc
        if numero < 0:
            raise ValueError(f"{nome_campo} não pode ser negativo.")
        return numero

    @staticmethod
    def validar_int(valor, nome_campo):
        try:
            numero = int(valor)
        except ValueError as exc:
            raise ValueError(f"{nome_campo} deve ser inteiro.") from exc
        if numero < 0:
            raise ValueError(f"{nome_campo} não pode ser negativo.")
        return numero

    @staticmethod
    def validar_modalidade(modalidade):
        modalidade = Validacoes.campo_obrigatorio(modalidade, "modalidade").lower()
        if modalidade not in ("venda", "aluguel"):
            raise ValueError("Modalidade deve ser 'venda' ou 'aluguel'.")
        return modalidade

    @staticmethod
    def validar_data(data):
        data = Validacoes.campo_obrigatorio(data, "data")
        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError as exc:
            raise ValueError("Data inválida. Use o formato DD/MM/AAAA.") from exc
        return data

    @staticmethod
    def validar_sim_nao(valor):
        valor = str(valor).strip().lower()
        if valor in ("s", "sim", "1", "true"):
            return True
        if valor in ("n", "nao", "não", "0", "false"):
            return False
        raise ValueError("Informe apenas S ou N.")
