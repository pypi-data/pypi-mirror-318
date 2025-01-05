"""
Este módulo realiza experimentos de machine learning para previsão de churn,
incluindo o uso de validação cruzada, registro de métricas e parâmetros no MLflow.
"""

import mlflow
from sklearn.model_selection import KFold, cross_val_score
from imblearn.ensemble import BalancedRandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from features import pipeline, TargetMapper
from dataset import load_data, prepare_data

df = load_data()
X_train, X_test, y_train, y_test = prepare_data(df)

print(y_test.value_counts())
print("Arquivo carregado com sucesso")

# Definição dos modelos
BRC = BalancedRandomForestClassifier(random_state=1234)
XGB = XGBClassifier(scale_pos_weight=19, random_state=1234, objective="binary:logistic")
LGB = LGBMClassifier(class_weight="balanced", random_state=1234)

models = [BRC, LGB, XGB]
model_names = ["Balanced RF", "Light GBM", "XGBoost"]

results = []

# Configuração do MLflow
mlflow.set_tracking_uri("")  # Deixe vazio para usar o padrão
mlflow.set_experiment("Churn Prediction Experiment")  # Nome do experimento

# Loop para treinar e registrar os modelos no MLflow
for model, name in zip(models, model_names):

    print(f"Treinando o modelo {name}")
    # Cria o pipeline com o modelo atual
    pipe = pipeline(model)
    kfold = KFold(n_splits=5, random_state=42, shuffle=True)

    # Inicia um run do MLflow para cada modelo
    with mlflow.start_run(run_name=name):
        # Cross-validation
        try:
            cv_results = cross_val_score(
                pipe, X_train, y_train, cv=5, scoring="roc_auc"
            )
            print("Calculou com sucesso")
            print(f"AUC Média: {cv_results.mean()}, Desvio Padrão: {cv_results.std()}")
        except Exception as e:
            print(f"Erro durante a execução: {e}")
        mean_auc = cv_results.mean()
        std_auc = cv_results.std()

        # Log de parâmetros do modelo
        mlflow.log_param("model_name", name)
        if hasattr(model, "n_estimators"):
            mlflow.log_param("n_estimators", model.n_estimators)
        if hasattr(model, "max_depth"):
            mlflow.log_param("max_depth", model.max_depth)

        # Log de métricas
        mlflow.log_metric("mean_auc", mean_auc)
        mlflow.log_metric("std_auc", std_auc)

        # Log do modelo
        mlflow.sklearn.log_model(pipe, "model")

        # Adiciona os resultados ao array de resultados para visualização posterior
        results.append(cv_results)
        print(f"{name}: AUC = {mean_auc:.3f} (+/- {std_auc:.3f})")
