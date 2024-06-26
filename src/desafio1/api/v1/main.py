import glob
import os
import pickle

from desafio1.api.services.data_service import download_iris_dataset
from desafio1.api.v1.routers.iris_router import app_iris_predict_v1
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Iris Classifier API")

app.include_router(app_iris_predict_v1, prefix="/v1")


def get_latest_model_path(models_dir: str) -> str:
    """
    Obtém o caminho do arquivo de modelo mais recente no diretório fornecido.

    Args:
        models_dir (str): Diretório onde os modelos estão armazenados.

    Returns:
        str: Caminho do arquivo de modelo mais recente.
    """
    model_files = glob.glob(os.path.join(models_dir, "iris_knn_v1_*.pkl"))  # Mudança para .pkl
    if not model_files:
        raise ModelNotFoundError()
    latest_model = max(model_files, key=os.path.getctime)
    return latest_model


class ModelNotFoundError(Exception):
    def __init__(self, message="Nenhum modelo encontrado no diretório especificado."):
        self.message = message
        super().__init__(self.message)


@app.get("/")
async def read_root() -> dict:
    """
    Endpoint raiz para verificar o status da API.

    Returns:
        dict: Mensagem de boas-vindas.
    """
    return {"message": "Welcome to the Iris Classifier API"}


@app.on_event("startup")
async def startup_event() -> None:
    """
    Ação a ser executada quando a aplicação iniciar.
    Isso inclui a ingestão dos dados do dataset Íris e o carregamento do modelo.
    """
    try:
        # Carrega o dataset Íris
        iris_data = download_iris_dataset()
        app.state.iris_data = iris_data

        # Carrega o modelo treinado mais recente
        model_dir = "./saved_models"
        model_path = get_latest_model_path(model_dir)
        with open(model_path, "rb") as f:
            app.state.model = pickle.load(f)  # Use pickle para carregar o modelo
        print(f"Modelo carregado com sucesso: {model_path}")
    except ModelNotFoundError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Falha ao carregar o modelo no startup.") from e
    except ConnectionError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Falha ao carregar o dataset Iris no startup.") from e
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Erro inesperado ao iniciar a aplicação.") from e


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """
    Ação a ser executada quando a aplicação for desligada.
    """
    print("Aplicação está sendo desligada...")
