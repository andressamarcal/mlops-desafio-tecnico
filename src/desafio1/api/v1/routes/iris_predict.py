import models.ml.classifier as clf
from fastapi import APIRouter, HTTPException
from models.schemas.iris import Iris, IrisPredictionResponse

app_iris_predict_v1 = APIRouter()


@app_iris_predict_v1.post(
    "/iris/predict",
    tags=["Predictions"],
    response_model=IrisPredictionResponse,
    description="Get a classification from Iris dataset based on sepal and petal dimensions.",
)
async def get_prediction(iris: Iris) -> IrisPredictionResponse:
    """
    Endpoint para obter previsões das espécies de flores Íris a partir das características da flor.

    Args:
        iris (Iris): Um objeto contendo características de uma flor Íris (comprimento e largura das sépalas e pétalas).

    Returns:
        IrisPredictionResponse: Um objeto contendo as previsões de classe, probabilidades e log probabilidades.

    Raises:
        HTTPException: Lança exceção HTTP 422 se houver problema na previsão devido a dados de entrada inválidos.
    """
    try:
        data = [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
        prediction = clf.model.predict(data).tolist()
        probability = clf.model.predict_proba(data).tolist()
        log_probability = clf.model.predict_log_proba(data).tolist()
        return IrisPredictionResponse(prediction=prediction, probability=probability, log_probability=log_probability)
    except Exception as e:
        # TODO: exceçao genérica para evitar que a aplicação quebre. o ideal seria ser mais especifica possivel na excepcion :)
        raise HTTPException(status_code=422, detail=f"Error in prediction: {e!s}")
