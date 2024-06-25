# Instalar a versão correta do Python
pyenv install 3.11.0

# Configurar o Poetry para usar a versão correta do Python
cd /caminho/do/seu/projeto
poetry env use 3.11.0

# Ativar o ambiente virtual do Poetry
poetry shell

# Verificar a versão do Python
python --version
