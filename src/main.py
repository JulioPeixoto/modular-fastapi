from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .core.db import mongodb
from fastapi import FastAPI
from .api import api_router
from .logger import logger
import asyncio
import uvicorn
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Função async para criar as collections no Data Base"""
    try:
        await mongodb.create_collections()
        yield
    except asyncio.CancelledError:
        pass
    except Exception as e:
        logger(f"Erro ao se conectar com Data Base: {e}")
    finally:
        await mongodb.close()


app = FastAPI(title="Rag", lifespan=lifespan)

_ORIGINS_ = os.getenv("ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware, allow_origins=_ORIGINS_, allow_methods=["*"], allow_headers=["*"]
)

# Incluir todas as rotas da API
app.include_router(api_router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
