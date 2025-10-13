# main.py

from src.analisador import analisar_falhas

CAMINHO_DB = "../data/falhas.db" # <--- ATENÇÃO: Troquei para "historico_resultados.db"
CAMINHO_RELATORIO = "reports/relatorio_estrategico.md"

if __name__ == "__main__":
    insights = analisar_falhas(CAMINHO_DB)
    print("✅ Análise concluída:\n")
    print(insights)

  
