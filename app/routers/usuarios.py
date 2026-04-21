from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
import sqlite3
from pydantic import BaseModel
from app.database.database import agregar_usuarios_db, listar_usuarios_db, actualizar_usuario_db, eliminar_usuario_db, obtener_usuario_por_username
from datetime import timedelta
from app.auth.auth import generar_hash, SECRET_KEY, ALGORITHM, verificar_password, crear_token, ACCESS_TOKEN_EXIPIRE_MINUTES

router = APIRouter(
    prefix ="/usuarios",
    tags=["usuarios"]
)
DB_PATH = "app/database/inventario.db"
oauth2_scheme = OAuth2PasswordBearer (tokenUrl ="login")
class UsuarioUpdate(BaseModel):
    username: str
    password: str
    rol: str

class UsuarioCreate(BaseModel):
    username: str
    password: str
    rol : str

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = obtener_usuario_por_username(form_data.username)
    if not usuario or not verificar_password(form_data.password, usuario["password_hash"]):
        raise HTTPException(status_code=400, detail="Credenciales invalidas")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXIPIRE_MINUTES)
    access_token = crear_token(
        data={"sub": usuario["username"], "rol": usuario["rol"]},
        expires_delta= access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def obtener_usuario_actual(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        rol: str = payload.get("rol")
        if username is None:
            raise HTTPException(status_code=401, detail="Token invalido")
        return {"username": username, "rol": rol}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalido")

@router.get("/usuarios/me")
def leer_usuario_actual(usuario: dict = Depends(obtener_usuario_actual)):
    return usuario


@router.post("/usuarios")
def registrar_usuario(usuario: UsuarioCreate):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM usuarios WHERE username = ?", (usuario.username,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="El usuario ya existe")
        
        password_hash = generar_hash(usuario.password)
        cursor.execute(
            "INSERT INTO usuarios (username, password_hash, rol) VALUES(?, ?, ?)",
            (usuario.username, password_hash, usuario.rol)

        )
        conn.commit()
    return {"mensaje": "Usuario creado exitosamente"}



@router.get("/")
def listar_usuario():
    usuarios = listar_usuarios_db()

    resultado =[]
    for u in usuarios:
        resultado.append({
            "id" : u[0],
            "Usuario" : u[1],
            "Constraseña" : u[2],
            "Rol" : u[3]
        })
    return resultado

@router.put("/{id}")
def actualizar_usuario(id: int, usuario: UsuarioUpdate):
    password_hash = generar_hash(usuario.password)
    actualizar_usuario_db(
        id,
        usuario.username,
        password_hash,
        usuario.rol
    )
    return {"mensaje": "Datos actualizados correctamente"}

@router.delete("/{id}")
def eliminar_usuario(id):
    eliminar_usuario_db(id)
    return {"mensaje:" f"Usuario {id} eliminado"}