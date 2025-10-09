import json
import sqlite3
from datetime import datetime
from validador import executar_endpoint
import requests

# Carrega os endpoints do JSON
with open("EndCheck/endpoints.json", "r", encoding="utf-8") as f:
    endpoints = json.load(f)

resultados = []

print("🔍 Iniciando validação dos endpoints...\n")

# Conecta (ou cria) banco de dados SQLite
conn = sqlite3.connect("historico_resultados.db")
cursor = conn.cursor()

# Cria tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico (
        nome TEXT,
        status INTEGER,
        data TEXT
    )
''')

# Função para executar verificação extra (GET)
def executar_verificacao_extra(verificacao):
    try:
        tipo = verificacao.get("tipo", "GET")
        url = verificacao.get("url")
        esperado = verificacao.get("esperado", 200)

        resposta = requests.get(url) if tipo == "GET" else None

        if resposta is None:
            return {"icone": "❌", "mensagem": f"Tipo não suportado: {tipo}"}

        sucesso = resposta.status_code == esperado
        comparativo = f"{resposta.status_code} = {esperado}" if sucesso else f"{resposta.status_code} ≠ {esperado}"
        icone = "✅" if sucesso else "❌"
        return {"icone": icone, "mensagem": comparativo}

    except Exception as e:
        return {"icone": "❌", "mensagem": f"Erro: {str(e)}"}


for ep in endpoints:
    print(f"⏳ Testando: {ep['nome']} ...")
    resultado = executar_endpoint(ep)
    verificacao_extra = ep.get("verificacao_extra")

    if resultado["sucesso"]:
        print("✅ Sucesso!\n")
    else:
        print(f"❌ Falha: {resultado['mensagem']}\n")

    # Verificação extra se houver
    if verificacao_extra:
        # Se usar {{id}}, tentar extrair ID da resposta
        if "{{id}}" in verificacao_extra["url"]:
            try:
                resposta = requests.post(ep["url"], json=ep.get("payload", {}))
                if resposta.status_code in [200, 201]:
                    data = resposta.json()
                    id_criado = data.get("id")
                    if id_criado:
                        verificacao_extra["url"] = verificacao_extra["url"].replace("{{id}}", str(id_criado))
            except:
                pass

        resultado["verificacao_extra"] = executar_verificacao_extra(verificacao_extra)
    else:
        resultado["verificacao_extra"] = None

    resultados.append(resultado)

    # Salva no banco
    cursor.execute("INSERT INTO historico (nome, status, data) VALUES (?, ?, ?)",
                   (resultado["nome"], resultado["obtido"], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

conn.commit()
conn.close()

# Gera relatório HTML
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
    esperado = r.get("esperado", "---")
    comparativo = f"{r['obtido']} → {esperado}" if r["obtido"] is not None else "---"
    verif = r["verificacao_extra"]
    verif_str = f"{verif['icone']} {verif['mensagem']}" if verif else "—"

    html += f"<tr><td>{r['nome']}</td><td>{status}</td><td>{r['mensagem']}</td><td>{comparativo}</td><td>{verif_str}</td></tr>"

html += "</table></body></html>"

with open("relatorio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("📄 Relatório salvo como 'relatorio.html'.")
