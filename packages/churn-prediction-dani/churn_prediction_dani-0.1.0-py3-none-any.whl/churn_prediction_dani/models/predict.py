import os
import sys
import pandas as pd
import joblib
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from config import MODEL_PATH, TEST_DATA_PATH, PREDICTIONS_PATH, PREDICTIONS_FILE

# Adicionar o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


def load_model(model_path=MODEL_PATH):
    """
    Carrega o modelo treinado do disco.

    Args:
        model_path (str): Caminho para o arquivo do modelo salvo.

    Returns:
        pipeline: Pipeline treinado.
    """
    try:
        model = joblib.load(model_path)
        print("Modelo carregado com sucesso.")
        return model
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Modelo não encontrado no caminho: {model_path}. Treine o modelo antes de realizar a predição."
        )


def calculate_metrics(y_true, y_pred, y_proba=None, output_path=PREDICTIONS_FILE):
    """
    Calcula métricas de avaliação (acurácia, F1, precisão, recall) e salva em um arquivo.

    Args:
        y_true (pd.Series): Valores reais.
        y_pred (pd.Series): Valores previstos.
        y_proba (pd.Series): Probabilidades previstas para a classe positiva (opcional).
        output_path (str): Caminho para salvar as métricas.

    Returns:
        dict: Dicionário com as métricas calculadas.
    """
    metrics = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "F1 Score": f1_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
    }

    # Calcula ROC AUC se as probabilidades forem fornecidas
    if y_proba is not None:
        try:
            metrics["ROC AUC"] = roc_auc_score(y_true, y_proba)
        except ValueError as e:
            metrics["ROC AUC"] = f"Erro ao calcular: {str(e)}"

    # Salva as métricas em um arquivo
    with open(output_path, "w") as f:
        for metric, value in metrics.items():
            if isinstance(value, str):  # Para erros ao calcular ROC AUC
                f.write(f"{metric}: {value}\n")
            else:
                f.write(f"{metric}: {value:.4f}\n")

    print(f"Métricas salvas em: {output_path}")
    return metrics


def make_predictions(data_path=TEST_DATA_PATH, threshold=0.5, target_column="Churn"):
    """
    Carrega os dados de teste, realiza o pré-processamento, faz as predições e salva os resultados.

    Args:
        data_path (str): Caminho para o arquivo de dados de teste.
        threshold (float): Limite de decisão para a classificação.
        target_column (str): Nome da coluna de destino (target).

    Returns:
        None
    """
    # Carrega o modelo treinado
    pipeline = load_model()

    # Carrega os dados de teste
    data = pd.read_csv(data_path)

    # Divide X e y (se 'Churn' estiver presente no conjunto de teste)
    x_test = data.drop(columns=[target_column], errors="ignore")
    y_true = data.get(target_column, None)  # Se houver

    # Obtém as probabilidades previstas para a classe positiva
    y_proba = pipeline.predict_proba(x_test)[:, 1]
    print("Probabilidades previstas calculadas com sucesso.")

    # Aplica o threshold para gerar as previsões finais
    y_pred = (y_proba >= threshold).astype(int)
    print(f"Predições realizadas com threshold = {threshold}.")

    # Salva as predições no DataFrame
    data["predicted_class"] = y_pred
    data["predicted_proba"] = y_proba  # Salva as probabilidades
    if y_true is not None:
        data["true_class"] = y_true

    # Salva os resultados em arquivo
    data.to_csv(PREDICTIONS_PATH, index=False)
    print(f"Resultados salvos em: {PREDICTIONS_PATH}")

    # Calcula métricas se y_true existir
    if y_true is not None:
        calculate_metrics(y_true=y_true, y_pred=y_pred, y_proba=y_proba)


if __name__ == "__main__":
    make_predictions()
