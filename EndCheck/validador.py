import requests

def executar_endpoint(endpoint):
    nome = endpoint.get("nome", "Sem nome")
    url = endpoint.get("url")
    metodo = endpoint.get("metodo", "GET").upper()
    esperado = endpoint.get("esperado", 200)
    payload = endpoint.get("payload", {})

    try:
        resposta = requests.request(metodo, url, json=payload)
        status_obtido = resposta.status_code
        sucesso = status_obtido == esperado

        resultado = {
            "nome": nome,
            "sucesso": sucesso,
            "mensagem": f"Status {status_obtido}, esperado {esperado}",
            "obtido": status_obtido,
            "esperado": esperado,
            "comparacao": f"{status_obtido} → {esperado}",
            "verificacao_extra": None
        }

        # Tentativa de extração do ID, se houver
        id_gerado = None
        try:
            resposta_json = resposta.json()
            if isinstance(resposta_json, dict):
                id_gerado = resposta_json.get("id")
        except Exception:
            pass  # ignora erro ao tentar ler JSON

        # Verificação extra, se existir
        if "verificacao_extra" in endpoint:
            extra = endpoint["verificacao_extra"]
            extra_url = extra.get("url")
            extra_metodo = extra.get("tipo", "GET").upper()
            extra_esperado = extra.get("esperado", 200)

            # Substituir {{id}} na URL da verificação
            if id_gerado is not None and "{{id}}" in extra_url:
                extra_url = extra_url.replace("{{id}}", str(id_gerado))

            try:
                extra_resposta = requests.request(extra_metodo, extra_url)
                extra_status = extra_resposta.status_code

                if extra_status == extra_esperado:
                    resultado["verificacao_extra"] = f"✅ {extra_status} = {extra_esperado}"
                else:
                    resultado["verificacao_extra"] = f"❌ {extra_status} ≠ {extra_esperado}"

            except Exception as e:
                resultado["verificacao_extra"] = f"❌ Erro: {str(e)}"

        return resultado

    except Exception as e:
        return {
            "nome": nome,
            "sucesso": False,
            "mensagem": f"Erro: {str(e)}",
            "obtido": None,
            "esperado": esperado,
            "comparacao": "--- → " + str(esperado),
            "verificacao_extra": "❌ Erro na requisição"
        }
