# fastapi-clean-arch

This repository is a starting point for building scalable and maintainable FastAPI applications following Clean Architecture principles. The project emphasizes layer separation, modularity, and best practices, making it easy to evolve and test the system.

## Project Structure

```
src/
├── core/         # Core settings, logger, configuration
├── domain/       # Domain models, schemas, and services
│   ├── models/
│   ├── schemas/
│   └── services/
├── external/     # Integrations with external services (e.g., OpenAI)
├── http/         # HTTP routes, controllers, and exceptions
│   ├── exceptions/
│   └── v1/
├── infra/        # Infrastructure: database, repositories, migrations
│   ├── db.py
│   ├── migrations/
│   └── repository/
├── main.py       # Application entrypoint
├── __init__.py

tests/            # Unit and integration tests
```

## Getting Started with Docker

Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed.

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd fastapi-clean-arch
   ```

2. **Configure environment variables:**
   Create a `.env` file in the project root and set the required variables.

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
