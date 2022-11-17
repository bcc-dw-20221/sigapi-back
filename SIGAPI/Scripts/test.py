import json
import requests as r

from datetime import datetime


BASE_URL = "http://localhost:8000"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NzAxNzcwLCJpYXQiOjE2Njg2OTgxNzAsImp0aSI6IjE4MjAyNGY1ZTc3MzRmOTFhNGZhZmE3NTVmNGZkYjkzIiwidXNlcl9pZCI6MX0.rw09PfUtKs7Q-tr4CYr8JcF4dNNndwnjSNiz757AzBQ"

# Vamos acessar um dos endpoints
resp = r.get(f"{BASE_URL}/sigapi/api/users/",headers={
            "Authorization": f"Bearer {token}",
        },)

print(resp.content.decode("utf-8")+"\n\n\n\n")

# Vamos inserir um novo item no endpoint

novo_user = {
    "username": "mar",
    "password": "123",
    "email": "mar@gmail.com"
}

resp = r.post(
        f"{BASE_URL}/sigapi/api/users/",
        data=novo_user,
        headers={
            "Authorization": f"Bearer {token}",
        },
)

print(resp.content.decode("utf-8"))

novo_aluno = {
        "user": "http://127.0.0.1:8000/sigapi/api/users/5/",
        "matricula": 1684184,
        "cpf": 149129712,
        "born": "2022-10-11",
        "endereco": "aracati",
        "nome_pai": "qrq",
        "nome_mae": "qwq",
        "sexo": "f",
        "telefone": "9985742",
        "estado_civil": "C",
        "rg": "987654321"
}

resp = r.post(
        f"{BASE_URL}/sigapi/api/aluno/",
        data=novo_aluno,
        headers={
            "Authorization": f"Bearer {token}",
        },
)

print(resp.content.decode("utf-8"))
