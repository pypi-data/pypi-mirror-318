import pytest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from features import (
    ColumnRenamer,
    ColumnDropper,
    DataProcessor,
    MedianImputer,
    TargetFeatureEncoder,
    pipeline,
)


# Fixture com dados fictícios
@pytest.fixture
def sample_data():
    return pd.DataFrame(
        {
            "ID": [1, 2],
            "Frequência de utilização de feature do sistema: Módulo financeiro": [
                "Alta",
                "Baixa",
            ],
            "PossuiContador": [None, "Sim"],
            "Fundação da empresa": [2015, None],
            "Receita mensal": [10000, None],
            "Receita total": [None, 500000],
            "Meses de permanência ": [24, None],
            "Emite boletos": ["Sim", "Não"],
            "Tipo de empresa": ["MEI", "LTDA"],
            "Utiliza serviços financeiros": ["Sim", "Não"],
        }
    )


@pytest.fixture
def target():
    return pd.Series([0, 1])


def test_column_renamer(sample_data):
    renamer = ColumnRenamer()
    data = renamer.fit_transform(sample_data)
    assert "Módulo Financeiro" in data.columns
    assert (
        "Frequência de utilização de feature do sistema: Módulo financeiro"
        not in data.columns
    )


def test_column_dropper(sample_data):
    """Testa se o ColumnDropper remove as colunas especificadas."""
    dropper = ColumnDropper()
    transformed_data = dropper.fit_transform(sample_data)
    assert "ID" not in transformed_data.columns
    assert "Emite boletos" not in transformed_data.columns


def test_data_processor(sample_data):
    """Testa se o DataProcessor cria a coluna `is_missing` e transforma `PossuiContador` corretamente."""
    processor = DataProcessor()
    transformed_data = processor.fit_transform(sample_data)
    assert "is_missing" in transformed_data.columns
    assert (
        transformed_data["PossuiContador"].iloc[0] == 0
    )  # Verifica se foi preenchido corretamente
    assert transformed_data["PossuiContador"].iloc[1] == 1


def test_median_imputer(sample_data):
    """Testa se o MedianImputer preenche os valores ausentes corretamente."""
    imputer = MedianImputer()
    transformed_data = imputer.fit_transform(sample_data)
    assert (
        not transformed_data[
            [
                "Fundação da empresa",
                "Receita mensal",
                "Receita total",
                "Meses de permanência ",
            ]
        ]
        .isnull()
        .any()
        .any()
    )


def test_target_feature_encoder(sample_data):
    """Testa se o TargetFeatureEncoder codifica corretamente as colunas categóricas."""
    encoder = TargetFeatureEncoder(cols=["PossuiContador"])
    transformed_data = encoder.fit_transform(sample_data)
    assert all(isinstance(x, (int, float)) for x in transformed_data["PossuiContador"])


def test_pipeline(sample_data, target):
    """Testa o pipeline completo com um modelo fictício."""
    model = RandomForestClassifier()
    pipe = pipeline(model)
    pipe.fit(sample_data, target)
    predictions = pipe.predict(sample_data)
    assert len(predictions) == len(
        target
    )  # Verifica se a saída tem o mesmo tamanho que o alvo
