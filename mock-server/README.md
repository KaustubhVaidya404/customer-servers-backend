# Mock Server

A simple Flask-based mock server designed to provide mock customer data for testing and development.

## Tech Stack

- **Framework**: [Flask](https://flask.palletsprojects.com/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Language**: Python 3.12+

## Project Structure

```text
mock-server/
├── app/
│   ├── routes.py          # API endpoint definitions
│   ├── services/          # Business logic and data loading
│   └── utils/             # Helper functions (e.g., pagination)
├── data/
│   └── customers.json     # Mock customer data
├── main.py                # Server entry point
├── config.py              # Application configuration
├── pyproject.toml         # Dependency definitions
└── requirements.txt       # Legacy dependency list
```

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed on your machine.
- [uv](https://github.com/astral-sh/uv) (recommended) or `pip` for package management.

### Installation

1. Navigate to the `mock-server` directory:
   ```bash
   cd mock-server
   ```

2. Install dependencies using `uv`:
   ```bash
   uv sync
   ```
   *Alternatively, using pip:*
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

Start the server using `uv`:
```bash
uv run main.py
```
*Alternatively, using Python directly:*
```bash
python main.py
```

The server will be available at `http://0.0.0.0:3000`.

## API Documentation

### Health Check
- **Endpoint**: `GET /api/health`
- **Description**: Verify if the server is running.
- **Response**:
  ```json
  { "status": "ok" }
  ```

### Get Customers (Paginated)
- **Endpoint**: `GET /api/customers`
- **Description**: Retrieves a paginated list of customers.
- **Query Parameters**:
  - `page` (optional): The page number (default: 1).
  - `limit` (optional): Number of records per page (default: 10).
- **Example**: `GET /api/customers?page=1&limit=5`
- **Response**:
  ```json
  {
    "data": [...],
    "total": 100,
    "page": 1,
    "limit": 5
  }
  ```

### Get Customer by ID
- **Endpoint**: `GET /api/customers/<customer_id>`
- **Description**: Retrieves details for a specific customer.
- **Response**:
  ```json
  {
    "customer_id": 1,
    "first_name": "Amit",
    "last_name": "Sharma",
    "email": "amit.sharma@example.com",
    "phone": "+919876543210",
    "address": "Mumbai, Maharashtra, India",
    "date_of_birth": "1990-05-14",
    "account_balance": 15230.75,
    "created_at": "2025-01-10T09:30:00Z"
  }
  ```
- **Error (404)**:
  ```json
  { "error": "Customer not found" }
  ```

## Configuration

Configuration values like the data file path are managed in `config.py`. By default, it points to `data/customers.json`.
