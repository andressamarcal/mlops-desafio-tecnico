import pandas as pd


def load_iris_data(file_path: str):
    """
    Carrega os dados do dataset Íris de um arquivo CSV.

    Args:
        file_path (str): Caminho para o arquivo CSV contendo o dataset Íris.

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados carregados.
    """
    return pd.read_csv(file_path)
