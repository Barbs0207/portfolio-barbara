# src/main.py

from analizador import analisar_falhas
from gerador_relatorio import gerar_md

CAMINHO_DB = "data/falhas.db"
CAMINHO_RELATORIO = "reports/relatorio_estrategico.md"

if __name__ == "__main__":
    insights = analisar_falhas(CAMINHO_DB)
    print("✅ Análise concluída:\n")
    print(insights)

    gerar_md(insights, CAMINHO_RELATORIO)
    print(f"\n📄 Relatório salvo em: {CAMINHO_RELATORIO}")
