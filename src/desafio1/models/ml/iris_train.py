import os
import pickle
from collections import Counter
from datetime import datetime
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import ndarray
from sklearn import datasets
from sklearn.metrics import (
    accuracy_score,
    auc,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_curve,
)
from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score,
    learning_curve,
    train_test_split,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm


class IrisModelTrainer:
    def __init__(self) -> None:
        """
        Inicializa a classe IrisModelTrainer com um pipeline de padronização e KNN.
        """
        self.pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("classifier", KNeighborsClassifier(n_neighbors=5)),
            ]
        )

    def load_data(self) -> Tuple[ndarray, ndarray]:
        """
        Carrega o dataset Íris e retorna os atributos e os alvos/targets.

        Returns:
            Tuple[ndarray, ndarray]: Tupla contendo os atributos e os alvos do dataset.
        """
        return datasets.load_iris(return_X_y=True)

    def split_data(
        self, X: ndarray, y: ndarray
    ) -> Tuple[ndarray, ndarray, ndarray, ndarray]:
        """
        Divide os dados em conjuntos de treinamento e teste com estratificação.

        Args:
            X (ndarray): Atributos do dataset.
            y (ndarray): Alvos do dataset.

        Returns:
            Tuple[ndarray, ndarray, ndarray, ndarray]: Conjuntos de dados divididos em treinamento e teste.
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        return X_train, X_test, y_train, y_test

    def plot_distribution(
        self, y_train: ndarray, y_test: ndarray, plot_path: str
    ) -> None:
        """
        Plota a distribuição das classes nos conjuntos de treinamento e teste.

        Args:
            y_train (ndarray): Alvos do conjunto de treinamento.
            y_test (ndarray): Alvos do conjunto de teste.
            plot_path (str): Caminho para salvar os gráficos.
        """
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))

        train_counts = Counter(y_train)
        test_counts = Counter(y_test)

        ax[0].bar(train_counts.keys(), train_counts.values(), color="blue")
        ax[0].set_title("Distribuição no Conjunto de Treinamento")
        ax[0].set_xlabel("Classes")
        ax[0].set_ylabel("Contagem")

        ax[1].bar(test_counts.keys(), test_counts.values(), color="green")
        ax[1].set_title("Distribuição no Conjunto de Teste")
        ax[1].set_xlabel("Classes")
        ax[1].set_ylabel("Contagem")

        plt.savefig(os.path.join(plot_path, "class_distribution.png"))
        plt.close()

    def plot_metrics(self, y_test: ndarray, y_pred: ndarray, plot_path: str) -> None:
        """
        Plota as métricas do modelo e salva os gráficos.

        Args:
            y_test (ndarray): Alvos/Targets de teste.
            y_pred (ndarray): Predições do modelo.
            plot_path (str): Caminho para salvar os gráficos.
        """
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, average="macro"),
            "recall": recall_score(y_test, y_pred, average="macro"),
            "f1_score": f1_score(y_test, y_pred, average="macro"),
        }

        fig, ax = plt.subplots()
        ax.plot(metrics.keys(), metrics.values(), marker="o", linestyle="-")
        ax.set_title("Model Metrics")
        ax.set_ylim(0, 1)
        for i, v in enumerate(metrics.values()):
            ax.text(i, v + 0.01, f"{v:.2f}", ha="center")

        plt.savefig(os.path.join(plot_path, "model_metrics.png"))
        plt.close()

    def plot_confusion_matrix(
        self, y_test: ndarray, y_pred: ndarray, plot_path: str
    ) -> None:
        """
        Plota a matriz de confusão e salva o gráfico.

        Args:
            y_test (ndarray): Alvos/Targets de teste.
            y_pred (ndarray): Predições do modelo.
            plot_path (str): Caminho para salvar os gráficos.
        """
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=np.unique(y_test),
            yticklabels=np.unique(y_test),
        )
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.title("Confusion Matrix")
        plt.savefig(os.path.join(plot_path, "confusion_matrix.png"))
        plt.close()

    def plot_roc_curve(self, y_test: ndarray, y_proba: ndarray, plot_path: str) -> None:
        """
        Plota a curva ROC e salva o gráfico.

        Args:
            y_test (ndarray): Alvos/Targets de teste.
            y_proba (ndarray): Probabilidades preditas pelo modelo.
            plot_path (str): Caminho para salvar os gráficos.
        """
        fpr = {}
        tpr = {}
        roc_auc = {}

        for i in range(len(np.unique(y_test))):
            fpr[i], tpr[i], _ = roc_curve(y_test == i, y_proba[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])

        plt.figure(figsize=(8, 6))
        for i in range(len(np.unique(y_test))):
            plt.plot(
                fpr[i],
                tpr[i],
                label=f"ROC curve (area = {roc_auc[i]:.2f}) for label {i}",
            )
        plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("Receiver Operating Characteristic")
        plt.legend(loc="lower right")
        plt.savefig(os.path.join(plot_path, "roc_curve.png"))
        plt.close()

    def plot_dataset_info(self, X: ndarray, plot_path: str) -> None:
        """
        Plota informações básicas sobre o dataset.

        Args:
            X (ndarray): Atributos do dataset.
            plot_path (str): Caminho para salvar os gráficos.
        """
        fig, ax = plt.subplots(2, 2, figsize=(12, 10))

        feature_names = [
            "Comprimento Sépala",
            "Largura Sépala",
            "Comprimento Pétala",
            "Largura Pétala",
        ]
        for i in range(4):
            ax[i // 2, i % 2].hist(X[:, i], bins=20, color="blue", alpha=0.7)
            ax[i // 2, i % 2].set_title(f"Distribuição de {feature_names[i]}")
            ax[i // 2, i % 2].set_xlabel(feature_names[i])
            ax[i // 2, i % 2].set_ylabel("Frequência")

        plt.tight_layout()
        plt.savefig(os.path.join(plot_path, "dataset_info.png"))
        plt.close()

    def plot_learning_curve(
        self, model: Pipeline, X: ndarray, y: ndarray, plot_path: str
    ) -> None:
        """
        Plota a curva de aprendizado do modelo.

        Args:
            model: O modelo a ser avaliado.
            X (ndarray): Atributos do dataset.
            y (ndarray): Alvos do dataset.
            plot_path (str): Caminho para salvar os gráficos.
        """
        train_sizes, train_scores, test_scores = learning_curve(
            model, X, y, cv=5, n_jobs=-1, train_sizes=np.linspace(0.1, 1.0, 10)
        )

        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)

        plt.figure()
        plt.title("Learning Curve")
        plt.xlabel("Training examples")
        plt.ylabel("Score")
        plt.grid()

        plt.fill_between(
            train_sizes,
            train_scores_mean - train_scores_std,
            train_scores_mean + train_scores_std,
            alpha=0.1,
            color="r",
        )
        plt.fill_between(
            train_sizes,
            test_scores_mean - test_scores_std,
            test_scores_mean + test_scores_std,
            alpha=0.1,
            color="g",
        )
        plt.plot(
            train_sizes, train_scores_mean, "o-", color="r", label="Training score"
        )
        plt.plot(
            train_sizes,
            test_scores_mean,
            "o-",
            color="g",
            label="Cross-validation score",
        )

        plt.legend(loc="best")
        plt.savefig(os.path.join(plot_path, "learning_curve.png"))
        plt.close()

    def evaluate_model(
        self, model: Pipeline, X_test: ndarray, y_test: ndarray, plot_path: str
    ) -> None:
        """
        Avalia o modelo usando as métricas precisão, recall e f1-score.

        Args:
            model (Pipeline): Modelo treinado.
            X_test (ndarray): Atributos de teste.
            y_test (ndarray): Alvos/Targets de teste.
            plot_path (str): Caminho para salvar os gráficos de métricas.
        """
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)

        report = classification_report(y_test, y_pred)
        print("\nRelatório de Classificação:\n", report)

        self.plot_metrics(y_test, y_pred, plot_path)
        self.plot_confusion_matrix(y_test, y_pred, plot_path)
        self.plot_roc_curve(y_test, y_proba, plot_path)

    def train_model(self, X_train: ndarray, y_train: ndarray) -> Pipeline:
        """
        Treina o modelo de classificação usando KNN.

        Args:
            X_train (ndarray): Atributos de treinamento.
            y_train (ndarray): Alvos de treinamento.

        Returns:
            Pipeline: O pipeline treinado.
        """
        self.pipeline.fit(X_train, y_train)
        return self.pipeline

    def cross_validate_model(self, X: ndarray, y: ndarray, plot_path: str) -> None:
        """
        Realiza a validação cruzada no modelo para avaliar o desempenho e plota os resultados.

        Args:
            X (ndarray): Atributos do dataset.
            y (ndarray): Alvos do dataset.
            plot_path (str): Caminho para salvar os gráficos.
        """
        model = KNeighborsClassifier(n_neighbors=5)
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        scores = cross_val_score(model, X, y, cv=skf)

        print("Acurácia com validação cruzada:", scores.mean())
        print("Desvio padrão da acurácia:", scores.std())

        plt.figure(figsize=(10, 6))
        plt.plot(
            range(1, len(scores) + 1), scores, marker="o", linestyle="-", color="blue"
        )
        plt.title("Cross Validation Scores")
        plt.xlabel("Fold")
        plt.ylabel("Accuracy")
        plt.ylim(0, 1)
        plt.grid(True)
        plt.savefig(os.path.join(plot_path, "cross_validation_scores.png"))
        plt.close()

    def save_model(self, model: Pipeline, file_path: str) -> None:
        """
        Salva o modelo treinado em um arquivo.

        Args:
            model (Pipeline): Modelo treinado.
            file_path (str): Caminho para salvar o modelo treinado.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump(model, f)
        print(f"Modelo salvo como: {file_path}")

    def run(self, file_path: str, plot_path: str) -> None:
        """
        Executa o processo completo de carregamento dos dados, divisão dos dados, treinamento,
        avaliação e salvamento do modelo.

        Args:
            file_path (str): Caminho para salvar o modelo treinado.
            plot_path (str): Caminho para salvar os gráficos de métricas.
        """

        steps = 10
        with tqdm(total=100, desc="Treinamento do Modelo", unit="step") as pbar:
            X, y = self.load_data()
            pbar.update(steps)
            self.plot_dataset_info(X, plot_path)
            pbar.update(steps)

            X_train, X_test, y_train, y_test = self.split_data(X, y)
            pbar.update(steps)

            self.plot_distribution(y_train, y_test, plot_path)
            pbar.update(steps)

            self.cross_validate_model(X_train, y_train, plot_path)
            model = self.train_model(X_train, y_train)
            pbar.update(steps)
            
            self.evaluate_model(model, X_test, y_test, plot_path)
            pbar.update(steps)

            self.plot_learning_curve(model, X, y, plot_path)
            pbar.update(steps)

            self.save_model(model, file_path)
            pbar.update(steps)

        print("Treinamento concluído com sucesso!\n")
        print(f"Gráficos salvos em: {plot_path}")
        print(f"Modelo salvo como: {file_path}")


if __name__ == "__main__":
    trainer = IrisModelTrainer()
    timestamp = datetime.now().strftime("%Y%m%d")
    model_file_path = f"./saved_models/iris_knn_v1_{timestamp}.pkl"
    plot_path = "./data"
    trainer.run(model_file_path, plot_path)
