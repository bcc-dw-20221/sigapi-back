import json
import requests as r

from datetime import datetime


BASE_URL = "http://localhost:8000"

# Vamos solicitar nosso par de tokens
resp = r.post(f"{BASE_URL}/api/token/", {"username": "rond.nely", "password": "123"})

print(resp.content.decode("utf-8"))

# extraindo as tokens para uso nos próximos exemplos

tokens = json.loads(resp.content)

# Vamos verificar nossa token de acesso
resp = r.post(
    f"{BASE_URL}/api/token/verify/",
    {"token": f"{tokens['access']}"},
)

print(f"A verificação da token retornou: {resp}")

# Vamos acessar um dos endpoints
resp = r.get(f"{BASE_URL}/sigapi/api/users/")

print(resp.content.decode("utf-8"))

# Vamos inserir um novo item no endpoint


novo_aluno = {
        "user": "http://127.0.0.1:8000/sigapi/api/users/4/",
        "matricula": 12346789,
        "cpf": 123546789,
        "born": "2022-10-11",
        "endereco": "aracati",
        "nome_pai": "qrq",
        "nome_mae": "qwq",
        "sexo": "f",
        "telefone": "9985742",
        "estado_civil": "C",
        "rg": "123546879"
}

resp = r.post(
        f"{BASE_URL}/sigapi/api/aluno/",
        data=novo_aluno,
        headers={
            "Authorization": f"Bearer {tokens['access']}",
        },
)

print(resp.content.decode("utf-8"))
