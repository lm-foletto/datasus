# api/main.py

from fastapi import FastAPI
import joblib
import pandas as pd
from data.download_data import main as update_data  # Importa o script de atualização

app = FastAPI()

# Carregar o modelo treinado
model = joblib.load("model/model.joblib")

@app.get("/predict")
def predict(data: dict):
    # Lógica de pré-processamento e previsão
    data_df = pd.DataFrame([data])
    prediction = model.predict(data_df)
    return {"prediction": prediction[0]}

@app.get("/update-data")
def update():
    update_data()  # Executa a função de download e atualização de dados
    return {"status": "Data updated"}
