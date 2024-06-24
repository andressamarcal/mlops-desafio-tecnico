from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configurações do JWT
SECRET_KEY = "SEU_SEGREDO_AQUI"  # Deve ser um segredo complexo em produção
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Duração do token

# Instância para lidar com hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Definição de onde o token será recebido
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Gera um token de acesso JWT com uma carga útil específica e uma validade opcional."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    """Verifica se uma senha em texto plano corresponde ao hash armazenado."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Gera um hash para uma senha em texto plano."""
    return pwd_context.hash(password)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Utiliza o token JWT para recuperar o usuário atual."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid JWT token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid JWT token")


async def authenticate_user(fake_db, username: str, password: str):
    """Autentica um usuário verificando suas credenciais."""
    user = fake_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user
