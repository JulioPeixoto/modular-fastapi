# Modular Layered FastAPI Boilerplate

This repo is a boilerplate for building scalable and maintainable FastAPI applications using a modular, layered architecture. It provides a clean separation of concerns and is ready to be extended for production use.

## Project Structure

```
src/
├── __pycache__/
├── api/         # API routes and endpoints
├── core/        # Core settings, configuration, and utilities
├── lib/         # Shared libraries and helpers
├── model/       # Database models and ORM definitions
├── queries/     # Database queries and repository logic
├── schemas/     # Pydantic schemas for data validation
├── services/    # Business logic and service layer
├── __init__.py
├── logger.py    # Logging configuration
├── main.py      # Application entrypoint

tests/           # Unit and integration tests
```

## Getting Started with Docker

Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd boilerplate-llmapp-fastapi
   ```

2. **Copy and configure environment variables:**
   Create a `.env` file in the root directory and set the required environment variables as needed.

3. **Start the application:**
   ```bash
   docker-compose up --build
   ```

   This will start the FastAPI app, PostgreSQL, and RabbitMQ services.

4. **Access the services:**
   - FastAPI: [http://localhost:8008/docs](http://localhost:8008/docs)
   - PostgreSQL: `localhost:5432` (user: `postgres`, password: `password123`)
   - RabbitMQ Management: [http://localhost:15672](http://localhost:15672) (user: `kalo`, password: `kalo`)

## License

MIT
