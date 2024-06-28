FROM python:3.11-slim

USER root
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 - && \
    ln -s /etc/poetry/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONPATH /app

# porta para a aplicação
EXPOSE 8000

# Comandos
CMD ["make", "poetry", "run", "uvicorn", "src.desafio1.api.v1.main:app", "--host", "0.0.0.0", "--port", "8000"]
