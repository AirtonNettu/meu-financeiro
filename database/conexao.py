import sqlite3


def conectar():
    conexao = sqlite3.connect("meu_financeiro.db")
    return conexao


def criar_tabela_movimentacoes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            tipo TEXT NOT NULL,
            data TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


criar_tabela_movimentacoes()

print("Banco e tabela inicializados com sucesso!")

def adicionar_movimentacao(descricao, valor, tipo, data):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO movimentacoes (descricao, valor, tipo, data)
        VALUES (?, ?, ?, ?)
    """, (descricao, valor, tipo, data))

    conexao.commit()
    conexao.close()

def listar_movimentacoes():
    conexao = conectar()
    cursor = conexao.cursor()


    cursor.execute("""
        SELECT * FROM movimentacoes
    """)

    movimentacoes = cursor.fetchall()

    conexao.close()
    return movimentacoes


def calcular_saldo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT SUM(
            CASE
                WHEN tipo = 'receita' THEN valor
                WHEN tipo = 'despesa' THEN -valor
                ELSE 0
            END
        )
        FROM movimentacoes
    """)

    resultado = cursor.fetchone()

    conexao.close()

    saldo = resultado[0]

    if saldo is None:
        saldo = 0

    return saldo