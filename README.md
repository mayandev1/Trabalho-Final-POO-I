<div align="center">

# 🏠 Sistema de Gerenciamento Imobiliário

### Trabalho Final da Disciplina de Programação Orientada a Objetos

Sistema desenvolvido em **Python** utilizando os princípios da **Programação Orientada a Objetos (POO)** para o gerenciamento de uma imobiliária, permitindo o cadastro e gerenciamento de clientes, proprietários, imóveis e negociações.

<br>

<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge">
<img src="https://img.shields.io/badge/POO-Programação%20Orientada%20a%20Objetos-green?style=for-the-badge">
<img src="https://img.shields.io/badge/UFPI-Sistemas%20de%20Informação-blueviolet?style=for-the-badge">

</div>

---

# 📖 Sobre o Projeto

O **Sistema de Gerenciamento Imobiliário** foi desenvolvido como trabalho final da disciplina de **Programação Orientada a Objetos**, do curso de **Bacharelado em Sistemas de Informação da Universidade Federal do Piauí (UFPI)**.

A aplicação simula o funcionamento de uma imobiliária, permitindo realizar o gerenciamento completo de clientes, proprietários, imóveis e negociações através de uma interface em terminal.

O sistema foi desenvolvido utilizando uma arquitetura modular, facilitando a organização do código, reutilização de componentes e manutenção da aplicação.

---

# 🎯 Objetivos

- Aplicar os conceitos de Programação Orientada a Objetos.
- Desenvolver um sistema organizado em módulos.
- Simular o funcionamento de uma imobiliária.
- Utilizar persistência de dados em arquivos JSON.
- Aplicar boas práticas de desenvolvimento em Python.

---

# ✨ Funcionalidades

## 👤 Clientes

- Cadastro de clientes
- Listagem de clientes
- Atualização de dados
- Remoção de clientes
- Busca por CPF

---

## 👨 Proprietários

- Cadastro de proprietários
- Listagem de proprietários
- Atualização de dados
- Remoção de proprietários
- Busca por CPF

---

## 🏠 Imóveis

- Cadastro de imóveis
- Cadastro de casas
- Cadastro de apartamentos
- Listagem de imóveis
- Atualização de imóveis
- Remoção de imóveis

---

## 🤝 Negociações

- Registro de negociações
- Associação entre cliente e imóvel
- Histórico de negociações

---

## 📊 Relatórios

- Relatório de clientes
- Relatório de proprietários
- Relatório de imóveis
- Estatísticas do sistema

---

## ⚙️ Recursos Gerais

- Validação de CPF
- Persistência automática em JSON
- Carregamento de dados de exemplo
- Menus interativos
- Tratamento de exceções
- Código modular

---

# 🏛️ Conceitos de POO Aplicados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

- Classes
- Objetos
- Encapsulamento
- Herança
- Polimorfismo
- Abstração
- Organização em módulos
- Reutilização de código

---

# 📂 Estrutura do Projeto

```text
Trabalho-Final-POO-I
│
├── data
│   ├── banco.json
│   └── dados_exemplo.json
│
├── menus
│   ├── __init__.py
│   ├── clientes.py
│   ├── imoveis.py
│   ├── negociacoes.py
│   ├── principal.py
│   ├── proprietarios.py
│   └── relatorios.py
│
├── models
│   ├── __init__.py
│   ├── apartamento.py
│   ├── casa.py
│   ├── cliente.py
│   ├── imovel.py
│   ├── pessoa.py
│   └── proprietario.py
│
├── services
│   ├── __init__.py
│   ├── dados_exemplo.py
│   ├── imobiliaria.py
│   ├── persistencia.py
│   ├── relatorio.py
│   └── validacoes.py
│
├── utils
│   ├── __init__.py
│   ├── entrada.py
│   └── formatacao.py
│
├── main.py
│
└── README.md
```

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| Python 3 | Linguagem principal |
| JSON | Persistência dos dados |
| Git | Controle de versão |
| GitHub | Hospedagem do projeto |
| POO | Arquitetura do sistema |

---

# 💾 Persistência de Dados

O sistema utiliza arquivos JSON para armazenar as informações cadastradas.

### Arquivos

| Arquivo | Finalidade |
|----------|------------|
| `banco.json` | Armazena os dados cadastrados durante a utilização do sistema. |
| `dados_exemplo.json` | Contém dados utilizados para demonstração e testes da aplicação. |

---

# 🚀 Como Executar

### Clone o repositório

```bash
git clone https://github.com/mayandev1/Trabalho-Final-POO-I.git
```

### Entre na pasta

```bash
cd Trabalho-Final-POO-I
```

### Execute o sistema

```bash
python main.py
```

---

# 📌 Organização do Projeto

O projeto foi dividido em módulos para facilitar sua manutenção.

## Models

Responsáveis por representar as entidades do sistema, como clientes, proprietários e imóveis.

---

## Services

Contêm toda a lógica de negócio da aplicação, incluindo persistência dos dados, validações e geração de relatórios.

---

## Menus

São responsáveis pela interação com o usuário através do terminal.

---

## Utils

Reúnem funções auxiliares para validação de entradas e formatação de informações.

---

## Data

Responsável pelo armazenamento permanente das informações do sistema.

---

# 📈 Fluxo de Funcionamento

```text
Usuário

      │

      ▼

Menus

      │

      ▼

Services

      │

      ▼

Models

      │

      ▼

Persistência (JSON)
```

---

# 📷 Demonstração

Nesta seção podem ser adicionadas capturas de tela do funcionamento do sistema.

```
📸 Tela principal

📸 Cadastro de clientes

📸 Cadastro de imóveis

📸 Relatórios
```

---

# 👥 Equipe

| Integrante | Função |
|------------|---------|
| **Allana Camily** | Desenvolvimento |
| **Mayan** | Desenvolvimento |

---

# 🎓 Informações Acadêmicas

**Universidade Federal do Piauí (UFPI)**

**Curso:** Bacharelado em Sistemas de Informação

**Disciplina:** Programação Orientada a Objetos

**Ano:** 2026

---

# 📄 Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos como trabalho da disciplina de **Programação Orientada a Objetos**, sem finalidade comercial.

---

<div align="center">

## Obrigado por visitar este projeto!

Desenvolvido por **Allana Camily** e **Mayan**

</div>
