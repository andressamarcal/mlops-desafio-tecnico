from api.v1.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_iris_prediction():
    """
    Testa o endpoint de previsão do Íris para garantir que ele retorna o status correto e o formato dos dados.
    """
    response = client.post(
        "/iris/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "probability" in response.json()
