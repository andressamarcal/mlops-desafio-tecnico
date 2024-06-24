"""
Explicando o por quê da escolha da Regressão Logística para o projeto:
1. Algoritmo extremamente otimizado e simples para explicação(interpratabilidade do modelo), ou seja, bem menos caixa preta.
2. Novamente, tem uma tnterpretação bem simples. Seus coeficientes da regressão logística são interpretáveis e oferecem insights diretos sobre a importância das features(feature importance).
3. Bem rápida e, novamente, extremante eficiente (principalmente em cenários de score de crédito =D)
4. Treinamento e previsão rápidos, mesmo com grandes conjuntos de dados.
5. Algoritmo bom para dados lineares, ou seja, funciona bem quando há uma relação linear entre as features e a variável alvo/target. :)

Feature Engineering:
    Para esse dataset do Íris, escolhi aplicar a padronização (Standardization), que basicamente, é uma técnica de normalização dos dados.
    Essa técnica transforma os dados para que tenham média zero e desvio padrão igual a um, o que pode melhorar a performance
    dos modelos de machine learning, como é o caso da Regressao Logistica que é baseada em distâncias.

>> O unico ponto que ressalto, é o fato dele nem sempreo capturar complexidade, acaba sendo menos eficaz em capturar relações não lineares complexas entre as features.
"""

from typing import Tuple

from joblib import dump
from numpy import ndarray
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class IrisModelTrainer:
    def __init__(self):
        """
        Inicializa a classe IrisModelTrainer com um pipeline de padronização e regressão logística.
        """
        self.pipeline = Pipeline([("scaler", StandardScaler()), ("classifier", LogisticRegression(max_iter=200))])

    def load_data(self) -> Tuple[ndarray, ndarray]:
        """
        Carrega o dataset Íris e retorna os atributos e os alvos/targets.

        Returns:
            Tuple[ndarray, ndarray]: Tupla contendo os atributos e os alvos do dataset.
        """
        return datasets.load_iris(return_X_y=True)

    def split_data(self, X: ndarray, y: ndarray) -> Tuple[ndarray, ndarray, ndarray, ndarray]:
        """
        Divide os dados em conjuntos de treinamento e teste.

        Args:
            X (ndarray): Atributos do dataset.
            y (ndarray): Alvos do dataset.

        Returns:
            Tuple[ndarray, ndarray, ndarray, ndarray]: Conjuntos de dados divididos em treinamento e teste.
        """
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def evaluate_model(self, model: Pipeline, X_test: ndarray, y_test: ndarray) -> None:
        """
        Avalia o modelo usando as métricas precisão, recall e f1-score.

        Args:
            model (Pipeline): Modelo treinado.
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

    def train_model(self, X_train: ndarray, y_train: ndarray) -> Pipeline:
        """
        Treina o modelo de classificação usando Logistic Regression.

        Args:
            X_train (ndarray): Atributos de treinamento.
            y_train (ndarray): Alvos de treinamento.

        Returns:
            Pipeline: O pipeline treinado.
        """
        self.pipeline.fit(X_train, y_train)
        return self.pipeline

    def save_model(self, model: Pipeline, file_path: str) -> None:
        """
        Salva o modelo treinado em um arquivo.

        Args:
            model (Pipeline): Modelo treinado.
            file_path (str): Caminho para salvar o modelo treinado.
        """
        dump(model, file_path)

    def run(self, file_path: str) -> None:
        """
        Executa o processo completo de carregamento dos dados, divisão dos dados, treinamento,
        avaliação e salvamento do modelo.

        Args:
            file_path (str): Caminho para salvar o modelo treinado.
        """
        X, y = self.load_data()
        X_train, X_test, y_train, y_test = self.split_data(X, y)
        model = self.train_model(X_train, y_train)
        self.evaluate_model(model, X_test, y_test)
        self.save_model(model, file_path)


if __name__ == "__main__":
    trainer = IrisModelTrainer()
    trainer.run("./ml/iris_lr_v1.joblib")
