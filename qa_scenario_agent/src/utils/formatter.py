def formatar_output(cenario_texto):
    """
    Limpa e formata o texto retornado pela IA para garantir que siga
    o padrão Xray com divisões bem marcadas.
    """
    linhas = cenario_texto.strip().splitlines()
    linhas_formatadas = []

    for linha in linhas:
        if linha.strip().startswith("✅"):
            linhas_formatadas.append("\n# ✅ Test Header\n")
        elif linha.strip().startswith("🔍"):
            linhas_formatadas.append("\n# 🔍 Scenario Description\n")
        elif linha.strip().startswith("🧪"):
            linhas_formatadas.append("\n# 🧪 Test Steps\n")
        elif linha.strip().startswith("📎"):
            linhas_formatadas.append("\n# 📎 Evidence Tips\n")
        elif linha.strip().startswith("🗂️"):
            linhas_formatadas.append("\n# 🗂️ Test Set\n")
        else:
            linhas_formatadas.append(linha)
    
    return "\n".join(linhas_formatadas)
