# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model/model.joblib")  # Carrega o modelo previamente treinado

class InputData(BaseModel):
    # Defina os campos de entrada com base nos dados de entrada do modelo
    variavel_1: float
    variavel_2: float
    variavel_n: float

@app.post("/predict")
async def predict(data: InputData):
    try:
        df = pd.DataFrame([data.dict()])  # Converte os dados de entrada em DataFrame
        prediction = model.predict(df)[0]
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Adiciona as bibliotecas de monitoramento
from prometheus_client import Counter, Histogram, start_http_server
import time

# Inicia o servidor de métricas
start_http_server(8001)

# Métricas de monitoramento
REQUEST_COUNT = Counter('request_count', 'Contagem de requisições para previsões')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Latência das requisições para previsões')

@app.post("/predict")
async def predict(data: InputData):
    REQUEST_COUNT.inc()  # Incrementa a contagem de requisições
    start_time = time.time()  # Tempo inicial para latência

    try:
        df = pd.DataFrame([data.dict()])
        prediction = model.predict(df)[0]
        REQUEST_LATENCY.observe(time.time() - start_time)  # Registra a latência
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
