# src/mock_data.py

import sqlite3
import os

db_path = "../data/falhas.db"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Corrigido: adiciona coluna status_esperado
cursor.execute("""
CREATE TABLE IF NOT EXISTS falhas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    endpoint TEXT,
    status_esperado INTEGER,
    status_obtido INTEGER,
    mensagem TEXT
)
""")

dados_ficticios = [
    ("/api/users", 201, 500, "Erro interno ao criar usuário"),
    ("/api/users", 201, 400, "Payload inválido"),
    ("/api/users", 201, 400, "Campo obrigatório ausente"),
    ("/api/posts", 200, 404, "Post não encontrado"),
    ("/api/login", 200, 403, "Permissão negada"),
    ("/api/dashboard", 200, 500, "Erro ao carregar dashboard"),
    ("/api/admin", 200, 403, "Acesso negado ao admin")
]

cursor.executemany(
    "INSERT INTO falhas (endpoint, status_esperado, status_obtido, mensagem) VALUES (?, ?, ?, ?)",
    dados_ficticios
)

conn.commit()
conn.close()

print("✅ Dados fictícios inseridos no banco com sucesso.")

