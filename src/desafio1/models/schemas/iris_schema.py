from typing import List, Optional

from pydantic import BaseModel


class Iris(BaseModel):
    """Schema para os dados de entrada do Iris.

    Attributes:
        sepal_length (float): Comprimento da sépala.
        sepal_width (float): Largura da sépala.
        petal_length (float): Comprimento da pétala.
        petal_width (float): Largura da pétala.
        species (str, optional): Espécie da flor. Pode ser uma de três possíveis: Iris-setosa, Iris-versicolor, Iris-virginica.
    """

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: Optional[str] = None  # Param opcional, pois pode não ser necessário para previsão


class IrisPredictionResponse(BaseModel):
    """Schema para a resposta da previsão.

    Attributes:
        prediction (List[int]): Lista de previsões de classe para cada instância de entrada.
        probability (List[List[float]]): Lista de probabilidades associadas a cada classe para cada instância de entrada.
        log_probability (List[List[float]]): Lista de log probabilidades associadas a cada classe para cada instância de entrada.
    """

    prediction: List[int]
    probability: List[List[float]]
    log_probability: List[List[float]]
