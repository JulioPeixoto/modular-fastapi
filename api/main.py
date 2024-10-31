from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routes import routes
import uvicorn
import os


app = FastAPI(title="Rag")

_ORIGINS_ = os.getenv("ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware, allow_origins=_ORIGINS_, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(routes.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    