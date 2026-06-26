class Pessoa:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados.get("nome", ""),
            dados.get("cpf", ""),
            dados.get("telefone", ""),
            dados.get("email", "")
        )

    def __str__(self):
        return f"{self.nome} | CPF: {self.cpf} | Tel: {self.telefone} | E-mail: {self.email}"
