import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega a chave da API do arquivo .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Altera o nome do modelo para a versão mais atual
model = genai.GenerativeModel(model_name="gemini-pro-latest")

def gerar_cenario_ia(requisito_texto):
    """
    Gera um cenário de teste no formato Xray a partir de um requisito funcional,
    utilizando o modelo Gemini-Pro com o método de chat.
    """

    prompt = f"""
Você é um engenheiro de QA que transforma requisitos funcionais em cenários de teste no formato Xray.
... (rest of your prompt code)
"""

    # Altera o nome do modelo para a versão mais atual
    model = genai.GenerativeModel("gemini-pro-latest")

    # Usa chat (compatível com v1beta)
    chat = model.start_chat()
    response = chat.send_message(prompt)

    return response.text.strip()