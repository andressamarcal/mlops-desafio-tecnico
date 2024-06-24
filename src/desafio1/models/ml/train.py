from typing import Tuple

from joblib import dump
from numpy import ndarray
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def load_data() -> Tuple[ndarray, ndarray]:
    """
    Carrega o dataset Íris e retorna os atributos e os alvos.

    Returns:
        Tuple[ndarray, ndarray]: Uma tupla contendo os atributos e os alvos do dataset.
    """
    return datasets.load_iris(return_X_y=True)


def create_pipeline() -> Pipeline:
    """
    Cria um pipeline de processamento com escalonamento MinMax e um classificador Gradient Boosting.

    Returns:
        Pipeline: Um pipeline do sklearn com pré-processamento e classificador.
    """
    clf_pipeline = [("scaling", MinMaxScaler()), ("clf", GradientBoostingClassifier())]
    return Pipeline(clf_pipeline)


def train_and_save_model(X: ndarray, y: ndarray, file_path: str) -> None:
    """
    Treina um modelo de classificação usando o pipeline definido e salva o modelo treinado.

    Args:
        X (ndarray): Atributos de treinamento.
        y (ndarray): Alvos de treinamento.
        file_path (str): Caminho para salvar o modelo treinado.
    """
    pipeline = create_pipeline()
    pipeline.fit(X, y)
    dump(pipeline, file_path)


if __name__ == "__main__":
    X, y = load_data()
    train_and_save_model(X, y, "./ml/iris_dt_v1.joblib")
