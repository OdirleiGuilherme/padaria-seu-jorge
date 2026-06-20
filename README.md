# 📦 Sistema de Cadastro de Fornecedores

![GitHub repo size](https://img.shields.io/github/repo-size/seu-usuario/seu-repositorio?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/seu-usuario/seu-repositorio?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/seu-usuario/seu-repositorio?style=for-the-badge)

> Um sistema simples em Python para gerenciamento, validação e persistência de dados de fornecedores.

### 🔨 Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão:
- [x] Criação do Model de Fornecedor
- [ ] Implementação de Banco de Dados (SQLite/PostgreSQL)
- [ ] Interface de linha de comando (CLI) ou API com Flask/FastAPI
- [ ] Validação real de CNPJ

---

## 💻 Sobre o projeto

Este projeto foi desenvolvido para resolver o problema de gerenciamento de fornecedores na padaria seu Jorge. 
Ele utiliza o padrão arquitetural MVC (focado na camada de Model) para separar a lógica de negócio e a entidade `Fornecedor`.

O padrão MVC separa a aplicação em três camadas lógicas:

**Model (Camada de Dados):** Localizada na pasta `models/`. Contém as classes `Fornecedor` e `Produto`, 
além de simular o banco de dados (armazenamento em memória) e aplicar regras de consistência dos dados.

**View (Camada de Interface):** Localizada na pasta `views/`. Responsável por renderizar o menu no terminal,
interagir com o usuário e capturar as entradas do teclado.

**Controller (Camada de Controle):** Localizada na pasta `controllers/`. É o cérebro da aplicação. 
Intermedia a comunicação entre a View e o Model, além de validar regras de negócio (como impedir o cadastro de um produto se o fornecedor não existir).

## 📂 Estrutura de Pastas

```text
padaria_seu_jorge/
│
├── docs/
|
├── src/
     ├── models/
│    ├── __init__.py
│    ├── fornecedor.py       # Estrutura e armazenamento de fornecedores
│    └── produto.py          # Estrutura e armazenamento de produtos
│
|    ├── views/
│    ├── __init__.py
│    └── padaria_view.py     # Interface de linha de comando (entradas e saídas)
│
|    ├── controllers/
│    ├── __init__.py
│    └── padaria_controller.py # Lógica de negócio e orquestração do sistema
│
└── main.py                 # Ponto de entrada do sistema

### Recursos atuais:
- **Entidade Fornecedor:** Armazena ID, Nome, CNPJ e Telefone.
- **Camada Model:** Gerencia a persistência (em memória) dos dados, permitindo salvar e listar registros.

---

## 🚀 Como executar o projeto

### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina o [Python 3.x](https://www.python.org/downloads/).

### 🎲 Rodando a aplicação

A atualizar

🛠 Tecnologias
As seguintes ferramentas foram usadas na construção do projeto:

Python (Linguagem base)

Git & GitHub (Controle de versão)

👤 Autor
Feito com ❤️ por Odirlei Guilherme. Entre em contato!
