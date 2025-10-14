from src.llm_interface import model

def gerar_cenario(requisito):
    prompt = f"""
    Gera um cenário de teste no formato Xray a partir de um requisito funcional,
    utilizando o modelo Gemini-Pro com o método de chat:

    Requisito:
    {requisito}

    O cenário deve ser claro, objetivo e simular uma situação realista de teste.
    """

    response = model.generate_content(prompt)

    return response.text
