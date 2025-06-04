# Development Guidelines

## Technology Stack

### Python
- Use Python version 3.12 for all development
- Ensure compatibility with Python 3.12+ features
- Use type hints throughout the codebase

### Package Management
- Use 'uv' for all package management operations
- Create virtual environments with `uv venv`
- Install packages with `uv pip install`
- Pin dependencies in pyproject.toml
- Use `uv pip install -e .` for development installation

### Build System
- Use hatchling as the build backend
- Configure build settings in pyproject.toml

## Code Quality

### Linting and Formatting
- Use ruff for both linting and formatting
- Run linting with `ruff check .`
- Format code with `ruff format .`
- Use ruff defaults for linting and formatting settings in pyproject.toml
- Include FastAPI-specific linting rules in pyproject.toml

### Type Checking
- Use pyright for static type checking
- Run type checking with `pyright`
- Ensure all functions and methods have proper type annotations
- Configure type checking settings in pyproject.toml

## Project Structure
- Organize code into logical modules and packages
- Follow the repository pattern for data access
- Keep models, repositories, services, and routes in separate directories
- Store database migrations in the migrations directory
- Place documentation in the docs directory

## Testing
- Write tests for all new functionality
- Use the provided test_main.http file for API endpoint testing
- Ensure tests pass before submitting changes

## Documentation
- Keep documentation up-to-date with code changes
- Document all public APIs, classes, and functions
- Follow clear and consistent documentation style
- Update README.md when adding new features or changing existing ones
- Use reStructuredText for documentation style
- Use triple double quotes for docstrings

## Git Workflow
- Create feature branches for new development
- Write clear, descriptive commit messages
- Reference issue numbers in commit messages when applicable
- Keep commits focused and atomic
- Use conventional commits for commit messages

## Security Practices
- Never hardcode sensitive information
- Use environment variables for configuration
- Validate all input data
- Follow secure coding practices
- Use HTTPS in production environments

## License
- Use GPLv3 license
- Include license headers in source files when appropriate

## Dependencies
- Core dependencies:
  - fastapi
  - uvicorn
  - pydantic
  - sqlalchemy
  - alembic
  - python-dotenv
- Development dependencies:
  - ruff
  - pyright
  - hatchling