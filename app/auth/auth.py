from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXIPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")



def generar_hash(password: str):
    return pwd_context.hash(password)

def verificar_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def crear_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt