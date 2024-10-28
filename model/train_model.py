# train_model.py
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from preprocess import preprocess_data, split_data
from data.download_data import main as update_data  # Importa o script de download e atualização de dados

def load_data(path="data/dados_internacoes.csv"):
    """Carrega os dados de internações atualizados"""
    import pandas as pd
    return pd.read_csv(path)

def train_model(X_train, y_train):
    """Treina o modelo e o retorna"""
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo e imprime as métricas"""
    predictions = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("RMSE:", mean_squared_error(y_test, predictions, squared=False))
    print("R²:", r2_score(y_test, predictions))

def save_model(model, path="model/model.joblib"):
    """Salva o modelo treinado"""
    joblib.dump(model, path)

if __name__ == "__main__":
    # Atualiza os dados de internações do DataSUS
    update_data()

    # Pipeline completo de treinamento
    data = load_data("data/dados_internacoes.csv")  # Carrega dados atualizados
    data = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(data)
    
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model)