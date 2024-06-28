import pandas as pd
from pandas import DataFrame


def download_iris_dataset() -> DataFrame:
    """
    Baixa o dataset Íris do UCI Machine Learning Repository e retorna como um DataFrame do pandas.

    Returns:
        DataFrame: Um DataFrame contendo os dados do dataset Íris, com as colunas 'sepal_length',
                    'sepal_width', 'petal_length', 'petal_width' e 'species'.

    Exceções:
        ConexãoFalhaException: Lança uma exceção caso não seja possível baixar o dataset.
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species",
    ]
    try:
        data = pd.read_csv(url, names=column_names)
        return data
    except Exception as e:
        raise ConnectionError(f"Não foi possível baixar o dataset Íris: {e}")
