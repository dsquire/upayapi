# uPay API

FastAPI implementation of a TouchNet Marketplace uPay posting endpoint.

## Overview

This API handles uPay Posting URL parameters sent by the TouchNet Marketplace uPay payment gateway. It processes payment transaction data and stores it in a database.

## Features

- Secure validation of posting requests using a posting key
- Validation of all required parameters
- Storage of transaction data in a database
- Support for both SQLite (development) and PostgreSQL (production)
- Comprehensive error handling and logging
- Database migrations using Alembic

## Requirements

- Python 3.12+
- Dependencies listed in pyproject.toml

## Installation

### Development Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/upayapi.git
   cd upayapi
   ```

2. Create a virtual environment using uv:
   ```
   uv venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`

4. Install the package in development mode:
   ```
   uv pip install -e .
   ```

5. Create a `.env` file with your configuration:
   ```
   DEBUG=True
   DATABASE_URL=sqlite:///./upay.db
   POSTING_KEY=your_secure_posting_key
   ```

## Usage

### Running the API

Start the API server with:

```
uvicorn upayapi.main:app --reload
```

The API will be available at http://localhost:8000

### API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /upay/posting`: Main endpoint for processing uPay transactions

### Database Migrations

Initialize the database:

```
alembic upgrade head
```

Create a new migration after model changes:

```
alembic revision --autogenerate -m "Description of changes"
```

## Testing

Run tests with:

```
pytest
```

## License

This project is licensed under the GPLv3 License - see the LICENSE file for details.
