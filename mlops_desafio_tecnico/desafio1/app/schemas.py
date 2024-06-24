from typing import List

from pydantic import BaseModel


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
