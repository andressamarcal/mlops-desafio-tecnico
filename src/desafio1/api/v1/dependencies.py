from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import ValidationError

"""
* Autenticação JWT: Este script define uma dependência oauth2_scheme que extrai o token de autenticação dos headers da requisição. A função get_current_user utiliza esse token para autenticar e obter o usuário.
* Validação de Usuário: A função get_current_active_user pode ser usada para garantir que apenas usuários autenticados e ativos possam acessar certos endpoints.
* Injeção de Configurações: get_settings poderia ser expandida para carregar configurações de forma dinâmica, baseando-se em variáveis de ambiente ou arquivos de configuração externos.
* Controle de Acesso por Role: get_user_with_role é uma função que você poderia utilizar para implementar controle de acesso baseado em roles.
"""


# JWT config
SECRET_KEY = "YOUR_SECRET_KEY_HERE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Instância OAuth2PasswordBearer que espera que o token esteja incluído no header da requisição
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Classe para representar um usuário autenticado
class User:
    username: str

    def __init__(self, username: str):
        self.username = username


# Função para obter o usuário atual com base no token JWT
async def get_current_user(token: str = Security(oauth2_scheme)) -> User:
    try:
        # Decodifica o token para extrair o username
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return User(username)
    except (JWTError, ValidationError):
        raise HTTPException(status_code=403, detail="Could not validate credentials")


# Função de dependência que pode ser usada para injetar configurações ou outros serviços
def get_settings():
    # Aqui poderia ser carregada uma configuração de ambiente ou arquivo
    return {"api_version": "v1"}


# Exemplo de dependência que requer um usuário autenticado
async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


# Injeção de dependência para verificar se o usuário tem um role específico
async def get_user_with_role(role: str, current_user: User = Depends(get_current_active_user)) -> User:
    # Implementar a lógica para verificar se o usuário tem o role necessário
    # Exemplo simples:
    allowed_roles = ["admin", "user"]
    if role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Operation not permitted")
    return current_user
