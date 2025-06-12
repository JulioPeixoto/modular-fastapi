from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .core.database import create_tables, close_db
from fastapi import FastAPI
from .api import api_router
from .logger import logger
import os
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Função async para criar as tabelas no PostgreSQL"""
    try:
        create_tables()
        logger.info("Tabelas criadas com sucesso no PostgreSQL")
    except Exception as e:
        logger.error(f"Erro ao se conectar com PostgreSQL: {e}")
        
    yield
    
    try:
        close_db()
    except Exception as e:
        logger.error(f"Erro ao fechar conexão: {e}")


app = FastAPI(title="Modular Boilerplate", lifespan=lifespan)

_ORIGINS_ = os.getenv("ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware, allow_origins=_ORIGINS_, allow_methods=["*"], allow_headers=["*"]
)

# Incluir todas as rotas da API
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
