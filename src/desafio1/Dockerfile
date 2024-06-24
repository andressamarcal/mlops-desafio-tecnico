FROM python:3.11-slim

WORKDIR /app

# Configurar o ambiente para não criar arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Configurar o ambiente para não fazer buffering das saídas
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* /app/

# Poetry config:
# - Não criar um ambiente virtual dentro do container, pois o container já é um ambiente isolado
# - Instalar as dependências de produção
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

COPY . /app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
