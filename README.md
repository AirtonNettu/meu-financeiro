# Meu Financeiro

Sistema Financeiro Pessoal desenvolvido como projeto real de uso diário e, ao mesmo tempo, como projeto de aprendizado em desenvolvimento de software.

O objetivo é construir uma aplicação capaz de registrar, organizar e analisar informações financeiras pessoais de forma simples, segura e progressiva.

> Projeto em desenvolvimento — ETAPA 1: Sistema Funcional.

---

## 🎯 Objetivo

O Meu Financeiro será utilizado para acompanhar informações como:

- Receitas
- Despesas
- Saldo
- Movimentações financeiras
- Despesas recorrentes
- Cartão de crédito
- Compras parceladas
- Dívidas
- Reserva financeira
- Rescisão
- Seguro-desemprego
- Metas
- Projeções financeiras

O princípio financeiro central do projeto é:

> Segurança financeira > Liquidez > Previsibilidade > Rendimento > Consumo

---

## 🛠️ Stack atual

- Python
- FastAPI
- Uvicorn
- SQLite
- uv
- Git
- GitHub

HTML, CSS e JavaScript serão utilizados futuramente na construção da interface.

---

## 🏗️ Arquitetura atual

```text
Cliente / Swagger
        ↓
      HTTP
        ↓
     FastAPI
        ↓
      Routes
        ↓
Funções Python
        ↓
      SQLite
```

### Estrutura atual

```text
meu-financeiro/
│
├── database/
│   ├── __init__.py
│   └── conexao.py
│
├── routes/
│   ├── __init__.py
│   ├── saldo.py
│   └── movimentacoes.py
│
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

---

## ⚙️ Funcionalidades implementadas

Atualmente o projeto possui:

- Aplicação FastAPI executando localmente
- Documentação automática utilizando Swagger
- Organização das rotas utilizando `APIRouter`
- Separação da aplicação em módulos
- Rota de saldo
- Rota inicial de movimentações
- Banco de dados SQLite
- Criação automática da tabela `movimentacoes`
- Persistência local de dados
- Inserção de movimentações no banco
- Consulta das movimentações armazenadas
- Cálculo do saldo utilizando os dados persistidos no SQLite

---

## 🌐 Endpoints atuais

### GET /

Verifica se a API está funcionando.

```http
GET /
```

---

### GET /saldo/

Consulta o saldo financeiro calculado a partir das movimentações armazenadas no banco de dados.

```http
GET /saldo/
```

Fluxo:

```text
GET /saldo/
     ↓
FastAPI
     ↓
routes/saldo.py
     ↓
calcular_saldo()
     ↓
SQLite
     ↓
SUM das movimentações
     ↓
JSON
```

Exemplo de resposta:

```json
{
    "saldo": 100
}
```

---

### GET /movimentacoes/

Endpoint inicial responsável pelo módulo de movimentações.

```http
GET /movimentacoes/
```

Atualmente essa rota já está registrada e funcionando no FastAPI.

Ela será evoluída para permitir consulta e cadastro de movimentações reais diretamente através da API.

---

## 🗄️ Banco de dados

Na primeira etapa do projeto utilizamos:

**SQLite**

O SQLite permite trabalhar com um banco de dados local armazenado em um arquivo, sem precisar instalar ou manter um servidor de banco de dados separado.

O banco atual utiliza a tabela:

```text
movimentacoes
```

### Estrutura da tabela

```text
id
descricao
valor
tipo
data
```

Exemplo conceitual:

| id | descricao | valor | tipo | data |
|---|---|---:|---|---|
| 1 | Teste de receita | 100.00 | entrada | 2026-09-01 |

---

## 🔌 Conexão com SQLite

A conexão com o banco é realizada utilizando a biblioteca nativa:

```python
import sqlite3
```

A função:

```python
conectar()
```

é responsável por abrir uma conexão com o banco.

Fluxo:

```text
Python
   ↓
sqlite3
   ↓
meu_financeiro.db
```

---

## 🧱 Criação da tabela

A função:

```python
criar_tabela_movimentacoes()
```

utiliza:

```sql
CREATE TABLE IF NOT EXISTS
```

Isso significa:

> Criar a tabela somente caso ela ainda não exista.

A chave:

```sql
PRIMARY KEY AUTOINCREMENT
```

faz o `id` aumentar automaticamente.

Exemplo:

```text
1
2
3
4
5
...
```

Os campos definidos com:

```sql
NOT NULL
```

são obrigatórios e não podem receber valores nulos.

---

## ➕ Inserção de movimentações

A função:

```python
adicionar_movimentacao()
```

é responsável por adicionar dados ao SQLite.

O comando utilizado é:

```sql
INSERT INTO
```

Os valores são enviados utilizando placeholders:

```sql
VALUES (?, ?, ?, ?)
```

em vez de montar comandos SQL manualmente com strings.

Isso também ajuda a evitar problemas de segurança, como SQL Injection.

---

## 🔎 Consulta de movimentações

A função:

```python
listar_movimentacoes()
```

consulta os registros utilizando:

```sql
SELECT * FROM movimentacoes
```

O método:

```python
fetchall()
```

pega todos os registros encontrados pela consulta e os entrega ao Python.

Fluxo:

```text
SQLite
   ↓
SELECT
   ↓
fetchall()
   ↓
Python
```

---

## 💰 Cálculo do saldo

O saldo não fica escrito manualmente dentro da rota.

Ele é calculado utilizando as movimentações armazenadas no banco.

A consulta utiliza:

```sql
SUM()
```

para somar os valores.

A lógica financeira considera:

```text
entrada → soma
saída   → subtrai
```

Exemplo:

```text
Salário       + R$ 1.500
Internet      - R$    60
Energia       - R$    80
-----------------------
Saldo          R$ 1.360
```

Esse conceito permite que o saldo seja derivado das movimentações reais em vez de existir como um número fixo no código.

---

## 🧠 Conceitos estudados durante o desenvolvimento

Durante esta etapa foram utilizados conceitos importantes de desenvolvimento backend.

### FastAPI

Framework Python utilizado para construir a API.

### API

Interface utilizada para permitir comunicação entre diferentes partes do sistema.

### Endpoint

Endereço específico disponibilizado pela API.

Exemplo:

```text
/saldo/
/movimentacoes/
```

### HTTP

Protocolo utilizado na comunicação entre cliente e servidor.

### GET

Método HTTP utilizado para consultar informações.

### JSON

Formato utilizado pela API para retornar dados.

Exemplo:

```json
{
    "saldo": 100
}
```

### Router

Permite separar endpoints em arquivos diferentes.

Utilizamos:

```python
APIRouter
```

Isso evita colocar todas as rotas dentro do `main.py`.

### SQLite

Banco de dados relacional local utilizado pelo projeto.

### SQL

Linguagem utilizada para conversar com bancos de dados relacionais.

Até agora utilizamos conceitos como:

```sql
CREATE TABLE
INSERT INTO
SELECT
SUM
```

### Cursor

Objeto utilizado pelo Python para enviar comandos SQL ao SQLite.

Exemplo:

```python
cursor = conexao.cursor()
```

### execute()

Executa um comando SQL.

```python
cursor.execute(...)
```

### commit()

Confirma alterações realizadas no banco.

```python
conexao.commit()
```

### close()

Fecha a conexão com o banco.

```python
conexao.close()
```

### fetchone()

Obtém um único resultado de uma consulta.

### fetchall()

Obtém todos os resultados encontrados.

### Persistência

Significa manter os dados armazenados mesmo depois que o programa é encerrado.

Antes do SQLite:

```text
Programa fecha
     ↓
Dados desaparecem
```

Com SQLite:

```text
Programa
   ↓
SQLite
   ↓
Disco
   ↓
Programa fecha
   ↓
Dados continuam armazenados
```

---

## 🔄 Fluxo atual da aplicação

O projeto já começa a possuir uma arquitetura backend real:

```text
Usuário
   ↓
Swagger / Cliente HTTP
   ↓
FastAPI
   ↓
Router
   ↓
Função Python
   ↓
SQLite
   ↓
Consulta / processamento
   ↓
Função Python
   ↓
FastAPI
   ↓
JSON
   ↓
Usuário
```

---

## 🔐 Segurança

Este projeto poderá trabalhar com dados financeiros pessoais reais.

Por isso, bancos de dados reais não devem ser enviados ao GitHub.

Arquivos como:

```text
*.db
*.sqlite
*.sqlite3
.env
.venv/
```

devem permanecer no `.gitignore`.

Isso evita publicar:

- dados financeiros pessoais;
- credenciais;
- tokens;
- chaves;
- configurações privadas.

Demonstrações públicas do projeto deverão utilizar dados fictícios.

---

## ▶️ Executando o projeto

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre na pasta:

```bash
cd meu-financeiro
```

Sincronize o ambiente:

```bash
uv sync
```

Execute:

```bash
uv run uvicorn main:app --reload
```

Servidor local:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 🗺️ Roadmap

O projeto possui três grandes etapas.

### ETAPA 1 — Sistema Funcional

Construção do sistema financeiro tradicional, local e realmente utilizável.

**Status: 🚧 Em desenvolvimento**

Objetivo:

> Conseguir utilizar o Meu Financeiro no dia a dia.

---

### ETAPA 2 — Sistema Online e Evolução

Possíveis evoluções:

- autenticação;
- interface web;
- backup;
- acesso seguro pela internet;
- relatórios;
- gráficos;
- melhorias de experiência;
- evolução da arquitetura.

---

### ETAPA 3 — Inteligência e Automação

Possível integração de inteligência artificial para interpretar os resultados produzidos pelo sistema.

Princípio:

```text
Python calcula.
SQLite armazena.
IA interpreta.
```

A inteligência artificial não deve substituir a lógica financeira determinística do sistema.

---

## 📚 Metodologia de desenvolvimento

Este projeto também é utilizado como ambiente de aprendizado.

O fluxo adotado é:

```text
ENTENDER
   ↓
IMPLEMENTAR
   ↓
EXECUTAR
   ↓
TESTAR
   ↓
ERRAR
   ↓
INVESTIGAR
   ↓
CORRIGIR
   ↓
ENTENDER O ERRO
   ↓
COMMITAR
   ↓
CONTINUAR
```

O objetivo não é apenas fazer o código funcionar.

O objetivo é entender:

- o que cada parte faz;
- por que ela existe;
- como os componentes se comunicam;
- como identificar erros;
- como organizar um projeto backend;
- como evoluir gradualmente uma aplicação real.

---

## 📌 Status atual

🚧 **Projeto em desenvolvimento**

Primeiro marco técnico:

> Aplicação FastAPI local organizada em rotas, conectada a um banco SQLite, capaz de persistir movimentações e utilizar os dados armazenados para calcular o saldo financeiro.

Próximos passos incluem evoluir o módulo de movimentações para cadastrar e consultar informações diretamente através da API.

---

## 📖 Projeto de aprendizado

O Meu Financeiro está sendo desenvolvido progressivamente enquanto novos conceitos de Python, Backend, APIs, SQL, banco de dados, arquitetura de software e segurança são estudados.

Por isso, a arquitetura será evoluída conforme novos conhecimentos forem adquiridos.

O foco não é construir tudo de uma vez.

O foco é construir, entender, testar e evoluir.