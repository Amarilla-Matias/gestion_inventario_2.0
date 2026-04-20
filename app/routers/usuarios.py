from fastapi import APIRouter
from pydantic import BaseModel
from app.database.database import agregar_usuarios_db, listar_usuarios_db, actualizar_usuario_db, eliminar_usuario_db

router = APIRouter(
    prefix ="/usuarios",
    tags=["usuarios"]
)

class UsuarioUpdate(BaseModel):
    username: str
    password_hash: str
    rol: str

@router.post("/")
def agregar_usuarios(username, password_hash, rol):
    agregar_usuarios_db(username, password_hash, rol)
    return {"mensaje:" f"Usuario {username} creado"}

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
    actualizar_usuario_db(
        id,
        usuario.username,
        usuario.password_hash,
        usuario.rol
    )
    return {"mensaje": ("Datos actualizado correctamente")}

@router.delete("/{id}")
def eliminar_usuario(id):
    eliminar_usuario_db(id)
    return {"mensaje:" f"Usuario {id} eliminado"}