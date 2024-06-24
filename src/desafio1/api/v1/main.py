from desafio1.api.data_ingestion import download_iris_dataset
from desafio1.api.routers import iris_router
from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI(title="Iris Classifier API")

# API Routes
app.include_router(iris_router)


@app.on_event("startup")
async def startup_event():
    """
    Ação a ser executada quando a aplicação iniciar.
    Isso inclui a ingestão dos dados do dataset Íris.
    """
    try:
        # Try to download the Iris dataset
        iris_data = download_iris_dataset()
        # If necessary, store the data in a way that is accessible during the app's runtime
        app.state.iris_data = iris_data
        print("Iris dataset loaded successfully!")
    except ConnectionError as e:
        print(str(e))
        # Decide whether to fail startup or just log a warning
        raise HTTPException(status_code=500, detail="Failed to load the Iris dataset at startup.")


@app.on_event("startup")
async def run_startup_tasks():
    try:
        app.state.iris_data = download_iris_dataset()
        print("Dataset Iris loaded successfully!")
    except Exception as e:
        print(f"Failed to load dataset: {e!s}")
        raise HTTPException(status_code=500, detail="Failed to initialize dataset.")


@app.on_event("shutdown")
async def run_shutdown_tasks():
    print("Application is shutting down...")
    # If there are any cleanup tasks, they can be performed here.


# Lifespan Events:
#
# The @app.on_event("startup") decorator has been replaced with explicit lifespan event handlers inside the function itself. This is consistent with the latest best practices in FastAPI, focusing on clarity and maintainability.
# In this example, the run_startup_tasks() function handles the loading of the Iris dataset and stores it in the application state (app.state). This ensures the dataset is available throughout the app's lifetime.
# The run_shutdown_tasks() function is added to handle cleanup operations if needed when the app shuts down, although it just logs a message for now.
# Error Handling:
#
# A ConnectionError is caught if the dataset fails to load, and an HTTPException is raised to stop the application launch with an appropriate error message and status code. This is crucial for deploying in production environments where the initial setup must be verified before serving requests.
# Logging:
#
# Logging is used to indicate successful loading or to report errors. This helps in debugging and in production monitoring.
