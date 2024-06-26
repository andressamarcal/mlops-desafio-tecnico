from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from sklearn.pipeline import Pipeline

app_iris_predict_v1 = APIRouter()


class IrisPredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class IrisPredictionResponse(BaseModel):
    prediction: str
    probability: float


def get_model(request: Request) -> Pipeline:
    """
    Obtém o modelo treinado do estado da aplicação.

    Args:
        request (Request): A requisição atual.

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
async def get_prediction(request: IrisPredictionRequest, req: Request):
    """
    Endpoint para obter previsões das espécies de flores Íris a partir das características da flor.

    Args:
        request (IrisPredictionRequest): Objeto contendo características de uma flor Íris.
        req (Request): A requisição atual para obter o modelo treinado.

    Returns:
        IrisPredictionResponse: Um objeto contendo a previsão e a probabilidade.
    """
    model = get_model(req)
    class_names = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    try:
        data = [[request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]]
        class_index = model.predict(data)[0]
        class_name = class_names[class_index]
        probability = max(model.predict_proba(data)[0])
        return IrisPredictionResponse(prediction=class_name, probability=probability)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Erro de valor: {e}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro do servidor: {e}") from e
