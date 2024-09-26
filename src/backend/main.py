from fastapi import FastAPI
from models.database import engine, Base
from routes import predictionRoutes
from utils.helpers import log_requests_middleware  # Import the logging middleware

# Criação da tabela no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register the logging middleware
app.middleware("http")(log_requests_middleware)

# Registro das rotas
app.include_router(predictionRoutes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
