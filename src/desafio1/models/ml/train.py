from typing import Tuple

from joblib import dump
from numpy import ndarray
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


def load_data() -> Tuple[ndarray, ndarray]:
    """
    Carrega o dataset Íris e retorna os atributos e os alvos.

    Returns:
        Tuple[ndarray, ndarray]: Uma tupla contendo os atributos e os alvos do dataset.
    """
    return datasets.load_iris(return_X_y=True)


def create_model() -> RandomForestClassifier:
    """
    Cria um modelo Random Forest Classifier.

    Returns:
        RandomForestClassifier: Um modelo Random Forest configurado.
    """
    return RandomForestClassifier(n_estimators=100, random_state=42)


def train_and_save_model(X: ndarray, y: ndarray, file_path: str) -> None:
    """
    Treina um modelo de classificação Random Forest e salva o modelo treinado.

    Args:
        X (ndarray): Atributos de treinamento.
        y (ndarray): Alvos de treinamento.
        file_path (str): Caminho para salvar o modelo treinado.
    """
    model = create_model()
    model.fit(X, y)
    dump(model, file_path)


if __name__ == "__main__":
    X, y = load_data()
    train_and_save_model(X, y, "./ml/iris_rf_v1.joblib")
