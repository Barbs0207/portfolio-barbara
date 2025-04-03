import pytest
from validador import executar_endpoint 

# 🔁 Endpoints de teste direto no código (não usa o JSON principal)
casos_teste = [
    {
        "nome": "GET Google",
        "url": "https://www.google.com",
        "metodo": "GET",
        "esperado": 200
    },
    {
        "nome": "POST jsonplaceholder",
        "url": "https://jsonplaceholder.typicode.com/posts",
        "metodo": "POST",
        "esperado": 201,
        "payload": {
            "title": "Teste Pytest",
            "body": "Esse é um post de teste com pytest",
            "userId": 42
        }
    }
]

# 🧠 Esse decorador é essencial!
@pytest.mark.parametrize("endpoint", casos_teste)
def test_endpoint(endpoint):
    resultado = executar_endpoint(endpoint)
    assert resultado["obtido"] == endpoint["esperado"], f"{endpoint['nome']} falhou"
