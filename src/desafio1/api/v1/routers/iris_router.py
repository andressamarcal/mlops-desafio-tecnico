from enum import Enum
from typing import Dict

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from sklearn.pipeline import Pipeline

app_iris_predict_v1 = APIRouter()


class IrisClassNames(str, Enum):
    """Enum para mapear classes numéricas para nomes de espécies de Íris."""

    setosa = "Iris-setosa"
    versicolor = "Iris-versicolor"
    virginica = "Iris-virginica"


class IrisPredictionRequest(BaseModel):
    """Modelo para a requisição de predição de Íris.

    Attributes:
        sepal_length (float): Comprimento da sépala.
        sepal_width (float): Largura da sépala.
        petal_length (float): Comprimento da pétala.
        petal_width (float): Largura da pétala.
    """

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class IrisPredictionResponse(BaseModel):
    """Modelo para a resposta da predição de Íris.

    Attributes:
        prediction (int): Classe predita como número.
        class_name (str): Nome da classe predita.
        probability (float): Probabilidade associada à predição.
    """

    prediction: int
    class_name: str
    probability: float


def get_model(request: Request) -> Pipeline:
    """Obtém o modelo treinado a partir do estado da aplicação.

    Args:
        request (Request): Requisição atual.

    Returns:
        Pipeline: O modelo treinado.
    """
    return request.app.state.model


@app_iris_predict_v1.post(
    "/iris/predict",
    tags=["Predictions"],
    response_model=IrisPredictionResponse,
    description="Obtenha uma classificação para flores de Íris",
)
async def get_prediction(
    request: IrisPredictionRequest, req: Request
) -> IrisPredictionResponse:
    """Endpoint para obter previsões das espécies de flores Íris a partir das características da flor.

    Args:
        request (IrisPredictionRequest): Objeto contendo características de uma flor Íris.
        req (Request): A requisição atual para obter o modelo treinado.

    Returns:
        IrisPredictionResponse: Um objeto contendo a previsão, o nome da classe e a probabilidade.
    """
    model = get_model(req)
    class_mapping: Dict[int, str] = {
        0: IrisClassNames.setosa.value,
        1: IrisClassNames.versicolor.value,
        2: IrisClassNames.virginica.value,
    }

    try:
        data = [
            [
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
        prediction = model.predict(data)[0]
        class_name = class_mapping[prediction]
        probability = max(model.predict_proba(data)[0])
        return IrisPredictionResponse(
            prediction=prediction, class_name=class_name, probability=probability
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Erro de valor: {e}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro do servidor: {e}") from e
