# 🏦 API Bancária Assíncrona com FastAPI

API RESTful assíncrona desenvolvida com FastAPI para gerenciar operações bancárias básicas como depósitos, saques e consulta de extrato, utilizando autenticação JWT e boas práticas de APIs modernas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- SQLAlchemy (Async)
- SQLite (facilmente substituível por PostgreSQL)
- JWT (JSON Web Token)
- Passlib (bcrypt)
- Uvicorn

---

## 🔐 Autenticação

A API utiliza autenticação baseada em JWT (JSON Web Token).

Fluxo:
1. O usuário realiza o cadastro
2. Efetua login
3. Recebe um token JWT
4. Utiliza o token para acessar endpoints protegidos

Header de autenticação:

Authorization: Bearer SEU_TOKEN_AQUI

---

## 📌 Funcionalidades

- Cadastro de usuários
- Login com geração de JWT
- Criação automática de conta bancária
- Depósito em conta
- Saque com validação de saldo
- Consulta de extrato de transações
- API totalmente assíncrona

---

## ⚙️ Como Executar o Projeto

1. Clonar o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git  
cd bank_api

---

2. Criar ambiente virtual (opcional):

python -m venv venv  
source venv/bin/activate   (Linux/Mac)  
venv\Scripts\activate      (Windows)

---

3. Instalar as dependências:

pip install -r requirements.txt

---

4. Executar a aplicação:

uvicorn app.main:app --reload