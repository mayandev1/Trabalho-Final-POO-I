# Trabalho Final de POO I - Sistema de Gerenciamento de Imóveis

Sistema em Python para uma imobiliária, usando Programação Orientada a Objetos e menu no terminal.

## Como executar

```bash
python main.py
```

## Estrutura

```text
models/      Classes do domínio: Pessoa, Cliente, Proprietario, Imovel, Casa, Apartamento
services/    Regras de negócio, persistência, relatórios, validações e dados de exemplo
menus/       Menus do terminal separados por módulo
utils/       Funções auxiliares de entrada, formatação e tela
data/        Arquivo JSON com dados persistidos
exports/     Relatórios TXT e CSV exportados
```

## Diferenciais implementados

- Persistência em JSON
- Menu terminal modularizado
- Relatórios completos
- Histórico de negociações
- Busca avançada
- Exportação TXT e CSV
- Dados pré-carregados para apresentação
- Validações e tratamento de exceções
- `__init__.py` nos pacotes para facilitar imports
- `main.py` limpa, apenas iniciando o sistema
