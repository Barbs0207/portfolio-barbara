import requests
import json

# 📂 Carrega os endpoints do arquivo JSON
with open("endpoints.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

resultados = []

# 🧪 Executa os testes
def executar_endpoint(endpoint):
    nome = endpoint["nome"]
    url = endpoint["url"]
    metodo = endpoint.get("metodo", "GET").upper()
    esperado = endpoint.get("esperado", 200)
    payload = endpoint.get("payload")

    try:
        if metodo == "POST":
            resposta = requests.post(url, json=payload)
        elif metodo == "PUT":
            resposta = requests.put(url, json=payload)
        elif metodo == "DELETE":
            resposta = requests.delete(url)
        else:
            resposta = requests.get(url)

        status_code = resposta.status_code
        sucesso = status_code == esperado

    except Exception as e:
        status_code = str(e)
        sucesso = False

    resultado = {
        "nome": nome,
        "metodo": metodo,
        "url": url,
        "esperado": esperado,
        "obtido": status_code,
        "status": "Sucesso" if sucesso else "Falha"
    }

    return resultado

# 🧾 Gera relatório HTML
def gerar_relatorio_html(resultados, nome_arquivo="relatorio.html"):
    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Relatório de Testes de Endpoints</title>
        <style>
            body { font-family: Arial; background: #f9f9f9; padding: 20px; }
            h1 { color: #444; }
            table { border-collapse: collapse; width: 100%; margin-top: 20px; }
            th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
            th { background-color: #eee; }
            .sucesso { background-color: #c8e6c9; } /* Verde claro */
            .falha { background-color: #ffcdd2; }   /* Vermelho claro */
        </style>
    </head>
    <body>
        <h1>Relatório de Testes de Endpoints</h1>
        <table>
            <tr>
                <th>Nome</th>
                <th>Método</th>
                <th>URL</th>
                <th>Esperado</th>
                <th>Obtido</th>
                <th>Resultado</th>
            </tr>
    """

    for item in resultados:
        classe = "sucesso" if item["status"] == "Sucesso" else "falha"
        html += f"""
        <tr class="{classe}">
            <td>{item['nome']}</td>
            <td>{item['metodo']}</td>
            <td>{item['url']}</td>
            <td>{item['esperado']}</td>
            <td>{item['obtido']}</td>
            <td>{item['status']}</td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(html)

# 🚀 Executa os testes em todos os endpoints
print("\n🔍 Testando endpoints:\n")
for endpoint in dados:
    resultado = executar_endpoint(endpoint)
    resultados.append(resultado)
    simbolo = "✅" if resultado["status"] == "Sucesso" else "❌"
    print(f"{resultado['nome']}: {simbolo} {resultado['status']}")

# 🖨️ Gera o relatório no final
gerar_relatorio_html(resultados)
print("\n📄 Relatório gerado: relatorio.html")
