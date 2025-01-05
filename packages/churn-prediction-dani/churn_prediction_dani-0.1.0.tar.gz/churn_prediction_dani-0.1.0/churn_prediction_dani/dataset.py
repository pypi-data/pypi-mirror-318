import pandas as pd
from sklearn.model_selection import train_test_split
from config import RAW_DATA_PATH, TRAIN_DATA_PATH, TEST_DATA_PATH


def load_data(filepath=RAW_DATA_PATH, target_column="Churn"):
    """
    Carrega os dados a partir de um arquivo Excel.

    Args:
        filepath (str): Caminho para o arquivo de dados.
        target_column (str): Nome da coluna de destino.

    Returns:
        pd.DataFrame: DataFrame contendo os dados carregados.
    """
    df = pd.read_excel(filepath)
    df[target_column] = df[target_column].map({"Sim": 1, "Não": 0})
    return df


def prepare_data(df, target_column="Churn"):
    """
    Divide os dados em treino e teste.

    Args:
        df (pd.DataFrame): DataFrame com os dados.
        target_column (str): Nome da coluna de destino.

    Returns:
        tuple: Dados de treino e teste (x_train, x_test, y_train, y_test).
    """
    df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
    x_train = df_train.drop(target_column, axis=1)
    y_train = df_train[target_column]
    x_test = df_test.drop(target_column, axis=1)
    y_test = df_test[target_column]
    return x_train, x_test, y_train, y_test


def split_df(df, test_size=0.2, random_state=42):
    """
    Divide os dados em treino e teste.

    Args:
        df (pd.DataFrame): DataFrame com os dados.
        test_size (float): Proporção de dados de teste.
        random_state (int): Semente para reprodutibilidade.

    Returns:
        tuple: DataFrames de treino e teste.
    """
    return train_test_split(df, test_size=test_size, random_state=random_state)


def split_df(df, test_size=0.2, random_state=42):
    """
    Divide os dados em treino e teste.

    Args:
        df (pd.DataFrame): DataFrame com os dados.
        test_size (float): Proporção de dados de teste.
        random_state (int): Semente para reprodutibilidade.

    Returns:
        tuple: DataFrames de treino e teste.
    """
    return train_test_split(df, test_size=test_size, random_state=random_state)


def save_splits(
    df_train, df_test, train_path=TRAIN_DATA_PATH, test_path=TEST_DATA_PATH
):
    """
    Salva os splits de treino e teste em arquivos CSV.

    Args:
        df_train (pd.DataFrame): Dados de treino.
        df_test (pd.DataFrame): Dados de teste.
        train_path (str): Caminho para salvar os dados de treino.
        test_path (str): Caminho para salvar os dados de teste.
    """
    df_train.to_csv(train_path, index=False)
    df_test.to_csv(test_path, index=False)


def main():
    """
    Função principal que executa o fluxo de carregamento, divisão e salvamento dos dados.
    """
    df = load_data()

    df_train, df_test = split_df(df)

    save_splits(df_train, df_test)
    print(f"Dados divididos:\nTreino: {TRAIN_DATA_PATH}\nTeste: {TEST_DATA_PATH}")


if __name__ == "__main__":
    main()
