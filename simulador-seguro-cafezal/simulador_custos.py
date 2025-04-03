# Funções de cálculo
def calcular_subvencao(valor_total, percentual, limite):
    """Aplica a subvenção com base no percentual e respeitando o limite."""
    subvencao = valor_total * percentual
    return min(subvencao, limite)

# Bloco principal
if __name__ == "__main__":
    # Dados do exemplo (linha 40 da planilha - REDUZIDA)
    municipio = "Cássia - MG"
    area = 10  # hectares (entrada simulada)

    # Valores extraídos da planilha para a simulação (já deduzidos)
    cobertura = 126000.00
    futura = 94500.00
    fitossanitario = 5000.00
    taxa_reduzida = 0.0546

    base_total = cobertura + futura + fitossanitario
    premio = base_total * taxa_reduzida

    print(f"Município: {municipio}")
    print(f"Área: {area} ha")
    print(f"\n🧮 Base de cálculo:")
    print(f"➤ Cobertura básica: R$ {cobertura:.2f}")
    print(f"➤ Produção futura: R$ {futura:.2f}")
    print(f"➤ Tratamento fitossanitário: R$ {fitossanitario:.2f}")
    print(f"📊 Total base: R$ {base_total:.2f}")
    print(f"💰 Prêmio total calculado: R$ {premio:.2f}")

    # Subvenções conforme a planilha
    percentual_estadual = 0.30
    limite_estadual = 25000
    percentual_federal = 0.40
    limite_federal = 60000

    subvencao_estadual = calcular_subvencao(premio, percentual_estadual, limite_estadual)
    subvencao_federal = calcular_subvencao(premio, percentual_federal, limite_federal)

    investimento_produtor = premio - subvencao_estadual - subvencao_federal

    print(f"\n📉 Subvenção estadual aplicada: R$ {subvencao_estadual:.2f}")
    print(f"📉 Subvenção federal aplicada: R$ {subvencao_federal:.2f}")
    print(f"🧑‍🌾 Investimento final do produtor: R$ {investimento_produtor:.2f}")

    # Parcelamento
    parcelas = 5
    valor_parcela = investimento_produtor / parcelas
    print(f"\n📆 Parcelamento em {parcelas}x de: R$ {valor_parcela:.2f}")


