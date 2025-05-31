FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy only dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy the rest of the application
COPY . .

# Development stage
FROM base as development
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# Production stage
FROM base as production
RUN poetry run python manage.py collectstatic --noinput
CMD ["poetry", "run", "gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000"] 