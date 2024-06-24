import pandas as pd
from api.services.data_service import load_iris_data
from pandas.testing import assert_frame_equal


def test_load_iris_data():
    """
    Testa se a função load_iris_data carrega corretamente os dados do dataset Íris.
    """
    # Caminho simulado para um arquivo CSV de teste
    test_csv_path = "desafio1/data/iris_test.csv"
    # Criando um DataFrame de teste para comparar com o carregado pela função
    expected_data = pd.DataFrame(
        {
            "sepal_length": [5.1, 4.9, 4.7],
            "sepal_width": [3.5, 3.0, 3.2],
            "petal_length": [1.4, 1.4, 1.3],
            "petal_width": [0.2, 0.2, 0.2],
            "species": ["setosa", "setosa", "setosa"],
        }
    )

    loaded_data = load_iris_data(test_csv_path)

    assert_frame_equal(loaded_data, expected_data)
