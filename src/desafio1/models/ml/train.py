from typing import Tuple

from joblib import dump
from numpy import ndarray
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

"""
Explicando o por quê da escolha da Regressão Logística para o projeto:
1. Algoritmo extremamente otimizado e simples para explicação(interpratabilidade do modelo), ou seja, bem menos caixa preta.
2. Novamente, tem uma tnterpretação bem simples. Seus coeficientes da regressão logística são interpretáveis e oferecem insights diretos sobre a importância das features(feature importance).
3. Bem rápida e, novamente, extremante eficiente (principalmente em cenários de score de crédito =D)
4. Treinamento e previsão rápidos, mesmo com grandes conjuntos de dados.
5. Algoritmo bom para dados lineares, ou seja, funciona bem quando há uma relação linear entre as features e a variável alvo/target. :)
O unico ponto que ressalto, é o fato dele nem sempreo capturar complexidade, acaba sendo menos eficaz em capturar relações não lineares complexas entre as features.
"""


def load_data() -> Tuple[ndarray, ndarray]:
    """
    Carrega o dataset Íris e retorna os atributos e os alvos/targets.

    Returns:
        Tuple[ndarray, ndarray]: Tupla contendo os atributos e os alvos do dataset.
    """
    return datasets.load_iris(return_X_y=True)


def create_model() -> LogisticRegression:
    """
    Cria um modelo Regreção Logistica.

    Returns:
        LogisticRegression: Um modelo Logistic Regression configurado.
    """
    return LogisticRegression(max_iter=200)


def evaluate_model(model: LogisticRegression, X_test: ndarray, y_test: ndarray) -> None:
    """
    Avalia o modelo usando as métricas precisão, recall e f1-score.

    Args:
        model (LogisticRegression): Modelo treinado.
        X_test (ndarray): Atributos de teste.
        y_test (ndarray): Alvos/Targets de teste.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="macro")
    recall = recall_score(y_test, y_pred, average="macro")
    f1 = f1_score(y_test, y_pred, average="macro")

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1:.2f}")


def train_and_save_model(X: ndarray, y: ndarray, file_path: str) -> None:
    """
    Treina um modelo de classificação 'Logistic Regression', e salva o modelo treinado.

    Args:
        X (ndarray): Atributos de treinamento.
        y (ndarray): Alvos de treinamento.
        file_path (str): Caminho para salvar o modelo treinado.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = create_model()
    model.fit(X_train, y_train)

    # avalia o modelo
    evaluate_model(model, X_test, y_test)

    # salva o modelo
    dump(model, file_path)


if __name__ == "__main__":
    X, y = load_data()
    train_and_save_model(X, y, "./ml/iris_lr_v1.joblib")
