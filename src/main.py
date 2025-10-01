from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import api_router
from src.core.logger import logger
from src.core.settings import settings
from src.infra.db import close_db, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
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


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todas as rotas da API
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
