# src/analizador.py

import sqlite3
from collections import Counter, defaultdict

def analisar_falhas(caminho_db):
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    cursor.execute("SELECT endpoint, status_esperado, status_obtido FROM falhas")
    registros = cursor.fetchall()

    if not registros:
        return "Nenhuma falha encontrada."

    total = len(registros)
    erros_por_endpoint = Counter([r[0] for r in registros])
    endpoints_criticos = erros_por_endpoint.most_common(3)

    # Sugestões por status
    sugestoes = defaultdict(set)

    for endpoint, esperado, obtido in registros:
        if obtido == 400:
            sugestoes[endpoint].add("Testar payloads inválidos ou campos obrigatórios ausentes.")
        elif obtido == 403:
            sugestoes[endpoint].add("Verificar testes de permissão e autenticação.")
        elif obtido == 404:
            sugestoes[endpoint].add("Testar IDs inexistentes ou rotas malformadas.")
        elif obtido == 500:
            sugestoes[endpoint].add("Simular entradas extremas ou inconsistentes para forçar o erro.")

    insights = f"🔍 Total de falhas registradas: {total}\n\n"
    insights += "🔥 Endpoints com mais falhas:\n"
    for endpoint, qtd in endpoints_criticos:
        insights += f" - {endpoint} → {qtd} falha(s)\n"

    insights += "\n🧠 Recomendações Inteligentes:\n"
    for endpoint, sugestao_set in sugestoes.items():
        insights += f"\n🔸 **{endpoint}**:\n"
        for s in sugestao_set:
            insights += f"   - {s}\n"

    conn.close()
    return insights


if __name__ == "__main__":
    caminho_db = "data/falhas.db"
    print("\n🔎 Analisando falhas de QA...\n")
    resultado = analisar_falhas(caminho_db)
    print(resultado)
    print("\n✅ Análise concluída com sucesso!\n")

