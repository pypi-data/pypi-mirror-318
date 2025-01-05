"""
Este módulo contém classes e funções para manipulação de dados e engenharia de
features, incluindo pipelines de transformação.
"""

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder


class ColumnRenamer(BaseEstimator, TransformerMixin):
    """
    Classe para renomear colunas e mapear valores de colunas específicas.
    """

    def __init__(self):
        self.renamed_columns = {
            "Frequência de utilização de feature do sistema: Módulo financeiro": "Módulo Financeiro",
            "Frequência de utilização de feature do sistema: Emissão de nota fiscal": "Emissão NF",
            "Frequência de utilização de feature do sistema: Integração bancária": "Integração Bancária",
            "Frequência de utilização de feature do sistema: Módulo de vendas": "Módulo de Vendas",
            "Frequência de utilização de feature do sistema: Relatórios": "Relatórios",
            "Frequência de utilização de feature do sistema: Utilização de APIs de integração": "APIs de Integração",
        }

    def fit(self, X, y=None):
        return self  # Nenhum ajuste necessário

    def transform(self, X):
        X = X.copy()

        # Renomear as colunas
        X.rename(columns=self.renamed_columns, inplace=True)

        return X


class ColumnDropper(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(
            columns=[
                "ID",
                "Emite boletos",
                "Tipo de empresa",
                "Utiliza serviços financeiros",
            ],
            axis=1,
        )


class DataProcessor(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()

        # Cria a coluna 'is_missing' com 1 para valores ausentes e 0 para valores não ausentes
        X_copy["is_missing"] = X_copy["PossuiContador"].isnull().astype(int)

        # Preenche os valores nulos com 0
        X_copy["PossuiContador"] = X_copy["PossuiContador"].fillna("Não")
        X_copy["PossuiContador"] = X_copy["PossuiContador"].apply(
            lambda x: 1 if x == "Sim" else 0
        )

        return X_copy


class MedianImputer(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.imputers = {}

    def fit(self, X, y=None):
        cols = [
            "Fundação da empresa",
            "Receita mensal",
            "Receita total",
            "Meses de permanência ",
        ]
        for col in cols:
            imputer = SimpleImputer(strategy="median")
            imputer.fit(X[[col]])
            self.imputers[col] = imputer
        return self

    def transform(self, X):
        X_copy = X.copy()
        for col, imputer in self.imputers.items():
            X_copy[col] = imputer.transform(X_copy[[col]])
        return X_copy


class TargetFeatureEncoder(BaseEstimator, TransformerMixin):

    def __init__(self, cols=None):
        self.cols = cols
        self.encoder = OrdinalEncoder(
            handle_unknown="use_encoded_value", unknown_value=-1
        )

    def fit(self, X, y=None):
        # Filtra as colunas existentes no DataFrame
        self.cols = [col for col in self.cols if col in X.columns]
        self.encoder.fit(X[self.cols])
        return self

    def transform(self, X):
        X = X.copy()
        valid_cols = [col for col in self.cols if col in X.columns]
        X[valid_cols] = self.encoder.transform(X[valid_cols])
        return X


def pipeline(model):

    # Criando o pipeline
    pipe = Pipeline(
        [
            ("renamer", ColumnRenamer()),
            ("dropper", ColumnDropper()),
            ("processor", DataProcessor()),
            ("imputer", MedianImputer()),
            (
                "target_encoder",
                TargetFeatureEncoder(
                    cols=[
                        "Possui mais de um sócio",
                        "Funcionários",
                        "PossuiContador",
                        "Faz conciliação bancária",
                        "Módulo Financeiro",
                        "Emissão NF",
                        "Integração Bancária",
                        "Módulo de Vendas",
                        "Relatórios",
                        "APIs de Integração",
                        "Contrato",
                        "Emite boletos.1",
                        "Tipo de pagamento",
                    ]
                ),
            ),
            ("classifier", model),
        ]
    )
    return pipe
