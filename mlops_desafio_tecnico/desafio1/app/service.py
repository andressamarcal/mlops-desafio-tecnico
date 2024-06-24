from typing import List, Tuple

import joblib
from desafio1.app.models import IrisModel
from sklearn.ensemble import RandomForestClassifier


def load_model() -> RandomForestClassifier:
    """
    Carrega o modelo de machine learning treinado a partir de um arquivo pickle.

    Returns:
        RandomForestClassifier: Modelo de classificação RandomForest carregado.
    """
    model = joblib.load("model/iris_model.pkl")
    return model


def predict_iris(iris: IrisModel, model: RandomForestClassifier) -> Tuple[List[int], List[List[float]]]:
    """
    Realiza a previsão de espécie de íris com base nas medidas fornecidas usando o modelo fornecido.

    Args:
        iris (IrisModel): Objeto IrisModel contendo as características de uma flor de íris.
        model (RandomForestClassifier): O modelo de RandomForest para fazer a previsão.

    Returns:
        Tuple[List[int], List[List[float]]]: Tuple contendo:
            - A classe prevista (como uma lista de inteiros).
            - As probabilidades associadas a cada classe (como uma lista de listas de floats).
    """
    data = [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
    pred = model.predict(data)
    prob = model.predict_proba(data)
    return pred, prob
