# tests/test_patients.py
import requests

def test_get_all_patients(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_patient(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and data["id"] == 1

def test_create_new_patient(base_url, headers):
    payload = {
        "name": "Bárbara QA",
        "email": "barbara@example.com",
        "phone": "+55 21 99999-9999"
    }
    response = requests.post(f"{base_url}/users", headers=headers, json=payload)
    assert response.status_code in (200, 201)
    data = response.json()
    assert data["name"] == payload["name"]

def test_update_patient(base_url, headers):
    update_data = {
        "name": "Bárbara QA Atualizada"
    }
    response = requests.put(f"{base_url}/users/1", headers=headers, json=update_data)
    assert response.status_code in (200, 204)

def test_delete_patient(base_url, headers):
    response = requests.delete(f"{base_url}/users/1", headers=headers)
    assert response.status_code in (200, 204)
