# main.py

import os
from src.analisador import analisar_falhas
from src.gerador_relatorio import gerar_md

CAMINHO_DB = os.environ.get('CAMINHO_DB_ABSOLUTO') or "../data/falhas.db"
CAMINHO_RELATORIO = "reports/relatorio_inteligente.html"

if __name__ == "__main__":
    insights = analisar_falhas(CAMINHO_DB)
    print("✅ Análise concluída:\n")
    print(insights)

    gerar_md(insights, CAMINHO_RELATORIO)
    print(f"\n📄 Relatório salvo em: {CAMINHO_RELATORIO}")