from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

CLAVE_SECRETA = "clave_secreta"
ALGORITHM = "HS256"

def encode_token(payload: dict):
    token = jwt.encode(payload, CLAVE_SECRETA, algorithm=ALGORITHM)
    return token
def decode_token(token):
    data = jwt.decode(token, CLAVE_SECRETA, algorithms=[ALGORITHM])
    return data
def generar_hash(password: str):
    return pwd_context.hash(password)

def verificar_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )