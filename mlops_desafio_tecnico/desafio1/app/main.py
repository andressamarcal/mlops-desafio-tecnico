from fastapi import FastAPI

from mlops_desafio_tecnico.desafio1.routers import iris_router

app = FastAPI(title="Iris Classifier API")

app.include_router(iris_router)
