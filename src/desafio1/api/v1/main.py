import logging

from api.services.data_service import download_iris_dataset
from api.v1.routers.iris_router import app_iris_predict_v1
from fastapi import FastAPI, HTTPException
from joblib import load

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Iris Classifier API")


@app.on_event("startup")
async def startup_event() -> None:
    """
    Ação a ser executada quando a aplicação iniciar.
    Isso inclui a ingestão dos dados do dataset Íris e o carregamento do modelo treinado.

    Raises:
        HTTPException: Se houver um problema ao carregar o dataset ou o modelo treinado.
    """
    try:
        iris_data = download_iris_dataset()
        # Armazena os dados no estado da aplicação
        app.state.iris_data = iris_data
        # Carrega o modelo treinado
        app.state.model = load("ml/iris_lr_v1.joblib")
        logger.info("Dataset Íris e modelo carregados com sucesso!")
    except FileNotFoundError as e:
        logger.exception("Modelo não encontrado")
        raise HTTPException(status_code=500, detail="Modelo não encontrado no startup.") from e
    except ConnectionError as e:
        logger.exception("Erro de conexão ao baixar o dataset Íris")
        raise HTTPException(status_code=500, detail="Erro de conexão ao baixar o dataset Íris.") from e
    except Exception as e:
        logger.exception("Erro inesperado no startup")
        raise HTTPException(status_code=500, detail="Erro inesperado no startup.") from e


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """
    Ação a ser executada quando a aplicação está sendo desligada.
    """
    logger.info("Aplicação está sendo desligada...")


app.include_router(app_iris_predict_v1)
