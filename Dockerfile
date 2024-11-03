FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . /app

EXPOSE 8008

CMD ["uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8008"]
