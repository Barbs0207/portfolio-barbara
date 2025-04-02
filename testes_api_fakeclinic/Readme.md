# 🏥 API Tests: FakeClinic

Este repositório contém um conjunto de testes automatizados para a API FakeClinic, criada para fins educativos e de portfólio.

## 📁 Estrutura
```
portfolio/
└── api-tests-fakeclinic/
    ├── conftest.py          # Configurações globais e fixtures
    ├── test_patients.py     # Testes da rota /users (pacientes)
    └── requirements.txt    # Dependências do projeto
```

## ✅ Tecnologias
- **Python 3.12**
- **Pytest** para execução dos testes
- **Requests** para chamadas HTTP

## 🧪 Casos de Teste

Arquivo `test_patients.py` testa:
- Listagem de pacientes
- Detalhe de um paciente por ID
- Criação de novo paciente

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Navegue até a pasta do projeto:
```bash
cd portfolio/api-tests-fakeclinic
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute os testes:
```bash
pytest
```

## 💡 Observações
- Esta é uma API fake, simulada para fins didáticos.
- Os dados de exemplo são fictícios.

---

Feito com carinho por [Bárbara Filadelfo](https://github.com/seu-usuario) 💕
