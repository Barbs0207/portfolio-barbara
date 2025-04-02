# conftest.py
import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"  # Simulando API pública (exemplo)

@pytest.fixture(scope="session")
def headers():
    return {"Content-Type": "application/json"}
