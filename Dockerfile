FROM python:3.11-slim

USER root
RUN apt-get update && \
    apt-get install -y curl build-essential python3-dev && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 - && \
    ln -s /etc/poetry/bin/poetry /usr/local/bin/poetry

WORKDIR /app

# Copie e instale as dependências do requirements.txt
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir cython
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o contêiner
COPY . /app

ENV PYTHONPATH /app

# Porta para a aplicação
EXPOSE 8000

# Comando padrão para iniciar a aplicação
CMD ["uvicorn", "src.desafio1.api.v1.main:app", "--host", "0.0.0.0", "--port", "8000"]
