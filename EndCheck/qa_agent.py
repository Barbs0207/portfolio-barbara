from validador import executar_endpoint
import json
from datetime import datetime
import sqlite3
import requests

# Carrega os endpoints do JSON
with open("EndCheck/endpoints.json", "r", encoding="utf-8") as f:
    endpoints = json.load(f)

resultados = []

print("🔍 Iniciando validação dos endpoints...\n")

# Conecta ao banco SQLite
conn = sqlite3.connect("historico_resultados.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico (
        nome TEXT,
        status INTEGER,
        data TEXT
    )
''')

for ep in endpoints:
    print(f"⏳ Testando: {ep['nome']} ...")
    resultado = executar_endpoint(ep)

    resultado["comparativo"] = "N/A"  # Inicial

    # Comparar com histórico
    cursor.execute("SELECT status FROM historico WHERE nome = ? ORDER BY data DESC LIMIT 1", (ep["nome"],))
    anterior = cursor.fetchone()
    if anterior:
        resultado["comparativo"] = f"{anterior[0]} → {resultado['obtido']}"
    else:
        resultado["comparativo"] = f"--- → {resultado['obtido']}"

    # Verificação extra (multi-tarefa)
    verificacao = ep.get("verificacao_extra")
    if verificacao:
        try:
            resp = requests.get(verificacao["url"])
            status_code = resp.status_code
            esperado = verificacao.get("esperado", 200)
            resultado["verificacao_extra"] = "✅" if status_code == esperado else f"❌ {status_code} ≠ {esperado}"
        except Exception as e:
            resultado["verificacao_extra"] = f"❌ Erro: {str(e)}"
    else:
        resultado["verificacao_extra"] = "—"

    # Salva no banco
    cursor.execute("INSERT INTO historico (nome, status, data) VALUES (?, ?, ?)",
                   (resultado["nome"], resultado["obtido"], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    resultados.append(resultado)

conn.commit()
conn.close()

# Gera o HTML
agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
html = f"""
<html>
<head><title>Relatório de Testes QA</title></head>
<body>
<h1>Relatório - {agora}</h1>
<table border="1">
<tr>
    <th>Nome</th><th>Status</th><th>Mensagem</th><th>Comparativo</th><th>Verificação Extra</th>
</tr>
"""

for r in resultados:
    status = "✅" if r["sucesso"] else "❌"
    html += f"<tr><td>{r['nome']}</td><td>{status}</td><td>{r['mensagem']}</td><td>{r['comparativo']}</td><td>{r['verificacao_extra']}</td></tr>"

html += "</table></body></html>"

with open("relatorio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("📄 Relatório salvo como 'relatorio.html'.")
