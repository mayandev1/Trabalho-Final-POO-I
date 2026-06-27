# 🏠 Sistema de Gerenciamento Imobiliário

> Trabalho Final da disciplina de **Programação Orientada a Objetos (POO)**.

Sistema desenvolvido em **Python** para gerenciamento de uma imobiliária, permitindo o cadastro de clientes, proprietários e imóveis, realização de negociações, geração de relatórios e persistência dos dados em arquivos JSON.

## 📚 Sobre o Projeto

O projeto foi desenvolvido com o objetivo de aplicar os principais conceitos de Programação Orientada a Objetos estudados na disciplina, por meio da construção de um sistema modular para gerenciamento de imóveis destinados à venda e aluguel.

Entre os conceitos aplicados estão:

* Classes e Objetos
* Encapsulamento
* Herança
* Polimorfismo
* Associação entre classes
* Sobrescrita de métodos
* Atributos de classe
* Métodos estáticos e de classe
* Tratamento de exceções
* Persistência de dados em JSON


# ✨ Funcionalidades

### 👤 Clientes

* Cadastro
* Consulta
* Remoção
* Busca por CPF

### 👨 Proprietários

* Cadastro
* Consulta
* Remoção
* Busca por CPF

### 🏠 Imóveis

* Cadastro de casas e apartamentos
* Código gerado automaticamente
* Consulta e listagem
* Remoção
* Controle de disponibilidade
* Validação de imóveis duplicados

### 🤝 Negociações

* Venda e aluguel de imóveis
* Associação entre cliente e imóvel
* Atualização automática da disponibilidade
* Histórico de negociações

### 📊 Relatórios

O sistema possui diversos relatórios gerenciais, incluindo:

* Média de valores dos imóveis
* Quantidade de imóveis disponíveis e negociados
* Imóveis por cidade
* Imóveis por ano de cadastro
* Quantidade de casas com piscina
* Total das taxas administrativas
* Valor total do patrimônio cadastrado
* Histórico de negociações
* Entre outros


# 🛠️ Tecnologias

* Python 3
* JSON
* Git
* GitHub


# 📂 Estrutura do Projeto

```text
Trabalho-Final-POO-I
│
├── data/
├── menus/
├── models/
├── services/
├── utils/
├── main.py
└── README.md
```

### Organização

* **models/** → entidades do sistema.
* **services/** → regras de negócio.
* **menus/** → interface em terminal.
* **utils/** → funções auxiliares.
* **data/** → persistência em JSON.


# 💾 Persistência

Os dados são armazenados automaticamente em arquivos JSON.

| Arquivo              | Descrição                         |
| -------------------- | --------------------------------- |
| `banco.json`         | Dados cadastrados pelo usuário    |
| `dados_exemplo.json` | Base para demonstração do sistema |



# 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/mayandev1/Trabalho-Final-POO-I.git
```

Acesse a pasta do projeto:

```bash
cd Trabalho-Final-POO-I
```

Execute o sistema:

```bash
python main.py
```



# 🎯 Conceitos de POO Aplicados

* ✔ Classes e Objetos
* ✔ Encapsulamento
* ✔ Herança
* ✔ Polimorfismo
* ✔ Associação entre Classes
* ✔ Sobrescrita de Métodos
* ✔ Métodos Estáticos e de Classe
* ✔ Atributos de Classe
* ✔ Tratamento de Exceções



# 👥 Equipe

| Integrante         | Responsabilidade                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| **Allana Martins** | Modelagem das classes, regras de negócio, persistência, validações, negociações e tratamento de exceções. |
| **Mayan**          | Interface em terminal, menus, integração entre módulos, experiência do usuário e relatórios.              |



# 🎓 Informações Acadêmicas

**Universidade Federal do Piauí (UFPI)**

* **Curso:** Bacharelado em Sistemas de Informação
* **Disciplina:** Programação Orientada a Objetos
* **Ano:** 2026



# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos como trabalho da disciplina de Programação Orientada a Objetos.
