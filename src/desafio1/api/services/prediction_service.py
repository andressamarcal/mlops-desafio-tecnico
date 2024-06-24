import joblib

model = joblib.load("path/to/your/model.pkl")


def make_prediction(iris_data):
    """
    Realiza uma previsão usando o modelo de machine learning carregado.

    Args:
        iris_data (IrisModel): Dados da flor Íris para a qual a previsão deve ser feita.

    Returns:
        dict: Um dicionário contendo as previsões e probabilidades.
    """
    data = [[iris_data.sepal_length, iris_data.sepal_width, iris_data.petal_length, iris_data.petal_width]]
    prediction = model.predict(data)
    probability = model.predict_proba(data)
    return {"prediction": prediction.tolist(), "probability": probability.tolist()}
