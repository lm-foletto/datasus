# preprocess.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """Carrega os dados brutos a partir do arquivo"""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Trata os dados: lida com dados ausentes e codificação"""
    data = data.dropna()  # Para fins de exemplo, removemos linhas com valores ausentes
    # Codificação de variáveis categóricas, ajuste de escala, criação de features etc.
    return data

def split_data(data):
    """Divide os dados em treino e teste"""
    X = data.drop("internacoes", axis=1)  # Supondo que "internacoes" seja o target
    y = data["internacoes"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
