import streamlit as st
from src.generator import gerar_cenario

st.set_page_config(page_title="Agente QA - Cenário Xray", layout="wide")

st.title("💡 Agente de Geração de Cenários de Teste")
st.subheader("Transforme requisitos funcionais em cenários Xray automaticamente")

# Área de texto para digitar o requisito
requisito = st.text_area("✍️ Escreva ou cole o requisito funcional abaixo:", height=300)

# Quando clicar no botão
if st.button("🚀 Gerar Cenário Xray"):
    if not requisito.strip():
        st.warning("Por favor, insira um requisito antes de gerar o cenário.")
    else:
        with st.spinner("Gerando cenário..."):
            try:
                cenario = gerar_cenario(requisito)
                st.success("✅ Cenário gerado com sucesso!")
                st.markdown("### 📄 Cenário Gerado:")
                st.code(cenario, language="markdown")

                # Opção para download
                st.download_button(
                    label="📥 Baixar cenário em .md",
                    data=cenario,
                    file_name="cenario_teste_xray.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error("❌ Ocorreu um erro ao gerar o cenário:")
                st.exception(e)
