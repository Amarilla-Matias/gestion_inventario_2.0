from pydantic import BaseModel
from app.auth.auth import generar_hash, verificar_password, encode_token, decode_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.database.database import eliminar_usuario_db, actualizar_usuario_db, agregar_usuarios_db, obtener_usuario_por_username, listar_usuarios_db
from fastapi import APIRouter, Depends, HTTPException
router = APIRouter(
    tags=["usuarios"]
)

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
class UsuarioCreate(BaseModel):
    username: str
    password: str
    rol: str

class UsuarioUpdate(BaseModel):
    username: str
    password: str
    rol: str

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = obtener_usuario_por_username(form_data.username)
    print(user)
    print(form_data.password)
    if not user or not verificar_password(form_data.password, user[2]):
        raise HTTPException(status_code=400, detail= "Usuario Incorrecto")
    
    token = encode_token({
        "username": user[1],
        "rol": user[3]
    })

    return{"access_token": token}
def get_current_user(token: str = Depends(oauth_scheme)):
    data = decode_token(token)
    username = data["username"]
    user = obtener_usuario_por_username(username)
    return user

def verificar_admin(
    user: dict = Depends(get_current_user)
):
    if user[3] != "admin":
        raise HTTPException(status_code=400, detail="No tienes permisos")
    return user
@router.get("/perfil")
def perfil(user:dict = Depends(get_current_user)):
    return user



@router.get("/usuarios")
def listar_usuarios():
    usuario = listar_usuarios_db()
    resultado = []
    for p in usuario:
        resultado.append({
            "id": p[0],
            "usuario": p[1],
            "contraseña": p[2],
            "rol": p[3]
        })
    return resultado

@router.post("/usuarios")
def registrar_usuario(usuario: UsuarioCreate):

    password_hash = generar_hash(usuario.password)
    agregar_usuarios_db(
        usuario.username, 
        password_hash, 
        usuario.rol)
    return {"mensaje": "Usuario creado exitosamente"}


@router.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario: UsuarioUpdate, admin = Depends(verificar_admin)):
    password_hash = generar_hash(usuario.password)
    actualizar_usuario_db(
        id,
        usuario.username,
        password_hash,
        usuario.rol
    )
    return {"mensaje": "Datos actualizados correctamente"}


@router.delete("/usuarios/{id}")
def eliminar_usuario(id: int , admin = Depends(verificar_admin)):
    eliminar_usuario_db(id)
    return {"mensaje:" f"Usuario {id} eliminado"}
