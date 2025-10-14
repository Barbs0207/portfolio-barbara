from src.generator import gerar_cenario

def main():
    print("🚀 Iniciando o agente de geração de cenários de teste...\n")

    try:
        # Lê o requisito de exemplo
        with open("examples/requisito_exemplo.txt", "r", encoding="utf-8") as f:
            requisito = f.read()

        # Gera o cenário
        cenario = gerar_cenario(requisito)

        # Salva o resultado
        output_path = "outputs/scenario_output.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cenario)

        print(f"✅ Cenário de teste gerado com sucesso!\nArquivo salvo em: {output_path}")

    except Exception as e:
        print("❌ Ocorreu um erro ao gerar o cenário:")
        print(e)


if __name__ == "__main__":
    main()
