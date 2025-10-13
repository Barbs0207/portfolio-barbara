# src/gerador_relatorio.py

from analisador import analisar_falhas
from datetime import datetime

caminho_db = "data/falhas.db"
resultado = analisar_falhas(caminho_db)

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

html = f"""
<html>
<head><meta charset="utf-8"><title>Relatório Inteligente de QA</title></head>
<body>
<h1>🧪 Relatório de Análise de Falhas QA</h1>
<p><strong>Gerado em:</strong> {agora}</p>
<pre style="font-family: Consolas, monospace; background-color: #f5f5f5; padding: 10px;">{resultado}</pre>
</body>
</html>
"""

with open("relatorio_inteligente.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Relatório HTML gerado com sucesso: relatorio_inteligente.html")

