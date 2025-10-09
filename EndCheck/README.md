# 🔍 Validação de Endpoints – Projeto em Python com GitHub Actions

Este projeto realiza a validação automática de endpoints HTTP (GET, POST, PUT etc.), usando Python.  
É ideal para garantir que APIs estejam respondendo corretamente, com status esperados, e fornece um relatório HTML com os resultados.

---

## 📌 Como executar localmente

### 1. Clone o repositório:

```bash
git clone https://github.com/Barbs0207/portfolio-barbara.git
cd portfolio-barbara/EndCheck
```

### 2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute o validador:

```bash
python multichecker.py
```

> Ao final, um arquivo `relatorio.html` será gerado com o resultado dos testes.

---

## 🤖 Validação automática via GitHub Actions

Este projeto possui um workflow CI que roda manualmente a verificação dos endpoints no GitHub:

1. Acesse a aba **Actions**
2. Clique em **Validação de Endpoints**
3. Clique em **Run workflow**

O relatório será gerado no histórico e poderá ser baixado em breve como artefato `.html`.

---

## 📁 Estrutura do Projeto

```text
📦 EndCheck/
 ┣ 📄 endpoints.json        # Lista de endpoints a validar
 ┣ 📄 multichecker.py       # Script principal de execução
 ┣ 📄 validador.py          # Função de validação do endpoint
 ┗ 📄 relatorio.html        # Relatório gerado com os resultados
```

---

## 🧪 Tecnologias usadas

- Python 3.13
- Requests (HTTP Client)
- JSON, datetime, HTML para estrutura e relatório
- GitHub Actions (CI/CD)

---

## 👩‍💻 Autora

Desenvolvido por **Bárbara Filadelfo** — QA Engineer, apaixonada por qualidade, automação, pets e soluções inteligentes.  
🔗 [LinkedIn](https://www.linkedin.com/in/barbara-filadelfo-150895237/)  

> 💼 Projeto feito como parte do portfólio profissional.

---

## 📈 Próximos passos

- [ ] Adicionar agendamento automático via cron
- [ ] Salvar `relatorio.html` como artefato no GitHub
- [ ] Separar endpoints por ambiente (`dev`, `qa`, `prod`)
- [ ] Adicionar testes com Pytest

---
