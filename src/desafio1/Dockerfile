# Use uma imagem base do Python
FROM python:3.11

# Configure o diretório de trabalho
WORKDIR /app

# Copie o arquivo pyproject.toml e poetry.lock para o contêiner
COPY pyproject.toml poetry.lock /app/

# Instale o Poetry
RUN pip install poetry

# Instale as dependências
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copie o restante do código para o contêiner
COPY . /app

# Exponha a porta que a API vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "api.v1.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
