from typing import Optional

from pydantic import BaseModel


class IrisModel(BaseModel):
    """Schema para os dados de entrada do Iris.

    Attributes:
        sepal_length (float): Comprimento da sépala.
        sepal_width (float): Largura da sépala.
        petal_length (float): Comprimento da pétala.
        petal_width (float): Largura da pétala.
        species (str, optional): Espécie da flor. Pode ser uma de três possíveis: Iris-setosa,
    """

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: Optional[str] = None  # Param opcional, pois pode não ser necessário para previsão
