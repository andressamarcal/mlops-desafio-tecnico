import joblib
from desafio1.app.models import IrisModel
from sklearn.ensemble import RandomForestClassifier


def load_model():
    model = joblib.load("model/iris_model.pkl")
    return model


def predict_iris(iris: IrisModel, model: RandomForestClassifier):
    data = [[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]]
    pred = model.predict(data)
    prob = model.predict_proba(data)
    return pred, prob
