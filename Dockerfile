FROM python:3.11-slim

USER root

# Instalar dependências necessárias
RUN apt-get update && \
    apt-get install -y curl build-essential python3-dev gcc g++ make && \
    apt-get clean

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONPATH /app

# Porta para a aplicação
EXPOSE 8000

# Comando padrão para iniciar a aplicação
CMD ["uvicorn", "src.desafio1.api.v1.main:app", "--host", "0.0.0.0", "--port", "8000"]
