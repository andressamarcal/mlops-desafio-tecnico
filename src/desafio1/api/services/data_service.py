import pandas as pd
from sklearn import datasets


def download_iris_dataset() -> pd.DataFrame:
    """
    Faz o download do dataset Íris e retorna um DataFrame do pandas.

    Returns:
        pd.DataFrame: DataFrame contendo o dataset Íris.
    """
    iris = datasets.load_iris(as_frame=True)
    return iris.frame
