from typing import List

import numpy as np
from sklearn.pipeline import Pipeline


def predict(model: Pipeline, features: List[float]) -> int:
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)[0]
    return prediction


def predict_proba(model: Pipeline, features: List[float]) -> List[float]:
    data = np.array(features).reshape(1, -1)
    probabilities = model.predict_proba(data)[0]
    return probabilities.tolist()
