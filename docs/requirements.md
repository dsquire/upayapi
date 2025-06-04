# uPay API Requirements

## Project Overview
This project implements a FastAPI application that handles uPay Posting URL parameters. It processes payment transaction 
data sent by the TouchNet Marketplace uPay payment gateway.

## Technology Stack

### Core Technologies
- **Python**: Version 3.12
- **FastAPI**: Web framework for building APIs
- **Pydantic**: Data validation and settings management
- **SQLAlchemy**: ORM for database operations
- **Alembic**: Database migration tool

### Database
- **Development**: SQLite
- **Production**: PostgreSQL

### Development Tools
- **Package Manager**: uv
- **Linting & Formatting**: Ruff
- **Type Checking**: Pyright
- **License**: GPLv3

## API Requirements

### Endpoint Specifications
The API must implement a POST endpoint at `/upay/posting` that accepts the following parameters from uPay:

#### Required Parameters
- `posting_key`: Authentication key for validating requests
- `tpg_trans_id`: Transaction reference number assigned by Payment Gateway
- `session_identifier`: Unique session identifier code
- `pmt_status`: Transaction status ('success' or 'cancelled')
- `pmt_amt`: Transaction amount (max: $99,999.99)
- `pmt_date`: Transaction processing date (format: mm/dd/yyyy)
- `name_on_acct`: Name on payment account

## Security Requirements
- Validate the `posting_key` to ensure requests come from authorized sources
- Implement proper input validation for all parameters
- Follow secure coding practices to prevent injection attacks
- Use HTTPS in production environments

## Data Storage Requirements
- Store all transaction data in the database
- Implement proper error handling and logging
- Ensure data integrity through validation
