![Python](https://img.shields.io/badge/python-3.12-blue)
![Pytest](https://img.shields.io/badge/tests-passing-brightgreen)

# Simulador de Custo de Seguro Cafezal ☕🌱

Este projeto foi desenvolvido com o objetivo de automatizar e validar os cálculos utilizados em uma planilha de simulação de seguro rural (seguro de cafezal). Ele replica, por código, a lógica de cálculo que normalmente é feita manualmente, permitindo agilidade, clareza e validação automática de resultados.

---

## 💻 Funcionalidades

- Cálculo automatizado do prêmio total com base em:
  - Cobertura básica
  - Produção futura
  - Tratamento fitossanitário
- Aplicação correta de subvenções:
  - Subvenção estadual (30% até R$ 25.000)
  - Subvenção federal (40% até R$ 60.000)
- Cálculo do investimento final do produtor
- Parcelamento do investimento em 5 vezes
- Testes automatizados com `pytest` cobrindo:
  - Cálculo do prêmio total
  - Subvenções com limites
  - Investimento e valor de parcelas

---

## 🧪 Testes Automatizados

Os testes estão localizados no arquivo `test_simulador.py`.

Para executá-los:

```bash
python -m pytest test_simulador.py

📊 Dados Utilizados

 Os valores simulados são referentes ao município de Cássia - MG, com uma área de 10 hectares.
🚀 Tecnologias

    Python 3.12

    Pytest

    Lógica matemática aplicada à área agrícola