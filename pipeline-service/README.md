# Pipeline Service

The Pipeline Service is a FastAPI-based backend designed to ingest, process, and manage customer data. It acts as a bridge between an external data source (Mock Server) and a PostgreSQL database.

## 🚀 Features

- **Data Ingestion**: Fetches customer records from a mock Flask server and performs upserts (Insert or Update) into the database.
- **RESTful API**: Provides endpoints for retrieving paginated customer lists and individual customer details.
- **Database Integration**: Uses SQLAlchemy ORM to interact with PostgreSQL.
- **Dockerized**: Fully containerized using Docker for easy deployment and local development.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **Data Ingestion**: [Requests](https://requests.readthedocs.io/)
- **Environment Management**: [Python Dotenv](https://github.com/theskumar/python-dotenv)

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional but recommended)

### Environment Variables

The service expects the following environment variables:

- `DATABASE_URL`: PostgreSQL connection string (e.g., `postgresql://postgres:root@localhost:5432/customer_db`)
- `FLASK_BASE_URL`: Base URL of the Mock Server (e.g., `http://mock-server:3000`)

### Local Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```
   The server will start at `http://localhost:8000`.

### Running with Docker

Use the `docker-compose.yml` in the root directory:
```bash
docker-compose up --build
```

## 📖 API Documentation

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/ingest` | `POST` | Fetches data from the mock server and updates the local DB. |
| `/api/customers` | `GET` | Returns a paginated list of customers (supports `page` and `limit` query params). |
| `/api/customers/{id}` | `GET` | Returns details for a specific customer by ID. |

## 📂 Project Structure

- `app/api/`: API routes definition.
- `app/core/`: Configuration and core settings.
- `app/db/`: Database models and connection setup.
- `app/services/`: Business logic for data ingestion and processing.
- `main.py`: Entry point for the FastAPI application.
