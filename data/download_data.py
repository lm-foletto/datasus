# data/download_data.py

import requests
import pandas as pd

# Autenticação na API do DataSUS
auth_url = "https://auth.datasus.gov.br/oauth/token"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
grant_type = "client_credentials"

auth_response = requests.post(auth_url, data={
    'grant_type': grant_type,
    'client_id': client_id,
    'client_secret': client_secret
})

if auth_response.status_code == 200:
    access_token = auth_response.json().get("access_token")
    headers = {"Authorization": f"Bearer {access_token}"}
else:
    raise Exception("Erro ao obter token de autenticação")

# Requisição de dados de internações
base_url = "https://api.datasus.saude.gov.br/dataset/internacoes"
params = {
    "dataInicio": "2023-01-01",
    "dataFim": "2023-12-31",
    "estado": "SP"
}
response = requests.get(base_url, headers=headers, params=params)

if response.status_code == 200:
    internacoes_data = response.json()
    internacoes_df = pd.DataFrame(internacoes_data)
    internacoes_df.to_csv("dados_internacoes.csv", index=False)
else:
    raise Exception("Erro ao buscar dados de internações")
