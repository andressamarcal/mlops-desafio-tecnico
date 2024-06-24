from typing import List

from pydantic import BaseModel


class IrisPredictionResponse(BaseModel):
    """Schema para a resposta da previ

    Attributes:
        prediction (List[int]): Lista
        probability (List[List[float]]
        log_probability (List[List[flo
    """

    prediction: List[int]
    probability: List[List[float]]
    log_probability: List[List[float]]
