📝 README.md – Versão Atualizada
# 🔍 Validação de Endpoints – Projeto em Python com GitHub Actions

Este projeto realiza a **validação automática de endpoints HTTP** (GET, POST, PUT etc.) usando Python. É ideal para garantir que APIs estejam respondendo corretamente, com status esperados, e fornece um relatório HTML com os resultados.

---

## 🚀 Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/Barbs0207/portfolio-barbara.git
cd portfolio-barbara/EndCheck


Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
venv\Scripts\activate


Instale as dependências:

pip install -r requirements.txt


Execute o validador:

python multichecker.py


Ao final, um arquivo relatorio.html será gerado com o resultado dos testes.

🤖 Validação Automática via GitHub Actions

Este projeto possui um workflow CI para rodar automaticamente a verificação dos endpoints no GitHub:

Acesse a aba Actions

Clique em Validação de Endpoints

Clique em Run Workflow

O resultado aparecerá no histórico e poderá ser baixado em breve como artefato .html.

📁 Estrutura do Projeto
📦 EndCheck
 ┣ 📄 endpoints.json            ← Lista de endpoints a validar
 ┣ 📄 multichecker.py           ← Script principal de execução
 ┣ 📄 validador.py              ← Função que realiza a requisição
 ┗ 📄 relatorio.html            ← Relatório de resultados

🧪 Tecnologias Usadas

Python 3.13

requests para chamadas HTTP

json, datetime, html para estrutura e relatório

GitHub Actions para CI/CD

👩‍💻 Autora

Desenvolvido por Bárbara Filadelfo – QA Engineer, apaixonada por qualidade, automação, pets e soluções inteligentes.
🔗 www.linkedin.com/in/barbara-filadelfo-150895237

💡 Projeto parte do portfólio profissional.
