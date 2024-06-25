import glob
import os

from api.services.data_service import download_iris_dataset
from api.v1.routers.iris_router import app_iris_predict_v1
from fastapi import FastAPI, HTTPException
from joblib import load

app = FastAPI(title="Iris Classifier API")

app.include_router(app_iris_predict_v1)


def get_latest_model_path(models_dir: str) -> str:
    """
    Obtém o caminho do arquivo de modelo mais recente no diretório fornecido.

    Args:
        models_dir (str): Diretório onde os modelos estão armazenados.

    Returns:
        str: Caminho do arquivo de modelo mais recente.
    """
    model_files = glob.glob(os.path.join(models_dir, "iris_lr_v1_*.joblib"))
    if not model_files:
        raise FileNotFoundError("Nenhum modelo encontrado no diretório especificado.")
    latest_model = max(model_files, key=os.path.getctime)
    return latest_model


@app.get("/")
async def read_root():
    """
    Endpoint raiz para verificar o status da API.

    Returns:
        dict: Mensagem de boas-vindas.
    """
    return {"message": "Welcome to the Iris Classifier API"}


@app.on_event("startup")
async def startup_event():
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
        app.state.model = load(model_path)
        print(f"Modelo carregado com sucesso: {model_path}")
    except FileNotFoundError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Falha ao carregar o modelo no startup.")
    except ConnectionError as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Falha ao carregar o dataset Iris no startup.")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Ação a ser executada quando a aplicação for desligada.
    """
    print("Aplicação está sendo desligada...")
