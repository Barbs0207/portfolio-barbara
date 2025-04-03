![Python](https://img.shields.io/badge/python-3.12-blue)
![Pytest](https://img.shields.io/badge/tests-passing-brightgreen)
![Status](https://img.shields.io/badge/relatorio-gerado-success)

# ✅ EndCheck — Validador de Endpoints

O **EndCheck** é um projeto desenvolvido para validar automaticamente a disponibilidade e o comportamento de **endpoints de APIs**.  
Ele realiza chamadas HTTP, compara os **status esperados com os obtidos** e gera um **relatório em HTML** com os resultados.

---

## ⚙️ Funcionalidades

- Leitura de um arquivo `.json` com os endpoints
- Suporte aos métodos `GET`, `POST`, `PUT`, `DELETE` (simulado)
- Comparação entre código **esperado** e **obtido**
- Mensagens coloridas no terminal para facilitar a leitura
- Geração automática de **relatório visual em HTML**
- Testes automatizados com `pytest`

---

## 🧪 Exemplo de Estrutura do `endpoints.json`

```json
[
  {
    "nome": "Google",
    "metodo": "GET",
    "url": "https://www.google.com",
    "esperado": 200
  },
  {
    "nome": "Criar Post",
    "metodo": "POST",
    "url": "https://jsonplaceholder.typicode.com/posts",
    "esperado": 201
  },
  {
    "nome": "Atualizar Post",
    "metodo": "PUT",
    "url": "https://jsonplaceholder.typicode.com/posts/1",
    "esperado": 200
  }
]

