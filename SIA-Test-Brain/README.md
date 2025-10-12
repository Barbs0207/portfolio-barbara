
# 🧠 SIA-Test-Brain

Sistema Inteligente de Análise de Falhas em APIs — desenvolvido por [Bárbara Filadelfo](https://www.linkedin.com/in/barbara-filadelfo-150895237)

---

## 💡 Visão Geral

O `SIA-Test-Brain` é um agente inteligente de QA que analisa falhas registradas durante testes de APIs e transforma os dados em **recomendações estratégicas**, ajudando times de qualidade a priorizar cenários críticos de forma eficiente e orientada por dados.

Este projeto faz parte do portfólio da **SIA**, uma IA emocional e estratégica desenvolvida por Bárbara Filadelfo, que une automação, análise e inteligência em um só sistema.

---

## 🛠️ Funcionalidades

- 📊 Leitura de um banco de dados SQLite com falhas de endpoints
- 🔎 Análise de padrões de erro por endpoint
- 🤖 Geração de recomendações automatizadas com base no tipo de erro
- 📄 Exportação de relatório em HTML com visual atrativo e informativo

---

## 🔍 Tecnologias Utilizadas

- `Python 3.13`
- `SQLite3`
- `Jinja2` para geração do relatório HTML
- `datetime` para marcação de data/hora
- Projeto estruturado com base em **Clean Code**

---

## 📁 Estrutura do Projeto

```
SIA-Test-Brain/
│
├── src/
│   ├── analisador.py           # Lê o banco e gera dados estratégicos
│   ├── gerador_relatorio.py    # Gera o relatório HTML final
│   ├── mock_data.py            # Popular o banco com dados fictícios
│   ├── templates/
│   │   └── relatorio_template.html  # Template HTML com Jinja2
│
├── dados/
│   └── falhas.db               # Banco SQLite com os dados de falhas
│
├── relatorios/
│   └── relatorio_qa.html       # Relatório gerado
│
└── README.md
```

---

## ▶️ Como Executar Localmente

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/SIA-Test-Brain.git
cd SIA-Test-Brain
```

2. **Crie e ative um ambiente virtual (opcional)**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Popule o banco de dados com dados fictícios (opcional)**
```bash
python src/mock_data.py
```

5. **Execute o analisador**
```bash
python src/analisador.py
```

6. **Gere o relatório HTML**
```bash
python src/gerador_relatorio.py
```

O relatório será salvo em `relatorios/relatorio_qa.html`.

---

## 🚀 Próximas Evoluções

- Integração com CI/CD (GitHub Actions)
- Exportação em Markdown e PDF
- Interface web com Flask
- Dashboards de análise contínua
- Integração com Slack e Notion

---

## 👩‍💻 Autora

**Bárbara Filadelfo**  
Analista de Qualidade Sênior | Dev em formação | Apaixonada por IA  
🔗 [LinkedIn](https://www.linkedin.com/in/barbara-filadelfo-150895237)

---

## 📄 Licença

Este projeto é de uso pessoal e está em constante evolução. Para uso comercial ou contribuições, entre em contato com a autora.

---
