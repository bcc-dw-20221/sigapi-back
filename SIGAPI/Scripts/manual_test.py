import json
import requests as r

from datetime import datetime


BASE_URL = "http://localhost:8000"

# Vamos solicitar nosso par de tokens
resp = r.post(f"{BASE_URL}/api/token/", {"username": "felipe", "password": "123456"})

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
resp = r.get(f"{BASE_URL}/boteco/api/perfis/")

print(resp.content.decode("utf-8"))

# Vamos inserir um novo item no endpoint
# Atenção: nas libs do JS e TS a gente usa o formato JSON normal.
#          Aqui no requests, precisei adaptar pro padrão user.atributo.

files = {}
with open("chifre.jpg", "rb") as profile_pic:
    files = {
        "foto_perfil": profile_pic,
    }
    novo_corno = {
        "user.username": "jao2",
        "user.password": "jao1234!",
        "user.email": "jao@cornos.com",
        "user.first_name": "João",
        "user.last_name": "dos Chifres Tortos",
        "foto_perfil": "chifre.jpg",
        "qtd_chifres": 10,
        "ultimo_chifre": datetime.now(),
        "procurando_mais": "true",
    }

    resp = r.post(
        f"{BASE_URL}/boteco/api/perfis/",
        data=novo_corno,
        files=files,
        headers={
            "Authorization": f"Bearer {tokens['access']}",
        },
    )

    print(resp.content.decode("utf-8"))