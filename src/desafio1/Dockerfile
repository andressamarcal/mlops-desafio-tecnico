# Use a imagem base do Python
FROM python:3.11

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo pyproject.toml e poetry.lock para o contêiner
COPY pyproject.toml poetry.lock /app/

# Instale o Poetry
RUN pip install poetry

# Instale as dependências do projeto
RUN poetry install

# Copie todo o código do projeto para o contêiner
COPY . /app

# Comando para treinar o modelo
CMD ["make", "train"]

# Exponha a porta para a API
EXPOSE 8000

# Comando para rodar a API
CMD ["make", "api"]
